cd ~/klipper_config
git fetch
echo "Pulling a config restore - will restart Klipper if config changes exist."
if git status | grep -q 'Your branch is behind'; then
  git pull && echo "Changes exist, pulled & restarting Klipper" && echo 'M118 GIT Repo Pull RESTART' > /tmp/printer && echo RESTART > /tmp/printer
else
	echo "No changes exist, configs are up to date."
fi
