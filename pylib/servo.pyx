cdef extern from "../clib/servo.h":

    void svSetup();

    void svRide(float quality);

    void svTurn(float quality);

def setup():
    return svSetup()

def ride(_quality):
    return svRide(_quality)

def turn(_quality):
    return svTurn(_quality)

