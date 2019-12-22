#include <stdlib.h>
#include <signal.h>
#include <pigpio.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

#include "servo.h"
#include "clamp.h"

void svSetup(void) {
	if (gpioInitialise() < 0) 
		printf("Servo problem - can't initialise! \n");
}

void svRide(float q0, float q1) {
	q0 = clamp(q0, -1, 1);
	q1 = clamp(q1, -1, 1);
	float multiplier0 = 250 * q0;
	float multiplier1 = 250 * q1;
	svSetup();
	gpioServo(RIGHT_WHEEL, MID_WIDTH + (int)multiplier0 - (int)multiplier1);
	gpioServo(LEFT_WHEEL, MID_WIDTH - (int)multiplier0 - (int)multiplier1);
	//time_sleep(0.4);
}


void svForward(float quality) {	
	quality = clamp(quality, -1, 1);
	float multiplier = 250 * quality;
	svSetup();
	gpioServo(RIGHT_WHEEL, MID_WIDTH + (int)multiplier);
	gpioServo(LEFT_WHEEL, MID_WIDTH - (int)multiplier);
	time_sleep(DRIVE_TIME);

}

void svTurn(float quality) {	
	quality = clamp(quality, -1, 1);
	float multiplier = 250 * quality;
	svSetup();
	gpioServo(RIGHT_WHEEL, MID_WIDTH - (int)multiplier);
	gpioServo(LEFT_WHEEL, MID_WIDTH - (int)multiplier);
	
	//time_sleep(TURN_TIME);

};

void svStop() {
	gpioServo(RIGHT_WHEEL, MID_WIDTH);
	gpioServo(LEFT_WHEEL, MID_WIDTH);
}
