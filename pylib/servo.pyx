cdef extern from "../clib/servo.h":

    void svSetup();
    
    void svRide(float q0, float q1);

    void svForward(float quality);

    void svTurn(float quality);
    
    void svStop();

def setup():
    return svSetup()

def ride(_q0, _q1):
    return svRide(_q0, _q1)

def forward(_quality):
    return svForward(_quality)

def turn(_quality):
    return svTurn(_quality)

def stop():
    return svStop()

