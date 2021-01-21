# Bingo Simulator

This project is a bingo simulation, designed to both play-out a bingo game in a GUI and display the different bingo
boards used on a breadboard containing a 5x5 grid of LED's. The purpose of this project was to incorporate
electrical engineering concepts into the code in some way, as well as perform a statistical analysis on the bingo
game itself.

### Running the code

While this code was initially designed to run on a Raspberry Pi in conjunction with LED's on a breadboard,
I have modified it to simply run on a computer (commented out anything hardware related). To see the demonstration, run `src/main.py` to
start up the GUI.

### The interactive game

The simulator is designed to be entirely run from a raspberry pi 3 connected to a breadboard with LED's arranged in a
5x5 matrix, with the LED at 0x0 corresponding to port 2, increasing by row until LED at 4x4 corresponding to port 26.
The raspberry pi should also be connected to a monitor / keyboard so that the GUI can be interacted with.

### The simulation results

The file `Stat Analysis Results.pdf` contains the results of the repeated execution of `src/STATmain.py`, which runs the bingo game
a specified number of times, for a specified number of boards, counting how many times each board won and the average
number of tiles that need to be called before a winner is determined. The results show a logarithmic relationship between
the number of boards and the number of tiles called out before a winner occurred.

### Improvements that could have been made

The initial game was created with a focus on GUI output and LED output, not on the simulation of many games across
varying amounts of boards, which is why there are duplicate classes for util, board, and main. In hindsight, I should have
created a parent class that the display version and statistical version inheritted from. Luckily the project was small
enough that this didn't pose any large issues.

### Concluding thoughts

I am proud of this project since I generally was able to uphold strong programming design skills. All methods within each
class very closely relate the purpose of said class, demonstrating strong cohesion. Since I had to duplicate code there
is probably unecessary coupling throughout, but generally the code is very neat, methods are small and focused, and the code
is readable.
