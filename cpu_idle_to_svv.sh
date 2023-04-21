#!/bin/bash

# klipper shell commands calls this with a 'cpu_idle_to_svv' only, so need to do a:
# sudo ln -s /home/pi/printer_data/config/cpu_idle_to_svv.sh /usr/bin/cpu_idle_to_svv
# to get this callable from anywhere by anyone, after chmod 755'g it (prior to the symbolic link creation)

val=$(top -bd 0.1 -n 1 | grep '%Cpu(s):'| tail -1 | awk '{print $8}')
str="save_variable VARIABLE=last_cpu_idle VALUE='\"$val\"'"
echo "$str"
echo "$str" > ~/printer_data/comms/klippy.serial

