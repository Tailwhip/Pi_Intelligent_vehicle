#include <stdio.h>
#include <stdlib.h>
#include <wiringPiI2C.h>
#include <errno.h>
#include <unistd.h>

#include "intensity.h"

int fd_0, fd_1;

void intSetup(){
	fd_0 = wiringPiI2CSetup(DEVICE_0);
	fd_1 = wiringPiI2CSetup(DEVICE_1);	
}

float intGetIntensity(int sensNum) {
	switch (sensNum) {
		case 1:
		// Left sensor:
			return intCountIntensity(fd_0);
		case 2:
		// Center-left sensor:
			return intCountIntensity(fd_1);
		case 3:
		// Center sensor:
			return intCountIntensity(fd_0);
		case 4:
		// Center-right sensor:
			return intCountIntensity(fd_1);
		default:
			return printf("Wrong number of intensity sensor!");
	}
}

float intCountIntensity(int fd) {
	int result;
	float intensity;

	wiringPiI2CWrite(fd, CONTINUOUS_LOW_RES_MODE);
	usleep(INT_DELAY);
	result = wiringPiI2CReadReg16(fd, 0x00);
	
	intensity = (float)result / MAX_INTENSITY;

	if(intensity == -1)
	{
		printf("Error.  Errno is: %d \n", errno);
	}

	return intensity;
}
