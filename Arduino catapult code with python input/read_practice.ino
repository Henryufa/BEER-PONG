#include <Servo.h>
#include <Stepper.h>


//servo initialization
int servoPin = 6;
float servoPos = 120;
Servo myServo;

//stepper initialization
int stepsPerRevolution = 2048;
int motSpeed=10;
int dt=500;
int stepperAngle = 1024;
Stepper myStepper(stepsPerRevolution,8,10,9,11);


String myCmd1;
String myCmd2 = "start";
String myCmd2p = myCmd2;

void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
myServo.attach(servoPin);
myStepper.setSpeed(motSpeed);
}

void loop() {
  // put your main code here, to run repeatedly:
while(Serial.available()==0){
}


myCmd1 = Serial.readStringUntil('\r');
myCmd2 = Serial.readStringUntil('\r');
stepperAngle = myCmd2.toInt();
servoPos = myCmd1.toInt();

if(myCmd2 != myCmd2p){
  myStepper.step(stepperAngle);
  delay(dt);
  myServo.write(servoPos);
  delay(dt);
  myServo.write(0);
  myStepper.step(-stepperAngle);
  delay(dt);
}
delay(dt);




}
