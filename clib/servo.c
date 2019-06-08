#include <wiringPi.h>
#include <softPwm.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

#include "servo.h"
#include "clamp.c"

int distanceOld = 0;
int firstTimer = 1;

void usSetup(void) {

	if (wiringPiSetup () == -1)
	{
	fprintf (stdout, "Servo problem: %s\n", strerror (errno)) ;
	return 1 ;
	}
}

void svRide(void) {
	
}
