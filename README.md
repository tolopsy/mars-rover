# Mars Rover

A program to distribute locomotive instructions to clusters of robotic rovers on a plateau with known boundary values.
Each rover executes a set of instructions to move and change orientation.

Input contains:

    - Plateau's top-right coordinates assuming the land is rectangular and the bottom-left coordinate is 0,0.
    - Each rover's landing position in the format `x y r` where x and y represents rover's cartesian position
      and r represents rover's orientation which can be N, E, W or S (The four cardinal points).
    - Instructions for each rover to execute. Each instruction is a string of characters containing `L`, `R` and/or `M`.
      `L` tells rover to rotate 90 degrees to the left. `R` tells rover to rotate 90 degrees to the right.
      `M` tells rover to move one unit forward in the direction of its orientation.
See more on input in the [usage](#usage) section.


## Pre-requisites
    - Python 3.8
    - Make utility


## Requirements
To install requirements, run `pip3 install -r requirements.txt` in terminal.


## NOTE: 
All `make` command should be run in the 'Mars Rover' project directory.


## Run test
To run test, run `make test` in terminal.


## Build application
To build application, run `make build` in terminal.


## Clean build
To clean previous build, run `make clean` in terminal.


## Usage Pre-requisites
- After build, the executable program is stored inside 'dist' folder of the project directory.
    You can run the program from the 'dist' folder. For example: `./dist/app -h`

- To run the executable program directly. Add the 'dist' path to the system's '$PATH'.
    To do this:
        - Ensure that your working directory is the project's directory
        - Run `export PATH="$(pwd)/dist:$PATH"`
        Now you can run the executable program 'app' directly in the terminal. For example: `app -h`


## Usage
- To accept input from a file, simply run `./dist/app <filepath>` OR `app <file_path>`.
    Example: 
        - `app input.txt`

- To accept input from the command line, use the '-p' and '-r' flags.
    -p: takes one input representing the plateau input.
    -r: takes list of inputs representing per rover landing/instruction input.
    Example:
        - `app -p "Plateau:5 5" -r "Rover1 Landing:1 2 N" "Rover1 Instructions:LMLMLMLMM" "Rover2 Landing:3 3 E" "Rover2 Instructions:MMRMMRMRRM"`

- Use the -h to print the help message. For example: `app -h`
