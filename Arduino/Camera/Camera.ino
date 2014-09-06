#include <SoftwareSerial.h>

#include "JPEGCamera.h"

SoftwareSerial s(5, 6);
JPEGCamera cam(s);
char resp[10];

void setup()
{
  Serial.begin(38400);
  s.begin(38400);  
  delay(25);
  cam.reset();
  delay(4000);
  cam.chBaudRate(1);
  delay(50);
  s.end();
  s.begin(19200);
  delay(50);
}

void loop()
{
  while (!Serial.available());
  while (Serial.available())Serial.read();

  cam.takePicture();
  delay(25);
  cam.readData(Serial);
  delay(100);
  cam.stopPictures();
}
