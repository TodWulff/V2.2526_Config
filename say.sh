mkdir -p ~/temp

params=""
for element in "$@"
do
	params="$params $element"
done

pico2wave -l en-US -w ~/temp/temp.wav "$params" > /dev/null 2>&1 &

cvlc --gain 2 --quiet --play-and-exit ~/temp/temp.wav > /dev/null 2>&1 &
