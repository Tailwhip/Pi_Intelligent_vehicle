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

    svSetup();
    intSetup();
    usSetup();
    accSetup();
    
    int i = 0;
    while (i == 0) {
        
        printf("US: %f %f %f %f %f \n", usGetDistance(1),
        usGetDistance(2), usGetDistance(3), usGetDistance(4),
        usGetDistance(5));
                
        //INT: %f %f %f %f         
        //intGetIntensity(1), intGetIntensity(2), intGetIntensity(3),
        //intGetIntensity(4));
        
        //ACC: %f %f
        //accGetAccX(), accGetAccY());

        /*
        svRide(randfloat(1));
        svRide(randfloat(-1));
    
        svTurn(randfloat(1));
        svTurn(randfloat(-1));
        */
    }
    gpioTerminate();
    intClose();
    
    return 0;
}
