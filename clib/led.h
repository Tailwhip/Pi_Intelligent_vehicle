#ifndef LED_H
#define LED_H

#define LED_DELAY	200000 // [us]
#define GREEN	28
#define RED		29

void ledSetup(void);
void ledPingGreen(void);
void ledPingRed(void);


#endif
