#include <wiringPiSPI.h>
#include <stdlib.h>
#include <wiringPiI2C.h>
#include <errno.h>
#include <unistd.h>
#include <asm/types.h>

#include "velocity.h"

int fd;
int time;

void velSetup() {
	fd = wiringPiI2CSetup(DEVICE);
	wiringPiI2CWriteReg8(fd, CTRL_REG1, 0xA7);							// 0b 1010 0111 - Turning on all axis with 100 Hz
	wiringPiI2CWriteReg8(fd, CTRL_REG4, 0x10); 							// 0b 0001 1000 - Turning on High res mode and +/- 4 g
	time = micros();
}

float velGetVelocityX() {
	__s32 result;
	float value;
	float normValue;
	float velocity;
		
	result = wiringPiI2CReadReg16(fd, OUTX_H);
	if(result < 0)
	{
	 printf("Error.  Errno is: %d \n", errno);
	}
	
	value = (__s16)result;
	normValue = value / MAX_ACC;
	
	velocity = velAccDerivative(normValue);
	
	return (float)velocity / MAX_VELOCITY;
}

float velAccDerivative(float acc){
	int delTime;
	
	delTime = micros() - time;
	time = micros();
	printf("DELTATIME: %i    | ", delTime);
	
	return acc * delTime;
}
