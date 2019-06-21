#include <stdio.h>
#include <stdlib.h>
#include <wiringPiI2C.h>
#include <errno.h>
#include <unistd.h>
#include <pigpio.h>
#include "intensity.h"

int fd_0, fd_1, fd_2, fd_3;

void intSetup() {
	gpioInitialise();
	//fd_0 = wiringPiI2CSetup(DEVICE_0);
	//fd_1 = wiringPiI2CSetup(DEVICE_1);
	//wiringPiI2CWrite(fd_0, CONTINUOUS_LOW_RES_MODE);
	//wiringPiI2CWrite(fd_1, CONTINUOUS_LOW_RES_MODE);
	fd_0 = i2cOpen(1, DEVICE_0, 0);
	fd_1 = i2cOpen(1, DEVICE_1, 0);
	//fd_2 = i2cOpen(0, DEVICE_0, 0);
	//fd_3 = i2cOpen(0, DEVICE_1, 0);
	i2cWriteByte(fd_0, CONTINUOUS_LOW_RES_MODE);
	i2cWriteByte(fd_1, CONTINUOUS_LOW_RES_MODE);
	//i2cWriteByte(fd_2, CONTINUOUS_LOW_RES_MODE);
	//i2cWriteByte(fd_3, CONTINUOUS_LOW_RES_MODE);
}

void intClose() {
	i2cClose(fd_0);
	i2cClose(fd_1);
	i2cClose(fd_2);
	i2cClose(fd_3);
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
			return intCountIntensity(fd_2);
		case 4:
		// Center-right sensor:
			return intCountIntensity(fd_3);
		default:
			return printf("Wrong number of intensity sensor!");
	}
}

float intCountIntensity12(int fd) {
	int result;
	float intensity;

	//wiringPiI2CWrite(fd, CONTINUOUS_LOW_RES_MODE);
	usleep(INT_DELAY);
	result = wiringPiI2CReadReg16(fd, 0x00);
	
	intensity = (float)result / MAX_INTENSITY;

	if(intensity == -1)
	{
		printf("Error.  Errno is: %d \n", errno);
	}

	return intensity;
}

float intCountIntensity(int fd) {
	int result;
	float intensity;

	//i2cWriteByte(fd, CONTINUOUS_LOW_RES_MODE);
	usleep(INT_DELAY);
	result = i2cReadByte(fd);
	
	intensity = (float)result / MAX_INTENSITY;

	if(intensity == -1)
	{
		printf("Error.  Errno is: %d \n", errno);
	}
	
	//intClose();
	
	return intensity;
}
