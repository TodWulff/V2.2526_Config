echo 'klipper_dialog S="Pushing a config backup"' > ~/printer_data/comms/klippy.serial

params=""
for element in "$@"
do
	params="$params $element"
done

cd ~/printer_data/config
git fetch && git status
git add .
git commit -m "$params"
git push

echo 'klipper_dialog S="Config backup complete"' > ~/printer_data/comms/klippy.serial
