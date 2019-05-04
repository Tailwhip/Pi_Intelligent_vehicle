#ifndef ULTRASONIC_H_
#define ULTRASONIC_H_

#define TRIG_1 7
#define ECHO_1 0

#define TRIG_2 1
#define ECHO_2 2

#define TRIG_3 3
#define ECHO_3 4

int distanceOld = 0;
int firstTimer = 1;

void Setup();

float GetDistanceLeft();

float GetDistanceCenter();

float GetDistanceRight();

#endif
