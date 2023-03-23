#!/bin/sh

#ensure user temp dir exists
mkdir -p ~/temp

#concatenate all passed elements as a single phrase
phrase=""
for element in "$@"
do
	phrase="$phrase $element"
done

#generate tts audio file
gtts-cli "$phrase" -o /home/pi/temp/temp.wav > ~/temp/temp_gtts.log 2>&1

#play the tts audio, returning when done making noise
cvlc --gain 1.5 --quiet --rate 1.25 --play-and-exit ~/temp/temp.wav > ~/temp/temp_cvlc.log 2>&1 
