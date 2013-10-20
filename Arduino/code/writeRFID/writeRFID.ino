// writeRFID.ino
// Trevor Stanhope
// Jan 29, 2013
// Writes Data to 13.56 MHz RFID Card

/* Dependent Libraries*/
#include <SoftwareSerial.h>

/* Global Objects */
#define txPin 4
#define rxPin 3
#define READ 0x02
#define DATA 0x03
#define WRITE 0x04
#define INTERVAL 1000

// For the RFID Module
SoftwareSerial rfidSerial(txPin, rxPin); // so the RFID can be read
int baudrate = 9600;
int interval = 1000;

// For STANDBY Mode (Valid RFID)

/* Functions*/
// Setup
void setup() {
  Serial.begin(baudrate);
  rfidSerial.begin(baudrate);
}

// Loop Actions
void loop() {
  int i = 0;
  rfidSerial.write(READ);
  if (rfidSerial.available()) {
    Serial.println("FOUND CARD");
    rfidSerial.write(WRITE);
    int bytes = rfidSerial.write("Hello");
    Serial.println(bytes);
    delay(100);
    rfidSerial.read(DATA);
    i = rfidSerial.peek();
    Serial.println(i);
  }
  else {
    Serial.println("SWIPE KEY CARD");
  }
  delay(INTERVAL); // check for card every on interval
}

