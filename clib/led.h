#include <wiringPi.h>
#include <stdio.h>

#ifndef _LED_H
#define _LED_H

#define LED_DELAY	500 // [us]
#define GREEN	28
#define RED		29

void ledSetup(void);
void ledPingGreen(void);
void ledPingRed(void);


#endif
