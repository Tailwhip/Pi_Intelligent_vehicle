#include <stdio.h>
#include "ultrasonic.c"
#include "intensity.c"
#include "velocity.c"

int main(){
    int i = 0;
    
    usSetup();
    intSetup();
    velSetup();
    
    while (i == 0){
        printf("US: %f %f %f     | Intense: %f %f     | Velocity: %f \n", 
        usGetDistanceLeft(), usGetDistanceCenter(), usGetDistanceRight(),
        intGetIntensFrontLeft(), intGetIntensFrontRight(),
        velGetVelocityX());
    }
    return 0;
}

