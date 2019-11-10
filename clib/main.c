#include <stdio.h>
#include <stdlib.h>
#include <pigpio.h>
#include "ultrasonic.h"
#include "intensity.h"
#include "acceleration.h"
#include "servo.h"
#include "led.h"

#include <wiringPi.h>


float randfloat(float a) {
   return (float)rand()/(float)(RAND_MAX/a);
}

int main() {

    svSetup();
    intSetup();
    usSetup();
    accSetup();
    ledSetup();
    int i = 0;
    while (i == 0) {
        
        printf("INT: 1: %f | 2: %f | 3: %f | 4: %f\n", intGetIntensity(1), 
        intGetIntensity(2), intGetIntensity(3), intGetIntensity(4));
        
        //ledPingRed();
        
        //ledPingGreen();        


        //printf("US: 1: %f \n", usGetDistance(1));

        //printf("US: 1: %f | 2: %f | 3: %f | 4: %f | 5: %f \n", 
        //usGetDistance(1), usGetDistance(2), usGetDistance(3),
        //usGetDistance(4), usGetDistance(5));
        
        //printf("ACC: X: %f | Y: %f |\n", accGetAccX(), accGetAccY());
        //printf("ACC: X: %f \n", accGetAccX());
        
        //svRide(-1);
        //svRide(randfloat(-1));
    
        //svTurn(1);
        //svTurn(randfloat(-1));
        
    }
    gpioTerminate();
    intClose();
    
    return 0;
}
