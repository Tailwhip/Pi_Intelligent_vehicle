#include <wiringPiSPI.h>

#include "velocity.h"

void velSetup() {
	if (wiringPiSPISetup(CHANNEL_0, 500000) < 0)
	{
		printf("Unable to open SPI device \n");
	}
}

float velGetVelocityX() {
	float result;
	unsigned char buffer[10];
	buffer[0] = 0xC0;
	buffer[1] = 0x10;
	buffer[2] = 0x2B;
	buffer[3] = 0xA0;
	buffer[4] = 0x20;
	buffer[5] = 0x1C;
	
	buffer[6] = 0x1F;
	buffer[7] = 0x1D;
	buffer[8] = 0xA4;
	buffer[9] = 0x80;
	buffer[10] = 0x84;
	
	wiringPiSPIDataRW(CHANNEL_0, buffer, 10);
	
	for (int i = 0; i < 10; i++)
		printf("Result: %d |", buffer[i]); 
	
	//sleep(1);
	result = buffer[0];
	return (float)result / MAX_VELOCITY;
}
