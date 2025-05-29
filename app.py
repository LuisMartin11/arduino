from flask import Flask, render_template, request, jsonify
import serial
import re


app = Flask(__name__)

# Cambia 'COM3' por el puerto correcto de tu Arduino
try:
    arduino = serial.Serial('COM11', 9600, timeout=1)
except Exception as e:
    print(f'Error al abrir el puerto serial: {e}')
    arduino = None

comandos_arduino = {
    'encender_cuarto': b'1',
    'apagar_cuarto': b'0',
    'encender_sala': b'2',
    'apagar_sala': b'3',
    'encender_cocina': b'4',
    'apagar_cocina': b'5',
    'encender_ventilador': b'6',   # <--- Agrega esto
    'apagar_ventilador': b'7',     # <--- Y esto
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/accion', methods=['POST'])
def accion():
    comando = request.form.get('comando')
    intensidad = request.form.get('intensidad')  # Nuevo parámetro opcional

    if not comando:
        return jsonify({'error': 'No se envió el comando'}), 400

    if comando in comandos_arduino:
        if arduino is None:
            return jsonify({'error': 'Arduino no conectado'}), 500
        try:
            arduino.write(comandos_arduino[comando])
        except Exception as e:
            return jsonify({'error': f'Error al enviar al Arduino: {e}'}), 500
        return jsonify({'status': 'OK'})
    elif comando in ['intensidad_cuarto', 'intensidad_sala', 'intensidad_cocina']:
        if arduino is None:
            return jsonify({'error': 'Arduino no conectado'}), 500
        if intensidad is None:
            return jsonify({'error': 'No se envió la intensidad'}), 400
        try:
            # Formato: I1-valor (ejemplo: I1-128)
            if comando == 'intensidad_cuarto':
                arduino.write(f'I1-{intensidad}\n'.encode())
            elif comando == 'intensidad_sala':
                arduino.write(f'I2-{intensidad}\n'.encode())
            elif comando == 'intensidad_cocina':
                arduino.write(f'I3-{intensidad}\n'.encode())
        except Exception as e:
            return jsonify({'error': f'Error al enviar intensidad al Arduino: {e}'}), 500
        return jsonify({'status': 'OK'})
    else:
        return jsonify({'error': 'Comando no reconocido'}), 400
    
@app.route('/sensor', methods=['GET'])
def sensor():
        if arduino is None:
            return jsonify({'error': 'Arduino no conectado'}), 500
        try:
            # Lee varias líneas hasta encontrar una válida
            for _ in range(10):
                linea = arduino.readline().decode(errors='ignore').strip()
                # Espera una línea como: TEMP:xx.x;HUM:yy.y
                match = re.match(r'TEMP:([\d.]+);HUM:([\d.]+)', linea)
                if match:
                    temp = float(match.group(1))
                    hum = float(match.group(2))
                    return jsonify({'temperatura': temp, 'humedad': hum})
            return jsonify({'error': 'No se recibieron datos válidos'}), 500
        except Exception as e:
            return jsonify({'error': f'Error al leer del Arduino: {e}'}), 500
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)