import ultrasonicWrp as us

us.usSetup()

while True:
    print("US: {} {} {}".format(us.usGetDistanceLeft(), us.usGetDistanceCenter(),
                                us.usGetDistanceRight()))
