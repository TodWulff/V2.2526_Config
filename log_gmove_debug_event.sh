#!/bin/bash

echo $(date +%H:%M:%S.%N) $@ >> /home/pi/printer_data/logs/gmove_debug.log &
