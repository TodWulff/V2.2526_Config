#!/bin/sh

mkdir -p ~/temp

params=""
for element in "$@"
do
	params="$params $element"
done

#for troubleshooting - writes to klipper console even if verbose is false
echo "M118 <font color=orange>$params</font>" > ~/printer_data/comms/klippy.serial

#generate tts audio file
pico2wave -l en-US -w ~/temp/temp.wav "$params" > /dev/null 2>&1

#play the tts audio, waiting until complete before finishing
#cvlc --gain 2 --quiet --play-and-exit ~/temp/temp.wav > /dev/null 2>&1
aplay ~/temp/temp.wav > /dev/null 2>&1