#include "acceleration.h"

int fd;
int oldTime;
float velocityOld;

void accSetup() {
	fd = wiringPiI2CSetup(DEVICE);
	//fd = i2cOpen(1, DEVICE, 0);
	wiringPiI2CWriteReg8(fd, CTRL_REG1, 0x57);		//0xA3				// 0b 1010 0111 - Turning on all axis with 100 Hz
	wiringPiI2CWriteReg8(fd, CTRL_REG2, 0x80);		//09
	wiringPiI2CWriteReg8(fd, CTRL_REG4, 0x10); 		//08				// 0b 0001 1000 - Turning on High res mode and +/- 4 g
	oldTime = micros();
	velocityOld = 0;
}

float accGetAccX() {
	int16_t out_x_h = wiringPiI2CReadReg8(fd, OUTX_H);
	int16_t out_x_l = wiringPiI2CReadReg8(fd, OUTX_L);
	
	int16_t x = out_x_h;
	x <<= 8;
	x |= out_x_l;
	x >>= 6;
	
	usleep(DELAY);
	
	float normAcc = 0;
	
	x = accAccDerivative(x);
	
	if (x > 30) normAcc = 1;
	else if (x < -30) normAcc = 0;
	else normAcc = 0.5;

	return normAcc;
}

float accGetAccY() {
	int out_y_h = wiringPiI2CReadReg8(fd, OUTY_H);
	int out_y_l = wiringPiI2CReadReg8(fd, OUTY_L);
	
	int16_t y = out_y_h;
	y <<= 8;
	y |= out_y_l;
	y >>= 6;
	
	usleep(DELAY);
	
	float normAcc = 0;
	
	y = accAccDerivative(y);
	
	if (y > 30) normAcc = 1;
	else if (y < -30) normAcc = 0;
	else normAcc = 0.5;

	return normAcc;
}

float accGetAccZ() {	
	int16_t out_z_h = wiringPiI2CReadReg8(fd, OUTZ_H);
	int16_t out_z_l = wiringPiI2CReadReg8(fd, OUTZ_L);
	
	int16_t z = out_z_h;
	z <<= 8;
	z |= out_z_l;
	z >>= 6;

	usleep(DELAY);

	return (float)z;
}

float accAccDerivative(float acc) {
	int delTime;
	
	delTime = micros() - oldTime;
	oldTime = micros();
	//printf("DELTATIME: %i    | ", delTime);
	
	return acc * delTime;
}
