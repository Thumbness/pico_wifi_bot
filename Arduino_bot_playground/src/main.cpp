#include <Arduino.h>

#define LED 2

unsigned int led_state = LOW;

void setup()
{
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
}

void loop()
{
  if (Serial.available() > 0)
  {
    char foo = Serial.read();
    if (foo == 'A')
    {
      led_state = HIGH;
    }
    else
    {
      led_state = LOW;
    }
  }
  digitalWrite(LED, led_state);
}