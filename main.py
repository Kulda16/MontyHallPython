import argparse

from src.montyhall import *
from src.plot import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Monty Hall Problem',
        description='Input your options, how you want to play the game.',
        epilog='Version 1.0.0',
        add_help=False,
    )
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='Show this help message and exit.')
    parser.add_argument('--switch', default=True, action=argparse.BooleanOptionalAction,
                        help='Switch: True by default. Change if you do not want to switch.')
    parser.add_argument('-ns', '--num_simulations', type=int,
                        help='Input number of simulations of the game. 100 simulations by default.')
    parser.add_argument('--show_logs', default=False, action=argparse.BooleanOptionalAction,
                        help='Show Logs: False by default. Change if you want to see the results of the game.')
    parser.add_argument('-pf', '--print_fig', default=False, action=argparse.BooleanOptionalAction,
                        help='Print Figure: False by default. Change if you want to print and save a figure.')
    args = parser.parse_args()

    if args.print_fig:
        x = monty_hall_game(args.switch, args.num_simulations, args.show_logs)
        game_statistics(x)
        plot_monty_hall(args.switch, args.num_simulations, fileformat="pdf")
        print(f"The file has been saved in .pdf format in 'outputs' root directory.")
    else:
        x = monty_hall_game(args.switch, args.num_simulations, args.show_logs)
        game_statistics(x)




