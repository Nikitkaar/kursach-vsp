import matplotlib.pyplot as plt
import numpy as np


class GrafVerTemp:
    def __init__(self, **kwargs):

        self.t_y = kwargs.get('t_y')
        self.t_max_max = kwargs.get('t_max_max', None)
        self.t_min_min = kwargs.get('t_min_min', None)
        self.t_max_zakr = kwargs.get('t_max_zakr', None)
        self.t_min_zakr = kwargs.get('t_min_zakr', None)
        self.delta_t_p = kwargs.get('delta_t_p', None)

    def grafic_maker_(self):
        # Создаем фигуру и ось
        plt.clf()
        # Define the data
        x = np.linspace(self.t_min_min, self.t_max_max, 100)
        y = np.exp(-(x**2)/(2*(10**2)))

        # Create the plot
        plt.plot(x, y)

        # Set the title of the plot
        plt.title("График плотности вероятности распределения температуры рельса в годичном цикле")

        # Set the labels for the x and y axes
        plt.xlabel("t℃")
        plt.ylabel("Вероятность распределения")

        # Add grid lines
        plt.grid(True)

        # Show the plot
        plt.savefig('График оптимальной температуры.pdf', format='pdf', bbox_inches='tight', pad_inches=0)

