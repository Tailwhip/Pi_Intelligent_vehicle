cdef extern from "../clib/intensity.h":

    void intSetup();

    void intClose();

    float intGetIntensity(int sensNum);

def setup():
    return intSetup()

def close():
    return intClose()

def getIntensity(_sensNum):
    return intGetIntensity(_sensNum)

