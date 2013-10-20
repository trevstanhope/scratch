/* 
  testLibrary.ino
  Trevor Stanhope
*/
#include <Test.h>

// testLibrary

Test myTest = Test(2);

void setup() {
}

void loop() {
  myTest.doSomething();
  delay(500);
}
