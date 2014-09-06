/*
 * @author : skygr
 * @description : arduino RubikCube 
 */

#include <SoftwareSerial.h>
#include <Servo.h>

/*
 * @about : Protocol Define
 */
#define Ctrl_Hand_Left_Open '1'
#define Ctrl_Hand_Left_Close '2'
#define Ctrl_Hand_Left_Vertical '3'
#define Ctrl_Hand_Left_Aclinic '4'
#define Ctrl_Hand_Right_Open 'A'
#define Ctrl_Hand_Right_Close 'B'
#define Ctrl_Hand_Right_Vertical 'C'
#define Ctrl_Hand_Right_Aclinic 'D'

/*
 * @about : Hand
 */
Servo handLeftCatch;
Servo handRightCatch;
Servo handLeftRotate;
Servo handRightRotate;
void handInit() {
  handLeftCatch.attach(8);
  handRightCatch.attach(9);
  handLeftRotate.attach(10);
  handRightRotate.attach(11);
}
void handLeftOpen() {
  handLeftCatch.write(0);
}
void handLeftClose() {
  handLeftCatch.write(180);
}
void handLeftVertical() {
  handLeftRotate.write(36);
}
void handLeftAclinic() {
  handLeftRotate.write(121);
}
void handRightOpen() {
  handRightCatch.write(0);
}
void handRightClose() {
  handRightCatch.write(180);
}
void handRightVertical() {
  handRightRotate.write(91);
}
void handRightAclinic() {
  handRightRotate.write(1);
}

/*
 * @about : main
 */
void setup()
{
  Serial.begin(38400);
  handInit();
  handLeftOpen();
  handRightOpen();
  handLeftAclinic();
  handRightAclinic();
}

void loop()
{
  if(Serial.available()) {
    switch(Serial.read()) {
      case Ctrl_Hand_Left_Open:
        handLeftOpen();
        break;
      case Ctrl_Hand_Left_Close:
        handLeftClose();
        break;
      case Ctrl_Hand_Left_Vertical:
        handLeftVertical();
        break;
      case Ctrl_Hand_Left_Aclinic:
        handLeftAclinic();
        break;
      case Ctrl_Hand_Right_Open:
        handRightOpen();
        break;
      case Ctrl_Hand_Right_Close:
        handRightClose();
        break;
      case Ctrl_Hand_Right_Vertical:
        handRightVertical();
        break;
      case Ctrl_Hand_Right_Aclinic:
        handRightAclinic();
        break;
    }
  }
}

