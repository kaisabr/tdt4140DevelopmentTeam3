from carInput import *

car = carInput()
speed = car.getCurrentSpeed()
while speed:
    speed = car.getCurrentSpeed()
    if speed != None:
        print(speed)
