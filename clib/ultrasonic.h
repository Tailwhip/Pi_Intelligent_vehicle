#ifndef ULTRASONIC_H
#define ULTRASONIC_H

#define TRIG_1 7
#define ECHO_1 0

#define TRIG_2 1
#define ECHO_2 2

#define TRIG_3 3
#define ECHO_3 4

extern int distanceOld;
extern int firstTimer;

void usSetup(void);

float usGetDistanceLeft(void);

float usGetDistanceCenter(void);

float usGetDistanceRight(void);

#endif
