#!/bin/bash

echo $(date +%H:%M:%S.%N) $@ >> /home/pi/printer_data/logs/state_debug.log &
