// ping
// Trevor Stanhope

#include <SoftwareSerial.h>
int interval = 1000;
byte val = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.write(1);
  delay(interval);
}
