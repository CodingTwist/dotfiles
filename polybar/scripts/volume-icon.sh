#!/bin/sh
HEADPHONES="alsa_output.usb-Logitech_G510s_Gaming_Keyboard-02.analog-stereo"

if [[ $(pactl info | sed -En 's/Default Sink: (.*)/\1/p') = $HEADPHONES ]]; then
	echo ""
else
	echo ""
fi
