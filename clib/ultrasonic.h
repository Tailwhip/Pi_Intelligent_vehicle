#ifndef ULTRASONIC_H
#define ULTRASONIC_H

#define TRIG_1		7
#define ECHO_1		0

#define TRIG_2		9 	// to be setted
#define ECHO_2		9	// to be setted

#define TRIG_3		1
#define ECHO_3		2

#define TRIG_4		9	// to be setted
#define ECHO_4		9	// to be setted

#define TRIG_5		3
#define ECHO_5		4

#define US_DELAY	0.01

extern int distanceOld;
extern int firstTimer;

void usSetup(void);

void usSensSetup(int trig, int echo);

float usGetDistance(int sensNum);

float usCountDistance(int trig, int echo);

#endif
