#include <stdlib.h>
#include <signal.h>
#include <pigpio.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

#include "servo.h"
#include "clamp.c"

void svSetup(void) {
	if (gpioInitialise() < 0) 
	printf("Servo problem");
}

void svRide(float quality) {
	quality = clamp(quality, -1, 1);
	float multiplier = 500 * quality;
	svSetup();
	printf("Ride %f \n", quality);
	gpioServo(RIGHT_WHEEL, MID_WIDTH + (int)multiplier);
	gpioServo(LEFT_WHEEL, MID_WIDTH - (int)multiplier);
	time_sleep(0.2);
	gpioTerminate();
}

void svTurn(float quality) {
	printf("Turn %f \n", quality);
	quality = clamp(quality, -1, 1);
	float multiplier = 500 * quality;
	svSetup();
	gpioServo(RIGHT_WHEEL, MID_WIDTH + (int)multiplier);
	gpioServo(LEFT_WHEEL, MID_WIDTH + (int)multiplier);
	time_sleep(0.2);
	gpioTerminate();
};
