# Proyecto Control de LEDs con Flask y Arduino

## Descripción

Este proyecto permite controlar tres LEDs conectados a un Arduino desde una interfaz web sencilla. Se utiliza Flask como servidor web que recibe comandos desde el frontend y los envía al Arduino vía comunicación serial para encender o apagar cada LED. Además, incluye un sistema básico de reconocimiento de voz en español para controlar los LEDs mediante comandos hablados.

## Tecnologías usadas

- **Arduino**: Control físico de LEDs mediante comunicación serial.
- **Python Flask**: Backend que recibe comandos HTTP y se comunica con Arduino.
- **HTML + Tailwind CSS + JavaScript**: Frontend para interfaz de usuario y reconocimiento de voz.
- **Reconocimiento de voz Web API**: Para interpretar comandos hablados en español.

## Funcionamiento

1. El usuario abre la interfaz web en el navegador.
2. Puede controlar manualmente los LEDs con botones para encender o apagar cada uno.
3. También puede activar el reconocimiento de voz y dar comandos como "encender luz uno", "apagar luz tres", etc.
4. El frontend envía los comandos al backend Flask vía HTTP POST.
5. Flask traduce esos comandos a caracteres específicos y los envía por el puerto serial al Arduino.
6. El Arduino interpreta el carácter recibido y enciende o apaga el LED correspondiente.

## Estructura del proyecto

- `app.py`: Servidor Flask que maneja las peticiones y comunicación con Arduino.
- `templates/index.html`: Archivo HTML con la interfaz de usuario y el código JavaScript para botones y voz.
- `arduino.ino`: Código para Arduino que recibe comandos seriales y controla los pines de los LEDs.

## Configuración

- Conecta los LEDs a los pines 9, 10 y 11 del Arduino.
- Configura el puerto serial correcto en `app.py`, por ejemplo:

  ```python
  arduino = serial.Serial('COM3', 9600, timeout=1)
  ```

  Cambia `'COM3'` por el puerto que corresponda en tu sistema operativo.

- Sube el código Arduino al dispositivo.

- Ejecuta el servidor Flask con:

  ```bash
  python app.py
  ```

- Abre el navegador en `http://localhost:5000`.

## Comandos reconocidos

* `encender_led1` / `apagar_led1`
* `encender_led2` / `apagar_led2`
* `encender_led3` / `apagar_led3`

Ejemplos de comandos de voz soportados:

* "encender luz uno"
* "apagar luz dos"
* "encender luz tres"

## Notas importantes

* Asegúrate que ningún otro programa esté usando el puerto serial (como el IDE de Arduino) para evitar conflictos.
* El reconocimiento de voz funciona sólo en navegadores compatibles con la Web Speech API (recomendado Google Chrome).
* Este proyecto es un prototipo básico para aprender integración entre web y Arduino.

