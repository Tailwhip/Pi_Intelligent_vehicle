#ifndef INTENSITY_H
#define INTENSITY_H

//Define some constants from the datasheet
#define DEVICE_0				    0x23 // Default device I2C address 
										 //	with ADDR non set
#define DEVICE_1				    0x5c // Default device I2C address 
										 //	with ADDR set
#define POWER_DOWN					0x00 // No active state
#define POWER_ON				    0x01 // Power on
#define RESET       				0x07 // Reset data register value

// Start measurement at 4 lx resolution. Time typically 16 ms.
#define CONTINUOUS_LOW_RES_MODE    	0x13
// Start measurement at 1 lx resolution. Time typically 120 ms
#define CONTINUOUS_HIGH_RES_MODE_1 	0x10
// Start measurement at 0.5 lx resolution. Time typically 120 ms
#define CONTINUOUS_HIGH_RES_MODE_2 	0x11
// Start measurement at 1 lx resolution. Time typically 120 ms
// Device is automatically set to Power Down after measurement.
#define ONE_TIME_HIGH_RES_MODE_1   	0x20
// Start measurement at 0.5 lx resolution. Time typically 120 ms
// Device is automatically set to Power Down after measurement.
#define ONE_TIME_HIGH_RES_MODE_2   	0x21
// Start measurement at 1 lx resolution. Time typically 120 ms
// Device is automatically set to Power Down after measurement.
#define ONE_TIME_LOW_RES_MODE      	0x23
// Maximum intensity value:
#define MAX_INTENSITY              	255 //65535 // 65280 // 63237
#define INT_DELAY					2000//200000 //16000 // 25000 // [us]


void intSetup(void);

void intClose(void);

float intGetIntensity(int sensNum);

float intCountIntensity(int fd, int device);

#endif
