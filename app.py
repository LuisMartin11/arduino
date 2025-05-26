from flask import Flask, render_template, request, jsonify
import serial

app = Flask(__name__)

# Cambia 'COM3' por el puerto correcto de tu Arduino
try:
    arduino = serial.Serial('COM3', 9600, timeout=1)
except Exception as e:
    print(f'Error al abrir el puerto serial: {e}')
    arduino = None

comandos_arduino = {
    'encender_led1': b'1',
    'apagar_led1': b'0',
    'encender_led2': b'2',
    'apagar_led2': b'3',
    'encender_led3': b'4',
    'apagar_led3': b'5',
    # Puedes agregar intensidad, etc.
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/accion', methods=['POST'])
def accion():
    comando = request.form.get('comando')
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
    else:
        return jsonify({'error': 'Comando no reconocido'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)