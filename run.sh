#!/bin/sh

sh cleanup.sh &

while true; do

    cd /home/pi/bios_fish/pHat
    sudo python3 static-light-fade.py 120 20 255 70 170 &
    echo "Turning on light violet."
    sleep 60

    cd /home/pi/bios_fish/ML-examples/yeah-world/ 
    sudo python3 record.py example/red 40
    echo "Collecting data for violet."

    sleep 80

    cd /home/pi/bios_fish/pHat
    sudo python3 static-light-fade.py 120 20 50 255 50 &
    echo "Turning on light green."
    sleep 60

    cd /home/pi/bios_fish/ML-examples/yeah-world/ 
    sudo python3 record.py example/green 40
    echo "Collecting data for green."
    sleep 80

    cd /home/pi/bios_fish/pHat
    sudo python3 static-light-fade.py 120 20 50 50 255 &
    echo "Turning on light blue."
    sleep 60 

    cd /home/pi/bios_fish/ML-examples/yeah-world/ 
    sudo python3 record.py example/blue 40
    echo "Collecting data for blue."
    sleep 80


    cd /home/pi/bios_fish/pHat
    sudo python3 static-light-fade.py 120 20 160 160 160 &
    echo "Turning on light white."
    sleep 60

    cd /home/pi/bios_fish/ML-examples/yeah-world/ 
    sudo python3 record.py example/white 40
    echo "Collecting data for white."
    sleep 80


    cd /home/pi/bios_fish/ML-examples/yeah-world/
    echo "Training..."
    python3 train.py example/model.h5 example/red example/green example/blue example/white
    echo "A.I. ambient lighting ON"
    sudo python3 run.py example/model.h5 3600 #execute for 30 minutes. (3600)
    sleep 30m # sleep 30m

done
    
