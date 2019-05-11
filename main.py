import ultrasonicWrp as us

us.setup()

while True:
    print("US: {} {} {}".format(us.getDistLeft(), us.getDistCenter(),
                                us.getDistRight()))
