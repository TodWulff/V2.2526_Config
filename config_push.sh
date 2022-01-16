echo "Pushing a config backup."
cd ~/klipper_config
git fetch && git status
git add .
git commit -m 'printer event - automated config backup'
git push
echo "Config backup complete."