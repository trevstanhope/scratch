int receiverPin = 13; // red
int ledPin = 12; // yellow

unsigned long duration; // time shutter is open

void setup()
{
  pinMode(receiverPin, INPUT);
  Serial.begin(9600);
}

void loop()
{
  digitalWrite(ledPin, HIGH);
  duration = pulseIn(receiverPin, LOW);
  if(duration != 0 )
  {
    Serial.println(duration);
  }
}
