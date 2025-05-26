int led1 = 9;
int led2 = 10;
int led3 = 11;

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char cmd = Serial.read();
    switch (cmd) {
      case '1': digitalWrite(led1, HIGH); break;
      case '0': digitalWrite(led1, LOW); break;
      case '2': digitalWrite(led2, HIGH); break;
      case '3': digitalWrite(led2, LOW); break;
      case '4': digitalWrite(led3, HIGH); break;
      case '5': digitalWrite(led3, LOW); break;
    }
  }
}
