#Cleanup every 24 h
while true; do
    rm -r /home/pi/bios_fish/ML-examples/yeah-world/example/*
    sleep 24h
done