/* 
  DHTLogger
  Developed by Trevor Stanhope
  Data logger for DHT sensors
*/

/* --- Libraries --- */
#include "stdio.h"
#include <DHT.h>
#include <SD.h>

/* --- Pins --- */
#define SD_PIN 10
#define DHT_INTERNAL_PIN A0
#define DHT_EXTERNAL_PIN A1

/* --- Values --- */
#define DHT_TYPE DHT22
#define BAUD 9600
#define CHARS 8
#define BUFFER 128
#define DIGITS 4
#define PRECISION 2
#define INTERVAL 1000
#define TIMEOUT 1

/* --- Functions --- */
float get_int_temp(void);
float get_int_humidity(void);
float get_ext_temp(void);
float get_ext_humidity(void);

/* --- Objects --- */
DHT INT_DHT(DHT_INTERNAL_PIN, DHT_TYPE);
DHT EXT_DHT(DHT_EXTERNAL_PIN, DHT_TYPE);

/* --- Strings --- */
char INT_T[CHARS];
char INT_H[CHARS];
char EXT_T[CHARS];
char EXT_H[CHARS];

/* --- Line Buffers --- */
char CSV[BUFFER];
char COMMAND;

/* --- State --- */
int TIME = 0; // seconds on

/* --- Setup --- */
void setup() {
  Serial.begin(BAUD);
  Serial.setTimeout(TIMEOUT);
  pinMode(SD_PIN, OUTPUT);
  if (!SD.begin(SD_PIN)) {
    return;
  }
  INT_DHT.begin();
  EXT_DHT.begin();
}

/* --- Loop --- */
void loop() {
  TIME++;
  dtostrf(get_ext_temp(), DIGITS, PRECISION, EXT_T); 
  dtostrf(get_ext_humidity(), DIGITS, PRECISION, EXT_H);
  dtostrf(get_int_temp(), DIGITS, PRECISION, INT_T);
  dtostrf(get_int_humidity(), DIGITS, PRECISION, INT_H);
  sprintf(CSV, "%d,%s,%s,%s,%s",TIME, INT_T, EXT_T, INT_H, EXT_H);
  Serial.println(CSV);
  File datafile = SD.open("datalog.txt", FILE_WRITE);
  if (datafile) {
    datafile.println(CSV);
    datafile.close();
  }
  delay(INTERVAL);
}

/* --- Sensor Functions --- */
// Internal Humidity
float get_int_humidity() {
  float val = INT_DHT.readHumidity();
  if (isnan(val)) {
    return 0;
  }
  else {
    return val;
  }
}

// Internal Temperature
float get_int_temp() {
  float val = INT_DHT.readTemperature();
  if (isnan(val)) {
    return 0;
  }
  else {
    return val;
  }
}

// Get External Humidity
float get_ext_humidity() {
  float val = EXT_DHT.readHumidity();
  if (isnan(val)) {
    return 0;
  }
  else {
    return val;
  }
}

// Get External Temperature
float get_ext_temp() {
  float val = EXT_DHT.readTemperature();
  if (isnan(val)) {
    return 0;
  }
  else {
    return val;
  }
}
