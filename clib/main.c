#include <stdio.h>
#include "ultrasonic.h"

int main(){
    int i = 0;
    
    usSetup();
    while (i == 0){
        printf("USonics: %f %f %f \n", usGetDistanceLeft(), usGetDistanceCenter(), usGetDistanceRight());
    }
    
    return 0;
}

