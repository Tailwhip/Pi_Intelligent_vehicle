#include <wiringPi.h>
#include <stdio.h>
#include "led.h"


void ledSetup() {
	wiringPiSetup();
	pinMode(GREEN, OUTPUT);
	pinMode(RED, OUTPUT);
}

void ledPingGreen() {
	digitalWrite(GREEN, HIGH);
	delayMicroseconds(LED_DELAY);
	digitalWrite(GREEN, LOW);
}

void ledPingRed() {
	digitalWrite(RED, HIGH);
	delayMicroseconds(LED_DELAY);
	digitalWrite(RED, LOW);
}

