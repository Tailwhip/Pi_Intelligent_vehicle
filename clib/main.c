#include <stdio.h>
#include "ultrasonic.c"
#include "intensity.c"
#include "acceleration.c"
#include "servo.c"

int main() {
    int i = 0;
    
    usSetup();
    intSetup();
    velSetup();
    svSetup();
    
    
    
    /*
    while (i == 0){
        printf("US: %f %f %f     | Intense: %f %f     | Acceleration: %f %f \n", 
        usGetDistance(1), usGetDistance(3), usGetDistance(5),
        intGetIntensity(1), intGetIntensity(2),
        accGetAccX(), accGetAccY());
    }
    */
    return 0;
}

