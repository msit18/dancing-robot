#include <Servo.h>

Servo servo1;

int pos = 0, incomingByte = 0;

void setup() {
  servo1.attach(9);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read() - 48;
    
    if (incomingByte == 1) {
      servo1.write(10);
      delay(50);
      servo1.write(0);
      delay(50);
    }
  }
  else {
    incomingByte = 0;
  }
}
