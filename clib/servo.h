#include <stdlib.h>
#include <signal.h>
#include <pigpio.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

#include "clamp.h"

#ifndef _SERVO_H
#define _SERVO_H

#define RIGHT_WHEEL				26//16 	// F: Clockwise B: CounterClockwise
									// TR: CounterClockwise TL: Clockwise
#define LEFT_WHEEL				16//26

#define CNTR_CLOCKWISE_WIDTH 	1000
#define MID_WIDTH 				1500
#define CLOCKWISE_WIDTH 		2000

#define DRIVE_TIME		 		0.10
#define TURN_TIME		 		0.15

void svSetup(void);

void svRide(float q0, float q1);

void svForward(float quality);

void svTurn(float quality);

void svStop(void);

#endif
