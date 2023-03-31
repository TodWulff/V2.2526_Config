#!/bin/bash

echo -e "\\033[XXm"

for i in range(30,37+1):
    echo -e "\033[%dm%d\t\t\033[%dm%d" % (i,i,i+60,i+60);

echo -e "\033[39m\\033[49m - Reset colour"
echo -e "\\033[2K - Clear Line"
echo -e "\\033[<L>;<C>H OR \\033[<L>;<C>f puts the cursor at line L and column C."
echo -e "\\033[<N>A Move the cursor up N lines"
echo -e "\\033[<N>B Move the cursor down N lines"
echo -e "\\033[<N>C Move the cursor forward N columns"
echo -e "\\033[<N>D Move the cursor backward N columns"
echo -e "\\033[2J Clear the screen, move to (0,0)"
echo -e "\\033[K Erase to end of line"
echo -e "\\033[s Save cursor position"
echo -e "\\033[u Restore cursor position"
echo -e " "
echo -e "\\033[4m  Underline on"
echo -e "\\033[24m Underline off"
echo -e "\\033[1m  Bold on"
echo -e "\\033[21m Bold off"
