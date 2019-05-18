#include <wiringPiSPI.h>
#include <stdlib.h>
#include <wiringPiI2C.h>
#include <errno.h>
#include <unistd.h>

#include "velocity.h"

int fd;

void velSetup() {
	//wiringPiSetup();
	fd = wiringPiI2CSetup(DEVICE);
	/*
	wiringPiI2CWriteReg8(fd, CTRL_REG1, 0xA7);
	wiringPiI2CWriteReg8(fd, CTRL_REG2, 0x00);
	wiringPiI2CWriteReg8(fd, CTRL_REG3, 0x00);
	wiringPiI2CWriteReg8(fd, CTRL_REG4, 0x00);
	wiringPiI2CWriteReg8(fd, CTRL_REG5, 0x00);
	wiringPiI2CWriteReg8(fd, CTRL_REG6, 0x00);
	wiringPiI2CWriteReg8(fd, REFERENCE, 0x00);
	wiringPiI2CWriteReg8(fd, INT1_THS, 0x00);
	wiringPiI2CWriteReg8(fd, INT1_DUR, 0x00);
	wiringPiI2CWriteReg8(fd, INT1_CFG, 0x00);
	wiringPiI2CWriteReg8(fd, CTRL_REG5, 0x00);
	*/
}

float velGetVelocityX() {
	int result;
	float velocity;
	/*
	wiringPiI2CWriteReg8(fd, CTRL_REG1, 0xA7);
	wiringPiI2CWriteReg8(fd, CTRL_REG2, 0x00);
	wiringPiI2CWriteReg8(fd, CTRL_REG3, 0x00);
	wiringPiI2CWriteReg8(fd, CTRL_REG4, 0x00);
	wiringPiI2CWriteReg8(fd, CTRL_REG5, 0x00);
	wiringPiI2CWriteReg8(fd, CTRL_REG6, 0x00);
	wiringPiI2CWriteReg8(fd, REFERENCE, 0x00);
	wiringPiI2CWriteReg8(fd, INT1_THS, 0x00);
	wiringPiI2CWriteReg8(fd, INT1_DUR, 0x00);
	wiringPiI2CWriteReg8(fd, INT1_CFG, 0x00);
	wiringPiI2CWriteReg8(fd, CTRL_REG5, 0x00);
	*/
	//printf("status: %d | ", wiringPiI2CReadReg8(fd, STATUS_REG));
	
	//usleep(2000);
	
	//printf("OUTX: %d | ", (wiringPiI2CReadReg16(fd, OUTX_H) & wiringPiI2CReadReg16(fd, OUTX_L)));
	//printf("OUTY: %d | ", (wiringPiI2CReadReg16(fd, OUTY_H) & wiringPiI2CReadReg16(fd, OUTY_L)));
	
	result = wiringPiI2CReadReg16(fd, OUTX_H);
	//result = ((result & 0xff00)>>8) | ((result & 0x00ff)<<8);
	velocity = (float)result / MAX_VELOCITY;

	if(velocity == -1)
	{
	 printf("Error.  Errno is: %d \n", errno);
	}

	return velocity;
}
