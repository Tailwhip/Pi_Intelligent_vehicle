cdef extern from "../clib/ultrasonic.h":

    void usSetup();

    float usGetDistance(int sensNum);

def setup():
    return usSetup()

def getDistance(_sensNum):
    return usGetDistance(_sensNum)

