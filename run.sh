#!/bin/sh

    cd /home/pi/bios_fish/pHat
    sudo python3 static-light-fade.py 120 40 255 70 170 &
    sleep 80

    cd /home/pi/bios_fish/ML-examples/yeah-world/ 
    sudo python3 record.py example/red 40

    echo "training with violet complete."
    sleep 80

    cd /home/pi/bios_fish/pHat
    sudo python3 static-light-fade.py 120 40 50 255 50 &
    echo "turning on color green"   
    sleep 80

    cd /home/pi/bios_fish/ML-examples/yeah-world/ 
    sudo python3 record.py example/green 40

    echo "training with green complete."
    sleep 80

    cd /home/pi/bios_fish/pHat
    sudo python3 static-light-fade.py 120 40 50 50 255 &
    echo "turning on color blue"   
    sleep 80 

    cd /home/pi/bios_fish/ML-examples/yeah-world/ 
    sudo python3 record.py example/blue 40

    echo "training with blue complete."
    sleep 80


    cd /home/pi/bios_fish/pHat
    sudo python3 static-light-fade.py 120 40 125 125 125 &
    echo "turning on color white" 
    sleep 80

    cd /home/pi/bios_fish/ML-examples/yeah-world/ 
    sudo python3 record.py example/white 40

    echo "training with white complete."
    sleep 80

    
    cd /home/pi/bios_fish/ML-examples/yeah-world/
    python3 train.py example/model.h5 example/red example/green example/blue example/white
    sudo python3 run.py example/model.h5 9000 #execute for 30 minutes.
    