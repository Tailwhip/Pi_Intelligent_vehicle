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

void svRide(float quality) {
	//printf("Ride %f \n", quality);
	
	quality = clamp(quality, -1, 1);
	float multiplier = 500 * quality;
	svSetup();
	gpioServo(RIGHT_WHEEL, MID_WIDTH + (int)multiplier);
	gpioServo(LEFT_WHEEL, MID_WIDTH - (int)multiplier);
	
	time_sleep(DRIVE_TIME);
	
	gpioServo(RIGHT_WHEEL, MID_WIDTH);
	gpioServo(LEFT_WHEEL, MID_WIDTH);
}

void svTurn(float quality) {
	//printf("Turn %f \n", quality);
	
	quality = clamp(quality, -1, 1);
	float multiplier = 500 * quality;
	svSetup();
	gpioServo(RIGHT_WHEEL, MID_WIDTH - (int)multiplier);
	gpioServo(LEFT_WHEEL, MID_WIDTH - (int)multiplier);
	
	time_sleep(TURN_TIME);
	
	gpioServo(RIGHT_WHEEL, MID_WIDTH);
	gpioServo(LEFT_WHEEL, MID_WIDTH);
};
