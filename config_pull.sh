echo 'klipper_dialog S="Checking for updated configs"' > ~/printer_data/comms/klippy.serial
cd ~/printer_data/config
git fetch

if git status | grep -q 'Your branch is behind'; then
	git pull --ff-only
	echo 'klipper_dialog S="Updated Configs Pulled"' > ~/printer_data/comms/klippy.serial
	echo 'g4 p1500' > ~/printer_data/comms/klippy.serial
	echo 'RESTART' > ~/printer_data/comms/klippy.serial
else
	echo 'say_wait_nc S="No Config Changes"' > ~/printer_data/comms/klippy.serial
fi
