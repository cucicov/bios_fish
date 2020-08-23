import unicornhat as uh
import random
import time

uh.set_layout(uh.AUTO)
uh.brightness(1)

for x in range(8):
    for y in range(4):
        uh.set_pixel(x, y, 255, 0, 0)

uh.show()
time.sleep(5)

for x in range(8):
    for y in range(4):
        uh.set_pixel(x, y, 0, 255, 0)

uh.show()
time.sleep(5)

for x in range(8):
    for y in range(4):
        uh.set_pixel(x, y, 0, 0, 255)

uh.show()
time.sleep(5)
    

for x in range(8):
    for y in range(4):
        uh.set_pixel(x, y, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

uh.show()
time.sleep(5)


for x in range(8):
    for y in range(4):
        uh.set_pixel(x, y, 255, 255, 255)

uh.show()

uh.off()
