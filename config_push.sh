echo "Pushing a config backup."
say  "Pushing a config backup."
echo 'M118 Pushing a config backup.' > ~/printer_data/comms/klippy.serial
# echo '{action_respond_info("Pushing a config backup.")}' > ~/printer_data/comms/klippy.serial

cd ~/printer_data/config
git fetch && git status
git add .
git commit -m 'printer event - automated config backup'
git push
echo "Config backup complete."
SAY  "Config backup complete."
echo 'M118 Config backup complete.' > ~/printer_data/comms/klippy.serial
# echo '{action_respond_info("Config backup complete.")}' > ~/printer_data/comms/klippy.serial
