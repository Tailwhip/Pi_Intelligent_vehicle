#include <stdio.h>
#include <stdlib.h>
#include <wiringPiI2C.h>
#include <errno.h>
#include <unistd.h>

#include "intensity.h"

void intSetup(){
	wiringPiI2CSetup(DEVICE);
}

float intGetIntensFrontLeft(){
	int fd, result;
	float intensity;

	fd = wiringPiI2CSetup(DEVICE_0);

	wiringPiI2CWrite(fd, 0x11);
	usleep(10000);
	result = wiringPiI2CReadReg16(fd, 0x00);
	result = ((result & 0xff00)>>8) | ((result & 0x00ff)<<8);
	intensity = (float)result / MAX_INTENSITY;

	if(intensity == -1)
	{
	 printf("Error.  Errno is: %d \n", errno);
	}

	return intensity;
}

/*
int main(void) {
	int fd, result;
	float intensity;
	int i = 0;
	fd = wiringPiI2CSetup(DEVICE);

	while (i == 0) {
	  wiringPiI2CWrite(fd, 0x11);
	  usleep(10000);
	  result = wiringPiI2CReadReg16(fd, 0x00);
	  result = ((result & 0xff00)>>8) | ((result & 0x00ff)<<8);
	  intensity = (float)result / MAX_INTENSITY;
	  printf("%f \n", intensity);

	  if(intensity == -1)
	  {
		 printf("Error.  Errno is: %d \n", errno);
	  }
	}
	return 0;
}
*/
