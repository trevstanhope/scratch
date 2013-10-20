// Blink

#define LED1 13
#define LED2 12

void setup()
{
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
}

void loop()
{
  digitalWrite(LED1, HIGH);
  delay(1000);
  digitalWrite(LED2, HIGH);
  digitalWrite(LED1, LOW);
  delay(500);
  digitalWrite(LED2, LOW);
  delay(500);
}
