import ultrasonic as us
import intensity as int
import acceleration as acc
import servo as sv

us.setup()
int.setup()
sv.setup()
acc.setup()

while True:
    print("US: {} {} {} {} {} | INT: {} {} {} {} | ACC: {} {}".format(us.getDistance(1), us.getDistance(2),
    us.getDistance(3), us.getDistance(4), us.getDistance(5), int.getIntensity(1), int.getIntensity(2),
    int.getIntensity(3), int.getIntensity(4), acc.getAccX(), acc.getAccY()))
    sv.ride(0.1355)
    sv.turn(0.4658)