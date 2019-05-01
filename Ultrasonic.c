#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
 
#define TRIG_1 7
#define ECHO_1 0

#define TRIG_2 1
#define ECHO_2 2

#define TRIG_3 3
#define ECHO_3 4

int distanceOld = 0;
int firstTimer = 1;

double clamp(float d, float min, float max) {
  const float t = d < min ? min : d;
  return t > max ? max : t;
}

void setup() {
        // distance memory:   
        wiringPiSetup();
        pinMode(TRIG_1, OUTPUT);
        pinMode(ECHO_1, INPUT);
 
        //TRIG pin must start LOW
        digitalWrite(TRIG_1, LOW);
        
        pinMode(TRIG_2, OUTPUT);
        pinMode(ECHO_2, INPUT);
 
        //TRIG pin must start LOW
        digitalWrite(TRIG_2, LOW);
        
        pinMode(TRIG_3, OUTPUT);
        pinMode(ECHO_3, INPUT);
 
        //TRIG pin must start LOW
        digitalWrite(TRIG_3, LOW);
        
        delay(30);
}

float GetDistanceLeft() {
        long travelTime = 0;
        long startTime = 0;
        float distance = 0;
        
        while (travelTime == 0) {
                int TIMER = 10;
                //Send trig pulse
                digitalWrite(TRIG_1, HIGH);
                delayMicroseconds(0.1);
                digitalWrite(TRIG_1, LOW);
         
                //Wait for echo start
                while(digitalRead(ECHO_1) == LOW) {
                        //Wait for echo end
                        startTime = micros();
                        TIMER--;
                        if (TIMER == 0)
                                break;
                }
                
                if (TIMER == 0)
                        continue;
                
                while(digitalRead(ECHO_1) == HIGH)
                        travelTime = micros() - startTime;
                                
                //Get distance in cm
                distance = (float)travelTime / 58;

                if (((distanceOld - distance) * (distanceOld - distance) > 50) 
                && firstTimer == 0)
                        continue;
                else if (firstTimer == 1)
                        firstTimer = 0;

                distanceOld = distance;
        }
        distance = clamp(distance, 0.0, 50.0);
        distance = (distance / 50.0);

        return distance;
}

float GetDistanceCenter() {
        long travelTime = 0;
        long startTime = 0;
        float distance = 0;
        
        while (travelTime == 0) {
                int TIMER = 10;
                //Send trig pulse
                digitalWrite(TRIG_2, HIGH);
                delayMicroseconds(0.1);
                digitalWrite(TRIG_2, LOW);
         
                //Wait for echo start
                while(digitalRead(ECHO_2) == LOW) {
                        //Wait for echo end
                        startTime = micros();
                        TIMER--;
                        if (TIMER == 0)
                                break;
                }
                
                if (TIMER == 0)
                        continue;
                
                while(digitalRead(ECHO_2) == HIGH)
                        travelTime = micros() - startTime;
                                
                //Get distance in cm
                distance = (float)travelTime / 58;

                if (((distanceOld - distance) * (distanceOld - distance) > 50) 
                && firstTimer == 0)
                        continue;
                else if (firstTimer == 1)
                        firstTimer = 0;

                distanceOld = distance;
        }
        distance = clamp(distance, 0.0, 50.0);
        distance = (distance / 50.0);

        return distance;
}

float GetDistanceRight() {
        long travelTime = 0;
        long startTime = 0;
        float distance = 0;
        
        while (travelTime == 0) {
                int TIMER = 10;
                //Send trig pulse
                digitalWrite(TRIG_3, HIGH);
                delayMicroseconds(0.1);
                digitalWrite(TRIG_3, LOW);
         
                //Wait for echo start
                while(digitalRead(ECHO_3) == LOW) {
                        //Wait for echo end
                        startTime = micros();
                        TIMER--;
                        if (TIMER == 0)
                                break;
                }
                
                if (TIMER == 0)
                        continue;
                
                while(digitalRead(ECHO_3) == HIGH)
                        travelTime = micros() - startTime;
                                
                //Get distance in cm
                distance = (float)travelTime / 58;

                if (((distanceOld - distance) * (distanceOld - distance) > 50) 
                && firstTimer == 0)
                        continue;
                else if (firstTimer == 1)
                        firstTimer = 0;

                distanceOld = distance;
        }
        distance = clamp(distance, 0.0, 50.0);
        distance = (distance / 50.0);

        return distance;
}

float getDistance(int TRIG, int ECHO) {
        long travelTime = 0;
        long startTime = 0;
        float distance = 0;
        
        while (travelTime == 0) {
                int TIMER = 10;
                //Send trig pulse
                digitalWrite(TRIG, HIGH);
                delayMicroseconds(0.1);
                digitalWrite(TRIG, LOW);
         
                //Wait for echo start
                while(digitalRead(ECHO) == LOW) {
                        //Wait for echo end
                        startTime = micros();
                        TIMER--;
                        if (TIMER == 0)
                                break;
                }
                
                if (TIMER == 0)
                        continue;
                
                while(digitalRead(ECHO) == HIGH)
                        travelTime = micros() - startTime;
                                
                //Get distance in cm
                distance = (float)travelTime / 58;

                if (((distanceOld - distance) * (distanceOld - distance) > 50) 
                && firstTimer == 0)
                        continue;
                else if (firstTimer == 1)
                        firstTimer = 0;

                distanceOld = distance;
        }
        distance = clamp(distance, 0.0, 50.0);
        //printf("%f \n", distance);
        
        distance = (distance / 50.0);

        return distance;
}

int main(void) {
        setup();
        int i = 0;
        while (i == 0) {
                printf("Distance: %f %f %f\n", getDistance(TRIG_1, ECHO_1), 
                getDistance(TRIG_2, ECHO_2), getDistance(TRIG_3, ECHO_3));
        };
        return 0;
}
