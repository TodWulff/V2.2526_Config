cd ~/klipper_config
git fetch
if git status | grep -q 'Your branch is behind'; then
  git pull && echo "restarting" && echo 'M118 Updated configs from git, restarting...' > /tmp/printer && echo RESTART > /tmp/printer
fi