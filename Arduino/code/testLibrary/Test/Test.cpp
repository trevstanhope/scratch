/*
  Test.h - Test library for Wiring - implementation
  Copyright (c) 2006 John Doe.  All right reserved.
*/

/* --- Header --- */
#include "Arduino.h" // include core Wiring API
#include "Test.h" // include this library's description file
#include "HardwareSerial.h" // include description files for other libraries used (if any)

/* --- Constructor --- */
// Function that handles the creation and setup of instances
Test::Test(int givenValue) {
  value = givenValue; // initialize this instance's variables
  pinMode(13, OUTPUT); // do whatever is required to initialize the library
  Serial.begin(9600);
}

/* --- Public Methods --- */
// Functions available in Wiring sketches, this library, and other libraries
void Test::doSomething(void) {
  // even though this function is public, it can access
  // and modify this library's private variables
  Serial.print("value is ");
  Serial.println(value);
  doSomethingSecret();  // it can also call private functions of this library
}

/* --- PrivateMethods --- */
// Functions only available to other functions in this library
void Test::doSomethingSecret(void) {
  digitalWrite(13, HIGH);
  delay(200);
  digitalWrite(13, LOW);
  delay(200);
}

