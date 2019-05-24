#include <stdio.h>
#include "ultrasonic.c"
#include "intensity.c"
#include "acceleration.c"

int main(){
    int i = 0;
    
    usSetup();
    intSetup();
    velSetup();
    
    while (i == 0){
        printf("US: %f %f %f     | Intense: %f %f     | Acceleration: %f %f \n", 
        usGetDistanceLeft(), usGetDistanceCenter(), usGetDistanceRight(),
        intGetIntensFrontLeft(), intGetIntensFrontRight(),
        accGetAccX(), accGetAccX());
    }
    return 0;
}

