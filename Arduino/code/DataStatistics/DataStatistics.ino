#include "Statistic.h"

Statistic myStats; 

void setup(void) 
{
  Serial.begin(9600);
  Serial.print("Demo Statistics lib ");
  Serial.println(STATISTIC_LIB_VERSION);
  myStats.clear(); //explicitly start clean
}

void loop(void) 
{
  long rn = random(0, 100);
  myStats.add(rn/100.0);

  Serial.print("  Count: ");
  Serial.print(myStats.count()); 

  Serial.print("  Average: ");
  Serial.print(myStats.average(), 4);

  Serial.print("  Std deviation: ");

  Serial.print(myStats.pop_stdev(), 4);
  Serial.println();

  if (myStats.count() == 300)
  {
   myStats.clear();
   delay(1000);
  }
}
