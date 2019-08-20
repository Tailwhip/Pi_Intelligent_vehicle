#include <wiringPiSPI.h>
#include <stdlib.h>
#include <wiringPiI2C.h>
#include <errno.h>
#include <unistd.h>
#include <asm/types.h>
#include <stdio.h>
#include <wiringPi.h>

#include "acceleration.h"

int fd;
int oldTime;
float velocityOld;

void accSetup() {
	fd = wiringPiI2CSetup(DEVICE);
	wiringPiI2CWriteReg8(fd, CTRL_REG1, 0xA3);							// 0b 1010 0111 - Turning on all axis with 100 Hz
	wiringPiI2CWriteReg8(fd, CTRL_REG2, 0x09);
	wiringPiI2CWriteReg8(fd, CTRL_REG4, 0x08); 							// 0b 0001 1000 - Turning on High res mode and +/- 4 g
	oldTime = micros();
	velocityOld = 0;
}

float accGetAccX() {
	__s32 result;
	float acc;
	float normAcc;
	usleep(2000);
	result = wiringPiI2CReadReg16(fd, OUTX_H) & wiringPiI2CReadReg16(fd, OUTX_L);
	if(result < 0) {
		printf("Error.  Errno is: %d \n", errno);
	}
	
	acc = (__s16)result;
	normAcc = acc / MAX_ACC;

	return normAcc;
}

float accGetAccY() {
	__s32 result;
	float acc;
	float normAcc;
	usleep(2000);
	result = wiringPiI2CReadReg16(fd, OUTY_H) & wiringPiI2CReadReg16(fd, OUTY_L);
	if(result < 0)
	{
		printf("Error.  Errno is: %d \n", errno);
	}
	
	acc = (__s16)result;
	normAcc = acc / MAX_ACC;

	return normAcc;
}

float accAccDerivative(float acc) {
	int delTime;
	
	delTime = micros() - oldTime;
	oldTime = micros();
	printf("DELTATIME: %i    | ", delTime);
	
	return acc * delTime;
}
