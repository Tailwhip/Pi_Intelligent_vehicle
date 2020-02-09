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

void writeToFile(FILE *f, float *intensities, int count) {
    for (int i = 0; i < count; i++) {
        fprintf(f, "%f | ", intensities[i]);
    }
    fprintf(f, "\n");
}

int main() {
    svSetup();
    intSetup();
    usSetup();
    //accSetup();
    ledSetup();
    //svRide(0, 1);
    
    FILE *f = fopen("Intensities.txt", "w");
    if (f == NULL)
    {
        printf("Error opening file!\n");
        exit(1);
    }
    
    fprintf(f, "INT1 | INT2 | INT3 | INT4 \n");
    /*
    float buffer[4] = {0, 0, 0, 0};
    
    size_t n = sizeof(buffer)/sizeof(*buffer);
    
    int count = (int)n;
    */
    int i = 0;
    while (i == 0) {
        /*
        for (int i = 0; i < count; i++) {
            buffer[i] = intGetIntensity(i+1);
        }
        
        writeToFile(f, buffer, count);
        */
        
        //svStop();
        printf("\e[1;1H\e[2J");
        //printf("INT: 1: %f | 2: %f | 3: %f | 4: %f \n", intGetIntensity(1), 
        //intGetIntensity(2), intGetIntensity(3), intGetIntensity(4));
        
        //ledPingRed();
        
        //ledPingGreen();        
        
        printf("US: 1: %f | 2: %f | 3: %f | 4: %f | 5: %f \n", 
        usGetDistance(1), usGetDistance(2), usGetDistance(3),
        usGetDistance(4), usGetDistance(5));
        
        //printf("%+10f", accGetAccX());
        //time_sleep(0.005);
        
        //printf("ACC: X:  % -1f | Y: % -1f | Z: % -1f |\n", accGetAccX(), accGetAccY(), accGetAccZ());
        //printf("ACC: X: %+1f \n", accGetAccX());

        //svStop();
        //svRide(0, 1);
        //svForward(-1);
        
        //svTurn(1);
        //svTurn(randfloat(-1));
        
    }
    //gpioTerminate();
    intClose();
    
    return 0;
}
