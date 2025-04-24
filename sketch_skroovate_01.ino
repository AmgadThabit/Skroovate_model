#define RED_LED 4
#define VIBRATION_MOTOR 2
#define TRACK_SENSOR 7

#include "Wire.h"       
#include "I2Cdev.h"     
#include "MPU6050.h"    

MPU6050 mpu;
int16_t ax, ay, az;
int16_t gx, gy, gz;

struct MyData {
  byte X;
  byte Y;
  byte Z;
};

MyData data;



void setup() {
  // put your setup code here, to run once:
  pinMode(VIBRATION_MOTOR,OUTPUT);// defining the motor as output
  pinMode(RED_LED, OUTPUT); // defining the led as output
  pinMode(TRACK_SENSOR, INPUT);// defining the track sesnor as input

  Serial.begin(9600);
  Wire.begin();
  mpu.initialize();
  //pinMode(LED_BUILTIN, OUTPUT);
}



void loop() {
  // put your main code here, to run repeatedly:
   int sval = digitalRead(TRACK_SENSOR);
  
      if (sval == HIGH) {
         digitalWrite(VIBRATION_MOTOR,HIGH); // start vibration 
         digitalWrite(RED_LED, HIGH);
         delay(100);
         digitalWrite(RED_LED, LOW);
         delay(100);
         

      } else {
         digitalWrite(VIBRATION_MOTOR,LOW); // turn off vibrtion 
         digitalWrite(RED_LED, LOW);
      
      }
   mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
   data.X = map(ax, -17000, 17000, 0, 255 ); // X axis data
   data.Y = map(ay, -17000, 17000, 0, 255); // Y axis data
   data.Z = map(az, -17000, 17000, 0, 255);  // Z axis data
   delay(500);
   Serial.print("Axis X = ");
   Serial.print(data.X);
   Serial.print("  ");
   Serial.print("Axis Y = ");
   Serial.print(data.Y);
   Serial.print("  ");
   Serial.print("Axis Z  = ");
   Serial.println(data.Z);
}


