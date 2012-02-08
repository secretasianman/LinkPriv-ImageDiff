#!/bin/bash

while read line; do
    ./webkit2png.py http://$line -o images/${line}
#    ./webkit2png.py http://$line -o images/${line}_160_100 --scale 160 100
#    ./webkit2png.py http://$line -o images/${line}_320_200 --scale 320 200
#    ./webkit2png.py http://$line -o images/${line}_480_300 --scale 480 300
done < "websites.txt"
