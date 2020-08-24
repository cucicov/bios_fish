# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Run a trained model on frames from the camera and play random sounds when
class 0 is detected.
"""
from __future__ import print_function

from sys import argv, stderr, exit
from os import getenv

import numpy as np
from tensorflow import keras

from camera import Camera
from pinet import PiNet
from randomsound import RandomSound
import unicornhat as uh
import random
import time
import math
import logging

# Smooth out spikes in predictions but increase apparent latency. Decrease on a Pi Zero.
#SMOOTH_FACTOR = 0.8


def main():
    # ---- camera init
    uh.set_layout(uh.PHAT)
    uh.brightness(1)
    #------

    model_file = argv[1]
    countdown = int(argv[2])


    # We use the same MobileNet as during recording to turn images into features
    print('Loading feature extractor')
    extractor = PiNet()


    # Here we load our trained classifier that turns features into categories
    print('Loading classifier')
    classifier = keras.models.load_model(model_file)

    
    # Initialize the camera and sound systems
    camera = Camera(training_mode=False)
    #random_sound = RandomSound()

    # Create a preview window so we can see if we are in frame or not
   

    # Smooth the predictions to avoid interruptions to audio
    smoothed = np.ones(classifier.output_shape[1:])
    smoothed /= len(smoothed)
    
    # init logger
    logger = logging.getLogger('bios-fish')
    hdlr = logging.FileHandler('/home/pi/bios_fish/log.txt')
    formatter = logging.Formatter('%(asctime)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.INFO)

    print('Now running!')
    while countdown > 0 :
        raw_frame = camera.next_frame()

        # Use MobileNet to get the features for this frame
        z = extractor.features(raw_frame)

        # With these features we can predict a 'normal' / 'yeah' class (0 or 1)
        # Keras expects an array of inputs and produces an array of outputs
        classes = classifier.predict(np.array([z]))[0]

        # smooth the outputs - this adds latency but reduces interruptions
        smoothed = smoothed * 0.8 + classes * (1.0 - 0.8)
        selected = np.argmax(smoothed) # The selected class is the one with highest probability
        
        calculateRed=math.floor(smoothed[0] * 255)
        calculatedGreen=math.floor(smoothed[1] * 255) + math.floor(smoothed[0] * 50)
        calculatedBlue=math.floor(smoothed[2] * 255) + math.floor(smoothed[0] * 50)
        calculatedWhite=math.floor(smoothed[3] * 255)
        if (calculateRed + calculatedWhite > 255):
            calculateRed = 255
        else:
            calculateRed = calculateRed + calculatedWhite
            
        if (calculatedGreen + calculatedWhite > 255):
            calculatedGreen = 255
        else:
            calculatedGreen = calculatedGreen + calculatedWhite
            
        if (calculatedBlue + calculatedWhite > 255):
            calculatedBlue = 255
        else:
            calculatedBlue = calculatedBlue + calculatedWhite
            
        uh.set_all(calculateRed, calculatedGreen, calculatedBlue)
        uh.show()

        # Show the class probabilities and selected class
        summary = 'Class %d [%s]' % (selected, ' '.join('%02.0f%%' % (99 * p) for p in smoothed))
        stderr.write('\r' + summary)
        logger.info(summary)

        # Perform actions for selected class. In this case, play a sound from the sounds/ dir
#        if selected == 0:
#            random_sound.play_from('sounds/')
#        else:
#            random_sound.stop()

        # Show the image in a preview window so you can tell if you are in frame
        time.sleep(0.2)
        countdown = countdown - 1


if __name__ == '__main__':
    main()
