#include <stdio.h>
#include <stdlib.h>
#include <pigpio.h>
#include "ultrasonic.h"
#include "intensity.h"
#include "acceleration.h"
#include "servo.h"

float randfloat(float a) {
   return (float)rand()/(float)(RAND_MAX/a);
}

int main() {
    
    int i = 0;
    svSetup();
    intSetup();
    usSetup();
    accSetup();
    
    while (i == 0) {
        
        printf("US: %f %f %f %f %f | INT: %f %f %f %f | ACC: %f %f \n",
        usGetDistance(1), usGetDistance(2), usGetDistance(3),
        usGetDistance(4), usGetDistance(5), intGetIntensity(1), 
        intGetIntensity(2), intGetIntensity(3), intGetIntensity(4),
        accGetAccX(), accGetAccY());
        
        svRide(randfloat(1));
        svRide(randfloat(-1));
    
        svTurn(randfloat(1));
        svTurn(randfloat(-1));
    }
    gpioTerminate();
    intClose();
    
    return 0;
}
