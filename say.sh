#!/bin/sh

# this worked well out of the gate with Raspiban hosts.  However, on Debian, it was not so
# ended up with a bloody forehead before piping output to temp log and tailing that with
# tail -f -n40 temp_gtts.log  and  tail -f -n40 temp_cvlc.log then discovered cvlc was emitting:
#        ALSA lib pcm_dmix.c:1075:(snd_pcm_dmix_open) unable to open slave
# giggled my way to success:
# https://dev.to/setevoy/linux-alsa-lib-pcmdmixc1108sndpcmdmixopen-unable-to-open-slave-38on
# missing modprobe.d conf file...


#ensure user temp dir exists
mkdir -p ~/temp

#concatenate all passed elements as a single phrase
phrase=""
for element in "$@"
do
	phrase="$phrase $element"
done

#for troubleshooting - writes to klipper console even if verbose is false
echo "M118 <font color=gray>Brody: </font><font color=lime>$phrase</font>" > ~/printer_data/comms/klippy.serial

#generate tts audio file
gtts-cli "$phrase" -o /home/pi/temp/temp.wav > ~/temp/temp_gtts.log 2>&1
#pico2wave -l en-US -w ~/temp/temp.wav "$phrase" > /dev/null 2>&1

#gtts-cli "$phrase" | mpg123 - > /dev/null 2>&1 &

#play the tts audio, returning immediately
cvlc --gain 2 --quiet --rate 1.25 --play-and-exit ~/temp/temp.wav > ~/temp/temp_cvlc.log 2>&1 &
#cvlc --gain 2 --quiet --play-and-exit ~/temp/temp.wav > /dev/null 2>&1 &
#aplay /home/pi/temp/temp.wav > /dev/null 2>&1 &
#aplay ~/temp/temp.wav > /dev/null 2>&1
#mplayer /home/pi/temp/temp.wav > /dev/null 2>&1 &
