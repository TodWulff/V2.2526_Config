#!/bin/bash
val=$(top -bd 0.1 -n 1 | grep '%Cpu(s):'| tail -1 | awk '{print $8}')
str="save_variable VARIABLE=last_cpu_idle VALUE='\"$val\"'"
echo "$str"
echo "$str" > ~/printer_data/comms/klippy.serial

