#!/bin/sh

#concatenate all passed elements as a single phrase
phrase=""
for element in "$@"
do
	phrase="$phrase $element"
done

#writes to klipper console
echo "M118 <font color=gray>Brody🔇: </font><font color=lime>$phrase</font>" > ~/printer_data/comms/klippy.serial
