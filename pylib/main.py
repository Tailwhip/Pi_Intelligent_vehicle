import ultrasonic as us

us.setup()

while True:
    print("US: {} {} {}".format(us.getDistance(1), us.getDistance(2),
                                us.getDistance(3)))
