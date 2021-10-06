#!/bin/bash

url="http://192.168.1.162:8080/rest/items/"
item="RoomLights/state"

responce=$(curl -s -X GET --header "Accept: text/plain" "$url$item")

if [ "$responce" ==  "ON" ]; then
	echo " Lights: ON "

else
	echo " Lights: OFF "
fi

