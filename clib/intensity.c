#include <stdio.h>
#include <stdlib.h>
#include <wiringPiI2C.h>
#include <errno.h>
#include <unistd.h>
#include <pigpio.h>
#include <math.h>
#include "intensity.h"

int fd_1, fd_2, fd_3, fd_4;

void intSetup() {
	if (gpioInitialise() < 0) 
		printf("Light sensor problem - can't initialise! \n");
	fd_1 = i2cOpen(1, DEVICE_0, 0);
	fd_2 = i2cOpen(1, DEVICE_1, 0);
	fd_3 = i2cOpen(0, DEVICE_0, 0);
	fd_4 = i2cOpen(0, DEVICE_1, 0);
}

void intClose() {
	i2cClose(fd_1);
	i2cClose(fd_2);
	i2cClose(fd_3);
	i2cClose(fd_4);
}

float intGetIntensity(int sensNum) {
	switch (sensNum) {
		case 1:
		// Left sensor:
			return intCountIntensity(fd_1);
		case 2:
		// Center-left sensor:
			return intCountIntensity(fd_2);
		case 3:
		// Center sensor:
			return intCountIntensity(fd_3);
		case 4:
		// Center-right sensor:
			return intCountIntensity(fd_4);
		default:
			return printf("Wrong number of intensity sensor!");
	}
}

float intCountIntensity(int fd) {
	
	char result[2];
    uint16_t raw_lux=0;
    
    i2cWriteByte(fd, CONTINUOUS_HIGH_RES_MODE_1);
    time_sleep(CONTINUOUS_HIGH_RES_1_DELAY_S);
    i2cReadDevice(fd, result, 2);
	
	raw_lux |= result[0];
    raw_lux <<= 8;
    raw_lux |= result[1];

	
	float value = (float) raw_lux;
	float intensity;
	
	intensity = value / MAX_INTENSITY;

	if(intensity == -1) {
		printf("Error.  Errno is: %d \n", errno);
	}
	
	return intensity;
}
