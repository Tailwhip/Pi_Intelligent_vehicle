#include <wiringPi.h>
#include <stdio.h>
#include <math.h>

#include "clamp.h"

#ifndef _ULTRASONIC_H
#define _ULTRASONIC_H

#define TRIG_1		21//7
#define ECHO_1		15

#define TRIG_2		16
#define ECHO_2		0

#define TRIG_3		1
#define ECHO_3		2

#define TRIG_4		3
#define ECHO_4		4

#define TRIG_5		5
#define ECHO_5		12

#define US_DELAY	10 // 0.01
#define MAX_DIST	15 


extern int distanceOld;
extern int firstTimer;

void usSetup(void);

void usSensSetup(int trig, int echo);

float usGetDistance(int sensNum);

float usCountDistance(int trig, int echo);

void shoot(int _trig);

#endif
