#!/usr/bin/env bash

val=$[100-$(vmstat 1 1|tail -1|awk '{print $15}')]
str="save_variable VARIABLE=last_cpu_util VALUE=$val"
echo $str > ~/printer_data/comms/klippy.serial
