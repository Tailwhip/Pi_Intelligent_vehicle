#ifndef ACCELERATION_H
#define ACCELERATION_H

#define DEVICE			0x19

#define CTRL_REG1		0x20
#define CTRL_REG2		0x21
#define CTRL_REG3		0x22
#define CTRL_REG4		0x23
#define CTRL_REG5		0x24
#define CTRL_REG6		0x25
#define REFERENCE		0x26
#define INT1_THS		0x32
#define INT1_DUR		0x33
#define INT1_CFG		0x30

#define STATUS_REG		0x27
#define OUTX_L			0x28
#define OUTX_H			0x29
#define OUTY_L			0x2A
#define OUTY_H			0x2B
#define OUTZ_L			0x2C
#define OUTZ_H			0x2D

#define DELAY			2000
#define MAX_ACC 		10//65535//65280

void accSetup(void);

float accGetAccX(void);

float accGetAccY(void);

float accGetAccZ(void);

float accAccDerivative(float acc);

#endif
