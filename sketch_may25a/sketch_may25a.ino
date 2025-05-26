const int led1 = 9;
const int led2 = 10;
const int led3 = 11;

int intensidad1 = 255;
int intensidad2 = 255;
int intensidad3 = 255;

bool estado1 = false;
bool estado2 = false;
bool estado3 = false;

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String comando = Serial.readStringUntil('\n');
    comando.trim();

    if (comando == "1") { // Encender LED 1
      estado1 = true;
      analogWrite(led1, intensidad1);
    }
    else if (comando == "0") { // Apagar LED 1
      estado1 = false;
      analogWrite(led1, 0);
    }
    else if (comando == "2") { // Encender LED 2
      estado2 = true;
      analogWrite(led2, intensidad2);
    }
    else if (comando == "3") { // Apagar LED 2
      estado2 = false;
      analogWrite(led2, 0);
    }
    else if (comando == "4") { // Encender LED 3
      estado3 = true;
      analogWrite(led3, intensidad3);
    }
    else if (comando == "5") { // Apagar LED 3
      estado3 = false;
      analogWrite(led3, 0);
    }
    else if (comando.startsWith("I1-")) {
      int valor = comando.substring(3).toInt();
      intensidad1 = constrain(valor, 0, 255);
      if (estado1) analogWrite(led1, intensidad1);
    }
    else if (comando.startsWith("I2-")) {
      int valor = comando.substring(3).toInt();
      intensidad2 = constrain(valor, 0, 255);
      if (estado2) analogWrite(led2, intensidad2);
    }
    else if (comando.startsWith("I3-")) {
      int valor = comando.substring(3).toInt();
      intensidad3 = constrain(valor, 0, 255);
      if (estado3) analogWrite(led3, intensidad3);
    }
  }
}