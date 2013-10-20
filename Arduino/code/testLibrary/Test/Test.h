/*
  Test.h - Test library for Wiring - description
  Copyright (c) 2006 John Doe.  All right reserved.
*/

#ifndef Test_h // ensure this library description is only included once
#define Test_h
#include "Arduino.h" // include types & constants of Wiring core API

class Test {
  public: // user-accessible "public" interface
    Test(int);
    void doSomething(void);
  private: // library-accessible "private" interface
    int value;
    void doSomethingSecret(void);
};

#endif

