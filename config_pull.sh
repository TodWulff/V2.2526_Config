say_wait Checking for updated configs
cd ~/printer_data/config
git fetch

if git status | grep -q 'Your branch is behind'; then
	git pull --ff-only
	say_wait Changes pulled - restarting Klipper
	echo 'RESTART' > ~/printer_data/comms/klippy.serial
else
	say_wait No changes
	# echo 'UPDATE_DELAYED_GCODE ID=_advise_printer_state DURATION=0.1' > ~/printer_data/comms/klippy.serial

fi
