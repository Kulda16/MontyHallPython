# MontyHallPython
Repository created for education purposes for course "Decision Theory and Analysis" in winter semester of acamidec year 
2023/2024 with provided numerical solution for Monty Hall Problem in Python.

## Before you start, make sure you have the following installed:
- any newer Linux distribution (recommended `Ubuntu 18` [and higher](https://ubuntu.com/download/desktop)),
- `Python 3.9` [and higher](https://www.python.org/downloads/),
- `pip 20.0` [and higher](https://pypi.org/project/pip/),
- optionally `Docker Destkop 4` [and higher](https://docs.docker.com/desktop/install/linux-install/) (if you want to run the program in a virtual container).

## Prerequisites

To clone the repository using HTTPS or SSH, run one of the following commands below in your terminal:

`git clone https://github.com/Kulda16/MontyHallPython.git`,

`git clone git@github.com:Kulda16/MontyHallPython.git`.

Make sure you are in cloned repository (and create) and activate the virtual environment:

`python -m venv ./.venv`,

`source .venv/bin/activate`.

Run the following for installing the required dependencies and libraries:

`pip install -r requirements.txt`.

## *Let's Make a Deal!* game

The application is fully controllable from the command line/terminal. To view the
help, run the following command:

` python main.py --help`.

The application has **4** mandatory parameters that you have to enter depending on what experiment you want to run:
1. `--switch / --no-switch` - the option for the contestant to change option number 2 to option number 1 in the game,
2. `--num_simulations` - the total number of game simulations you want to run,
3. `--show_logs / --no-show_logs` - option to enable/disable console listings/logs of individual game simulation results,
4. `--print_fig / --no-print_fig` - option to generate a graph of the probability of winning vs. 
5. the number of simulated games (saved in the `outputs` folder).

Example:

Following command will get you the 10000 runs of experiment, without switching contestant's
first choice and without showing the results of the game. Finally, it will plot you the graph.

`python main.py --no-switch -ns 10000  --no-show_logs --pr
int_fig`.



## Starting the application in Docker

## Contributing and the future work

In the `docs` directory you can find two documents. The first one is for operations, how to use the application. 
The second one is for developers, where in the future you should find mainly descriptions of functions, classes, parameters and their types.
If you would like to contribute to the repository, clone the repository, create a branch, develop and create a merge request.
The application is maintained as opensource, so feel free to use it!

Future work should include writing tests and completing documentation for proper further development and overall operations.