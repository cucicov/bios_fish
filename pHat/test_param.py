import unicornhat as uh
import random
import time
import sys

uh.set_layout(uh.PHAT)
uh.brightness(1)

for x in range(8):
    for y in range(4):
        uh.set_pixel(x, y, int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

uh.show()
time.sleep(30)