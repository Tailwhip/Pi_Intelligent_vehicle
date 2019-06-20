#ifndef SERVO_H
#define SERVO_H

#define RIGHT_WHEEL				16 	// F: Clockwise B: CounterClockwise
									// TR: CounterClockwise TL: Clockwise
#define LEFT_WHEEL				26

#define CNTR_CLOCKWISE_WIDTH 	1000
#define MID_WIDTH 				1500
#define CLOCKWISE_WIDTH 		2000

void svSetup(void);

void svRide(float quality);

void svTurn(float quality);

#endif
