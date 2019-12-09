# Bingo Simulator

This project is a bingo simulation, designed to both play-out a bingo game in a GUI and display the different bingo
boards used on a breadboard containing a 5x5 grid of LED's

### Running the code

#### The interactive game

The simulator is designed to be entirely run from a raspberry pi 3 connected to a breadboard with LED's arranged in a
5x5 matrix, with the LED at 0x0 corresponding to port 2, increasing by row until LED at 4x4 corresponding to port 26.
The raspberry pi should also be connected to a monitor / keyboard so that the GUI can be interacted with. If you wish to
run this code on a regular PC to use the GUI alone, then you must comment out all of the imports / uses of RPi.GPIO in
`src/util.py`.

#### The simulation results

The file `Stat Analysis Results.pdf` contains the results of the execution of 'src/STATmain', which runs the bingo game
a specified number of times, for a specified number of boards, counting how many times each board won and the average
number of tiles that need to be called before a winner is determined. This file can be run from a PC without any modification
