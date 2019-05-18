#include <wiringPi.h>

#include "ultrasonic.h"
#include "clamp.c"

int distanceOld = 0;
int firstTimer = 1;

void usSetup(void) {
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

float usGetDistanceLeft(void) {
	long travelTime = 0;
	long startTime = 0;
	float distance = 0;
	
	while (travelTime == 0) {
		int TIMER = 2;
		//Send trig pulse
		digitalWrite(TRIG_1, HIGH);
		delayMicroseconds(US_DELAY);
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

float usGetDistanceCenter(void) {
	long travelTime = 0;
	long startTime = 0;
	float distance = 0;
	
	while (travelTime == 0) {
		int TIMER = 2;
		//Send trig pulse
		digitalWrite(TRIG_2, HIGH);
		delayMicroseconds(US_DELAY);
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

float usGetDistanceRight(void) {
	long travelTime = 0;
	long startTime = 0;
	float distance = 0;
	
	while (travelTime == 0) {
		int TIMER = 2;
		//Send trig pulse
		digitalWrite(TRIG_3, HIGH);
		delayMicroseconds(US_DELAY);
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
