#say_wait Pushing a config backup	#echos to klipper console too


# parse commit message (possibly unquoted) into a single string
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

#say_wait Complete	#echos to klipper console too

