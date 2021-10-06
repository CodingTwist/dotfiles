#!/bin/bash

currentFallback=$(pactl list short sinks | grep RUNNING | cut -c 1)
if [ $currentFallback -eq 1 ]
then
    value=0
else
    value=1
fi

pacmd set-default-sink $value


