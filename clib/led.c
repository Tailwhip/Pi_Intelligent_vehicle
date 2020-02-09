#include "led.h"


void ledSetup() {
	wiringPiSetup();
	pinMode(GREEN, OUTPUT);
	pinMode(RED, OUTPUT);
}

void ledPingGreen() {
	digitalWrite(GREEN, HIGH);
    delay(LED_DELAY);
    printf("PING GREEN \n");
    digitalWrite(GREEN, LOW);
    delay(LED_DELAY);
}

void ledPingRed() {
	digitalWrite(RED, HIGH);
    delay(LED_DELAY);
    printf("PING RED \n");
    digitalWrite(RED, LOW);
    delay(LED_DELAY);
}

