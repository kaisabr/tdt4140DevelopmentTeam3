from carInput import *

car = carInput()
speed = car.getCurrentSpeed()
interiorlight = car.isInteriorLightOn()
distance = car.distanceToCar()

while speed:
    speed = car.getCurrentSpeed()
    if speed != None:
        print(speed)

while interiorlight:
    print (interiorlight)
    interiorlight = car.isInteriorLightOn()

while distance:
    print(distance)

