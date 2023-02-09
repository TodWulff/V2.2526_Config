echo "Pushing a config backup."
cd ~/printer_data/config
git fetch && git status
git add .
git commit -m 'printer event - automated config backup'
git push
echo "Config backup complete."