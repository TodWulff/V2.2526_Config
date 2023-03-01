cd ~/printer_data/config
git fetch
echo "Pulling a config restore - will restart Klipper if config changes exist."
if git status | grep -q 'Your branch is behind'; then
  git pull && echo "Changes exist, pulled & restarting Klipper" && echo 'M118 GIT Repo Pull RESTART' > ~/printer_data/comms/klippy.serial && echo RESTART > ~/printer_data/comms/klippy.serial
else
	echo "No changes exist, configs are up to date."
	SAY "No changes exist, configs are up to date."
	echo 'M118 No changes exist, configs are up to date.' > ~/printer_data/comms/klippy.serial
#	echo '{action_respond_info("No changes exist, configs are up to date.")}' > ~/printer_data/comms/klippy.serial

fi
