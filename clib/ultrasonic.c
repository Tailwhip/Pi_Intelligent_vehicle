#include <wiringPi.h>
#include <stdio.h>

#include "ultrasonic.h"
#include "clamp.h"

int distanceOld = 0;
int firstTimer = 1;

void usSetup(void) {
	// distance memory:   
	wiringPiSetup();
	
	usSensSetup(TRIG_1, ECHO_1);
	//usSensSetup(TRIG_2, ECHO_2);
	usSensSetup(TRIG_3, ECHO_3);
	//usSensSetup(TRIG_4, ECHO_4);
	usSensSetup(TRIG_5, ECHO_5);
	
	delay(30);
}

void usSensSetup(int trig, int echo){
	pinMode(trig, OUTPUT);
	pinMode(echo, INPUT);

	//TRIG pin must start LOW
	digitalWrite(trig, LOW);
}

float usGetDistance(int sensNum) {
	switch (sensNum) {
		case 1:
		// Left sensor:
			return usCountDistance(TRIG_1, ECHO_1);
		case 2:
		// Center-left sensor:
			return usCountDistance(TRIG_2, ECHO_2);
		case 3:
		// Center sensor:
			return usCountDistance(TRIG_3, ECHO_3);
		case 4:
		// Center-right sensor:
			return usCountDistance(TRIG_4, ECHO_4);
		case 5:
		// Right sensor:
			return usCountDistance(TRIG_5, ECHO_5);
		default:
			return printf("Wrong number of ultrasonic sensor!");
	}
}

float usCountDistance(int trig, int echo) {
	long travelTime = 0;
	long startTime = 0;
	float distance = 0;
	
	while (travelTime == 0) {
		int TIMER = 2;
		//Send trig pulse
		digitalWrite(trig, HIGH);
		delayMicroseconds(US_DELAY);
		digitalWrite(trig, LOW);
 
		//Wait for echo start
		while(digitalRead(echo) == LOW) {
			//Wait for echo end
			startTime = micros();
			//delayMicroseconds(100);
			TIMER--;
			if (TIMER == 0)
				break;
		}
		
		if (digitalRead(echo) == LOW)
			//return 1;
			continue;
	
		while(digitalRead(echo) == HIGH)
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
