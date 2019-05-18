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

float intGetIntensFrontLeft(){
	int result;
	float intensity;

	wiringPiI2CWrite(fd_0, CONTINUOUS_LOW_RES_MODE);
	usleep(INT_DELAY);
	result = wiringPiI2CReadReg16(fd_0, 0x00);
	//result = ((result & 0xff00)>>8) | ((result & 0x00ff)<<8);
	intensity = (float)result / MAX_INTENSITY;

	if(intensity == -1)
	{
	 printf("Error.  Errno is: %d \n", errno);
	}

	return intensity;
}

float intGetIntensFrontRight(){
	int result;
	float intensity;

	wiringPiI2CWrite(fd_1, CONTINUOUS_LOW_RES_MODE);
	usleep(INT_DELAY);
	result = wiringPiI2CReadReg16(fd_1, 0x00);
	//result = ((result & 0xff00)>>8) | ((result & 0x00ff)<<8);
	intensity = (float)result / MAX_INTENSITY;

	if(intensity == -1)
	{
	 printf("Error.  Errno is: %d \n", errno);
	}

	return intensity;
}
