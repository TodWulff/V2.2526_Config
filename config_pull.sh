cd ~/klipper_config
git fetch
echo "Pulling a config restore - will restart Klipper if config changes exist."
if git status | grep -q 'Your branch is behind'; then
  git pull && echo "Changes exist, pulled & restarting Klipper" && echo 'M118 Updated configs from git, restarting...' > /tmp/printer && echo RESTART > /tmp/printer
fi
