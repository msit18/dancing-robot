//Run with Serial_attempt.py.  Used for testing if the arduino recieved write signals from the python code.

void setup() {
 Serial.begin(9600); 
}

void loop() {
  Serial.print(Serial.read());
 delay(1000); 
}
