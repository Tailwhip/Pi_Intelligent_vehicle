cdef extern from "../clib/acceleration.h":

    void accSetup();

    float accGetAccX();

    float accGetAccY();

    float accAccDerivative(float acc);

def setup():
    return accSetup()

def getAccX():
    return accGetAccX()

def getAccY():
    return accGetAccY()

def getAccDerivative(_acc):
    return accAccDerivative(_acc)
