#include <stdio.h>
#include <stdlib.h>
#include <wiringPiI2C.h>
#include <errno.h>
#include <unistd.h>

//Define some constants from the datasheet
#define DEVICE 0x23 // Default device I2C address
#define POWER_DOWN 0x00 //No active state
#define POWER_ON 0x01 // Power on
#define RESET 0x07 // Reset data register value

// Start measurement at 4lx resolution. Time typically 16ms.
#define CONTINUOUS_LOW_RES_MODE 0x13
// Start measurement at 1lx resolution. Time typically 120ms
#define CONTINUOUS_HIGH_RES_MODE_1 0x10
// Start measurement at 0.5lx resolution. Time typically 120ms
#define CONTINUOUS_HIGH_RES_MODE_2 0x11
// Start measurement at 1lx resolution. Time typically 120ms
// Device is automatically set to Power Down after measurement.
#define ONE_TIME_HIGH_RES_MODE_1 0x20
// Start measurement at 0.5lx resolution. Time typically 120ms
// Device is automatically set to Power Down after measurement.
#define ONE_TIME_HIGH_RES_MODE_2 0x21
// Start measurement at 1lx resolution. Time typically 120ms
// Device is automatically set to Power Down after measurement.
#define ONE_TIME_LOW_RES_MODE 0x23
// Maximum intensity value:
#define MAX_INTENSITY 63237

void setup(){
	wiringPiI2CSetup(DEVICE);
}

float getIntensity_1(){
	int fd_1, result;
	float intensity;

	fd_1 = wiringPiI2CSetup(DEVICE);;

	wiringPiI2CWrite(fd_1, 0x11);
	usleep(10000);
	result = wiringPiI2CReadReg16(fd_1, 0x00);
	result = ((result & 0xff00)>>8) | ((result & 0x00ff)<<8);
	intensity = (float)result / MAX_INTENSITY;

	if(intensity == -1)
	{
	 printf("Error.  Errno is: %d \n", errno);
	}

	return intensity;
}

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



