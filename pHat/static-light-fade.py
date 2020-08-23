import unicornhat as uh
import random
import time
import sys

uh.set_layout(uh.PHAT)
uh.brightness(1)

interval = int(sys.argv[1])
fadeInterval = float(sys.argv[2])
red = int(sys.argv[3])
green = int(sys.argv[4])
blue = int(sys.argv[5])

redIncStep = int((red/fadeInterval)/8)
greenIncStep = int((green/fadeInterval)/8)
blueIncStep = int((blue/fadeInterval)/8)

localRed = 0
localGreen = 0
localBlue = 0

#---------------fade in
print('start fade in')
while(fadeInterval > 0) :
    localRed += redIncStep
    localGreen += greenIncStep
    localBlue += blueIncStep
    for x in range(8):
        for y in range(4):
            uh.set_pixel(x, y, localRed, localGreen, localBlue)

    uh.show()
    time.sleep(0.12)
    fadeInterval = fadeInterval - 0.12
    
#---------------display color
print('start display')
for x in range(8):
    for y in range(4):
        uh.set_pixel(x, y, localRed, localGreen, localBlue)

uh.show()
time.sleep(interval)
fadeInterval = float(sys.argv[2])

#---------------fade out
print('start fade out')
while(fadeInterval > 0) :
    localRed -= redIncStep
    localGreen -= greenIncStep
    localBlue -= blueIncStep
    for x in range(8):
        for y in range(4):
            uh.set_pixel(x, y, localRed, localGreen, localBlue)

    uh.show()
    time.sleep(0.12)
    fadeInterval = fadeInterval - 0.12

uh.clear()
uh.show()
uh.off()
print('end')
