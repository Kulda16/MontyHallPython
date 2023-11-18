import os
import random
import numpy as np
import matplotlib.pyplot as plt
from src.montyhall import monty_hall_game

plt.style.use('fivethirtyeight')


def plot_monty_hall(switch: bool, num_simulations: int, fileformat: str):
    num_tests = []
    win_percentage = []
    filename = str(f"monty_hall_{switch}_{num_simulations}_{random.randint(1, 100)}")
    x = np.linspace(1, num_simulations, 10)
    y1 = np.repeat(0.67, 10)
    y2 = np.repeat(0.33, 10)

    if switch:
        for i in range(1, num_simulations):
            num_tests.append(i)
            y = monty_hall_game(switch, i, show_logs=False)
            win_percentage.append(y[1] / y[4])

        nazev = f"Monty Hallův problém se změnou původní volby: Ano"
        plt.figure(figsize=(12.2, 7.5), dpi=100)
        plt.plot(num_tests, win_percentage, label='závislost pravděpodobnosti výhry \nna počtu simulací hry')
        plt.plot(x, y1, color="r", label='funkce: y = 0.67')
        plt.title(nazev)
        plt.xlabel("Počet simulací hry")
        plt.ylabel("Procento vítězství")
        plt.legend(loc="upper right")
        plt.savefig(os.getcwd() + f"/outputs/{filename}.{fileformat}")
    else:
        for i in range(1, num_simulations):
            num_tests.append(i)
            y = monty_hall_game(switch, i, show_logs=False)
            win_percentage.append(y[0] / y[4])

        nazev = f"Monty Hallův problém se změnou původní volby: Ne"
        plt.figure(figsize=(12.2, 7.5), dpi=100)
        plt.plot(num_tests, win_percentage, label=f'závislost pravděpodobnosti výhry \nna počtu simulací hry')
        plt.plot(x, y2, color="r", label='funkce: y = 0.33')
        plt.title(nazev)
        plt.xlabel("Počet simulací hry")
        plt.ylabel("Procento vítězství")
        plt.legend(loc="upper right")
        plt.savefig(os.getcwd() + f"/outputs/{filename}.{fileformat}")
