echo "Pushing a config backup."
#say  "Pushing a config backup."

# echo '{action_respond_info("Pushing a config backup.")}' > ~/printer_data/comms/klippy.serial
echo 'M118 Pushing a config backup.' > ~/printer_data/comms/klippy.serial
say_wait  Pushing a kunfihg backup.
echo 'M118 Commit Message $@.' > ~/printer_data/comms/klippy.serial

cd ~/printer_data/config
git fetch && git status
git add .
git commit -m '$@' 
git push
echo "Config backup complete."
#say  "Config backup complete."
echo 'M118 Config backup complete.' > ~/printer_data/comms/klippy.serial
# echo '{action_respond_info("Config backup complete.")}' > ~/printer_data/comms/klippy.serial
say_wait  Complete.
