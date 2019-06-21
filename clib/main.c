#include <stdio.h>
#include <stdlib.h>
#include "ultrasonic.c"
#include "intensity.c"
//#include "acceleration.c"
#include "servo.c"

float randfloat(float a)
{
   return (float)rand()/(float)(RAND_MAX/a);
}

int main() {
    
    int i = 0;
    intSetup();
    usSetup();
    //velSetup();
    
    while (i == 0) {
        
        printf("US: %f %f %f %f %f INT: %f %f %f \n",
        usGetDistance(1), usGetDistance(2), usGetDistance(3),
        usGetDistance(4), usGetDistance(5), intGetIntensity(1), 
        intGetIntensity(2), intGetIntensity(4));
        //accGetAccX(), accGetAccY());
        
        // | Intense: %f %f     | Acceleration: %f %f \n"
        
        svRide(randfloat(1));
        svRide(randfloat(-1));
    
        svTurn(randfloat(1));
        svTurn(randfloat(-1));
    }
    
    intClose();
    
    return 0;
}
