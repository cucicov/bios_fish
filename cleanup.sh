#Cleanup every 6 h
while true; do
    rm -r /home/pi/bios_fish/ML-examples/yeah-world/example/*
    sleep 6h
done