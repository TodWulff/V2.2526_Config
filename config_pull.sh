cd ~/printer_data/config
git fetch
echo "Pulling a config restore - will restart Klipper if config changes exist."
# echo 'M118 Checking config status.' > ~/printer_data/comms/klippy.serial
say_wait Checking for updated kunfihgs.

if git status | grep -q 'Your branch is behind'; then
	git pull --ff-only
	echo "Changes exist, pulled & restarting Klipper" 
	echo 'M118 GIT Repo Pull RESTART' > ~/printer_data/comms/klippy.serial
	say_wait Changes pulled.
	echo RESTART > ~/printer_data/comms/klippy.serial
else
	echo "No changes exist, configs are up to date."
#	echo 'M118 No changes exist, configs are up to date.' > ~/printer_data/comms/klippy.serial
	say_wait No changes.
	echo 'UPDATE_DELAYED_GCODE ID=_advise_printer_state DURATION=0.1' > ~/printer_data/comms/klippy.serial

fi
