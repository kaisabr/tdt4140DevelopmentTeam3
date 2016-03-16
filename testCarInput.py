from carInput import *

car = carInput()

speed = car.getCurrentSpeed()
interiorlight = car.isInteriorLightOn()
doorStatus = car.isDoorOpen()
distance = car.distanceToCar()


while speed:
    if speed != None:
        print(speed)
    speed = car.getCurrentSpeed()

while interiorlight:
    print (interiorlight)
    interiorlight = car.isInteriorLightOn()

while doorStatus:
    print(doorStatus)
    doorStatus = car.isDoorOpen()


while distance:
    print(distance)

