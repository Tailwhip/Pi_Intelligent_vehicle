cdef extern from "../clib/led.h":

    void ledSetup();
    
    void ledPingGreen();
    
    void ledPingRed();

def setup():
    return ledSetup()

def ping_green():
    return ledPingGreen()

def ping_red():
    return ledPingRed()

