import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


class Shpala:

    def __init__(self, **kwargs):
        # Обработка переданных аргументов
        self.sostavs = kwargs.get('sostavs', None)  # Если sostavs не передан, будет None
        self.k = self.sostavs.k
        # Остальные атрибуты и их инициализация

    def summa_l_0(self):
        """Расстояния от колесных пар до 1-ой шпалы."""
        if self.sostavs.RaschetnayaOS_N() == 1 or self.sostavs.n == 2:
            if self.sostavs.n == 4:
                return [55, self.sostavs.l_i[0] + 55, self.sostavs.l_i[0] + self.sostavs.l_i[1] + 55,
                        self.sostavs.l_i[0] + self.sostavs.l_i[1] + self.sostavs.l_i[2] + 55]
            elif self.sostavs.n == 3:
                return [55, self.sostavs.l_i[0] + 55, self.sostavs.l_i[0] + self.sostavs.l_i[1] + 55]
            else:
                return [55, self.sostavs.l_i[0] + 55]
        else:
            if self.sostavs.n == 4:
                return [-self.sostavs.l_i[0] + 55, 55, self.sostavs.l_i[1] + 55,
                        self.sostavs.l_i[1] + self.sostavs.l_i[2] + 55]
            else:
                return [-self.sostavs.l_i[0] + 55, 55, self.sostavs.l_i[1] + 55]

    def summa_l_1(self):
        """Расстояния от колесных пар до 3-ей шпалы."""
        if self.sostavs.RaschetnayaOS_N() == 1 or self.sostavs.n == 2:
            if self.sostavs.n == 4:
                return [-55, self.sostavs.l_i[0] - 55, self.sostavs.l_i[0] + self.sostavs.l_i[1] - 55,
                        self.sostavs.l_i[0] + self.sostavs.l_i[1] + self.sostavs.l_i[2] - 55]
            elif self.sostavs.n == 3:
                return [-55, self.sostavs.l_i[0] - 55, self.sostavs.l_i[0] + self.sostavs.l_i[1] - 55]
            else:
                return [-55, self.sostavs.l_i[0] - 55]
        else:
            if self.sostavs.n == 4:
                return [-self.sostavs.l_i[0] - 55, -55, self.sostavs.l_i[1] - 55,
                        self.sostavs.l_i[1] + self.sostavs.l_i[2] - 55]
            else:
                return [-self.sostavs.l_i[0] - 55, -55, self.sostavs.l_i[1] - 55]

    def grafic(self):
        fig, axes = plt.subplots(2, 1, figsize=(8, 6), dpi=300)

        for i in range(2):
            x = np.linspace(-500, 500, 1000)
            y = np.exp((-self.k * np.abs(x))) * (np.cos(self.k * x) + np.sin(self.k * np.abs(x)))

            axes[i].plot(x, y, linewidth=0.5)
            axes[i].set_title('k = {:.5f}'.format(self.k), fontsize=8)
            axes[i].set_xlim(-400, 450)
            axes[i].set_ylim(-1, 1.5)
            axes[i].tick_params(labelsize=6)
            axes[i].invert_yaxis()
            axes[i].spines['left'].set_position(('data', 1.5))
            axes[i].spines['bottom'].set_position(('data', 0))
            axes[i].spines['top'].set_visible(False)
            axes[i].spines['right'].set_visible(False)

            highlight_x = [3 * np.pi / (4 * self.k), -3 * np.pi / (4 * self.k)]
            highlight_y = [0, 0]

            axes[i].scatter(highlight_x, highlight_y, color='none', edgecolors='blue', marker='o')

            for (x, y) in zip(highlight_x, highlight_y):
                axes[i].annotate(f'{x:.1f}     \u03B7 = 0', xy=(x, y), xytext=(-15, 15), textcoords='offset points',
                                 fontsize=6, ha='left', va='top')

            if i == 0:  # Для первого графика
                lighthigh_x = self.summa_l_0()
                lighthigh_y = [0] * len(lighthigh_x)
                axes[i].scatter(lighthigh_x, lighthigh_y, color='red', marker='o', s=10)
                axes[i].scatter(lighthigh_x, [x - 0.7 for x in lighthigh_y], color='None', edgecolors='blue',
                                marker='o',
                                s=1000)
                for (x, y) in zip(lighthigh_x, lighthigh_y):
                    axes[i].annotate(
                        f"{x:.1f}     \u03B7 = {np.exp((-self.k * np.abs(x))) * (np.cos(self.k * x) + np.sin(self.k * np.abs(x))):.5f}",
                        xy=(x, y), xytext=(-20, -3), textcoords='offset points', fontsize=4.8,
                        ha='left', va='top')
                # Добавление прямоугольников
                rect1 = Rectangle((-13.8, 0), 27.6, -0.15, edgecolor='r', facecolor='none')
                rect2 = Rectangle((55 - (55 / 4), 0), 27.6, -0.15, edgecolor='b', facecolor='none')
                rect3 = Rectangle((110 - (55 / 4), 0), 27.6, -0.15, edgecolor='b', facecolor='none')
                axes[i].add_patch(rect1)
                axes[i].add_patch(rect2)
                axes[i].add_patch(rect3)

            if i == 1:  # Для второго графика
                lighthigh_x = self.summa_l_1()
                lighthigh_y = [0] * len(lighthigh_x)
                axes[i].scatter(lighthigh_x, lighthigh_y, color='red', marker='o', s=10)
                axes[i].scatter(lighthigh_x, [x - 0.7 for x in lighthigh_y], color='None', edgecolors='blue',
                                marker='o',
                                s=1000)
                for (x, y) in zip(lighthigh_x, lighthigh_y):
                    axes[i].annotate(
                        f"{x:.1f}     \u03B7 = {np.exp((-self.k * np.abs(x))) * (np.cos(self.k * x) + np.sin(self.k * np.abs(x))):.5f}",
                        xy=(x, y), xytext=(-20, -3), textcoords='offset points', fontsize=4.8,
                        ha='left', va='top')
                # Добавление прямоугольников
                rect1 = Rectangle((-13.8, 0), 27.6, -0.15, edgecolor='r', facecolor='none')
                rect2 = Rectangle((-55 + (55 / 4), 0), -27.6, -0.15, edgecolor='b', facecolor='none')
                rect3 = Rectangle((-110 + (55 / 4), 0), -27.6, -0.15, edgecolor='b', facecolor='none')
                axes[i].add_patch(rect1)
                axes[i].add_patch(rect2)
                axes[i].add_patch(rect3)

        plt.subplots_adjust(hspace=0.5)
        plt.savefig("my_plot.pdf")  # Сохраните график после его построения
