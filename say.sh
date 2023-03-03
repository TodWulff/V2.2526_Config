#!/bin/bash

# pico2wave -l en-US -w ~/temp/temp.wav "$1" > /dev/null 2>&1 &

## the above choked on emitting the first word when the parameters were passed from Klipper to this script by way of shell command.
## I suspect that I just didn't fight long enough to get to klipper to pass the string encapsulation characters when shell commands kicked it off.
## Regardless, the following works and, as a side benefit, from the linux shell you don't need to wrap the string in single or double quotes.
## prolly bad forum, but meh, it works and I taint going to fix it any more.

# create a temp directory in user's home folder if it doesn't exist
mkdir -p ~/temp

# parse and assemble parameters as a single long parameter
# 'side benefit': being able to pass a sentence for speech synthesis
# without encapsulating it in string encapsulation characters
# say This: is , a silly example! .
params=""
for element in "$@"
do
	params="$params $element"
done

# create a temp.way of the generated speech synthesis sans console delay/traffic
pico2wave -l en-US -w ~/temp/temp.wav "$params" > /dev/null 2>&1 &

# and play the converted speech over the audio system
cvlc --gain 2 --quiet --play-and-exit ~/temp/temp.wav > /dev/null 2>&1 &
# ^^^ optional if one favors vlc, or, if you're using aplay (raspbian) the following line works
# aplay ~/temp/temp.wav > /dev/null 2>&1 &



### So this shell script will work stand alone from the linux shell. To make use of this from within Klipper Macros, the use of
### the shell command module (installable with th33xitus' kiauh script) is how I chose to pursue it.  The following is what I did
### to make it work from macros (and the console):
### 
### In shell_command.cfg:
### 
### 	[gcode_shell_command say_it]
### 	command: sh /home/pi/printer_data/config/say.sh
### 	timeout: 2
### 	verbose: false
### 
### Klipper gcode utility macro
### 
### 	[gcode_macro SAY]
### 	gcode:
### 		RUN_SHELL_COMMAND CMD=say_it PARAMS='{params.S}'
### 
### Then, from the console or from within your macros (i.e. print start, pause, cancel, etc.) you can issue a command in the following form
### and the host should timely emit the speech without stalling the processing of gcode, I perceive.  If this is not the case, let me know:
### 
### [gcode_macro some_user_macro]
### ...
### gcode:
### 	...
### 	say_wait S="My this is, if nothing else, quite neat!"
### 	...
###
###	Enjoy!
###
### ~MHz


