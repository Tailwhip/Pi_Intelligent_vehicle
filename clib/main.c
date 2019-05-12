#include <stdio.h>
#include "ultrasonic.c"
#include "intensity.c"

int main(){
    int i = 0;
    
    usSetup();
    intSetup();
    
    while (i == 0){
        printf("US: %f %f %f | Intense: %f %f \n", usGetDistanceLeft(), usGetDistanceCenter(), usGetDistanceRight(),
         intGetIntensFrontLeft(), intGetIntensFrontRight());
    }
    
    return 0;
}

