#!/bin/bash

#touch /home/pi/printer_data/logs/gmove_debug.log &
#echo $@ >> /home/pi/printer_data/logs/gmove_debug.log &
echo $(date +%H:%M:%S.%N) $@ >> /home/pi/printer_data/logs/gmove_debug.log &
