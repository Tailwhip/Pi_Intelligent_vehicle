#include <stdio.h>
#include "ultrasonic.c"
#include "intensity.c"

int main(){
    int i = 0;
    
    usSetup();
    while (i == 0){
        printf("US: %f %f %f | Intense: %f \n", usGetDistanceLeft(), usGetDistanceCenter(), usGetDistanceRight(),
         intGetIntensFrontLeft());
    }
    
    return 0;
}

