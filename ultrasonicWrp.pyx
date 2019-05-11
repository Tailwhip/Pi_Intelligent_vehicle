cdef extern from "clib/ultrasonic.h":
    int TRIG_1
    int ECHO_1

    int TRIG_2
    int ECHO_2

    int TRIG_3
    int ECHO_3
    
    int distanceOld
    int firstTimer

    void usSetup()

    float usGetDistanceLeft()

    float usGetDistanceCenter()

    float usGetDistanceRight()

def setup():
    return usSetup()

def getDistLeft():
    return usGetDistanceLeft()

def getDistCenter():
    return usGetDistanceCenter()

def getDistRight():
    return usGetDistanceRight()
