import numpy as np
import matplotlib.pyplot as plt


class Grafics_progibov:

    def __init__(self, **kwargs):
        # Обработка переданных аргументов
        self.sostavs = kwargs.get('sostavs', None)  # Если sostavs не передан, будет None
        self.k = kwargs.get('k', None)  # Если sostavs не передан, будет None
        self.g = ["Локомотив Прямая Лето", "Локомотив Прямая Зима", "Локомотив Кривая Лето", "Локомотив Кривая Зима", "Вагон Прямая Лето", "Вагон Прямая Зима", "Вагон Кривая Лето", "Вагон Кривая Зима"]
        # Остальные атрибуты и их инициализация


    def isser(self):
        result = []

        for sostav in self.sostavs:
            i = sostav.xn()
            if i != 0:
                result.append(i)

        # Удаление всех нулей из вложенных списков
        result = [[item for item in sublist if item != 0] for sublist in result]

        return result
    def grafic_mader(self):
        fig, axes = plt.subplots(8, 1, figsize=(8, 11), dpi=300)

        for i in range(8):
            x = np.linspace(-550, 550, 1100)
            y = np.exp((-self.sostavs[i].k * np.abs(x))) * (np.cos(self.sostavs[i].k * x) + np.sin(self.sostavs[i].k * np.abs(x)))

            axes[i].plot(x, y, linewidth=0.5)
            axes[i].plot(x, y, linewidth=0.5)
            axes[i].set_title('k = {:.5f}, {}'.format(self.sostavs[i].k, self.g[i]), fontsize=8)
            axes[i].set_xlim(-550, 550)
            axes[i].set_ylim(-1, 1.5)
            axes[i].tick_params(labelsize=6)
            axes[i].invert_yaxis()
            axes[i].spines['left'].set_position(('data', 1.5))
            axes[i].spines['bottom'].set_position(('data', 0))
            axes[i].spines['top'].set_visible(False) # Удаление верхней границы спайнов
            axes[i].spines['right'].set_visible(False) # Удаление правой границы спайнов

            # Отметка точек на графике
            highlight_x = [3 * np.pi / (4 * self.sostavs[i].k), -3 * np.pi / (4 * self.sostavs[i].k)]
            highlight_y = [np.exp((-self.sostavs[i].k * np.abs(3 * np.pi / (4 * self.sostavs[i].k)))) * (
                        np.cos(self.sostavs[i].k * 3 * np.pi / (4 * self.sostavs[i].k)) - np.sin(self.sostavs[i].k * np.abs(3 * np.pi / (4 * self.sostavs[i].k)))),
                           np.exp((-self.sostavs[i].k * np.abs(-3 * np.pi / (4 * self.sostavs[i].k)))) * (
                                       np.cos(self.sostavs[i].k * -3 * np.pi / (4 * self.sostavs[i].k)) - np.sin(self.sostavs[i].k * np.abs(-3 * np.pi / (4 * self.sostavs[i].k))))]

            axes[i].scatter(highlight_x, highlight_y, color='none', edgecolors='blue', marker='o')

        # Добавление подписей к точкам
            for (x, y) in zip(highlight_x, highlight_y):
                axes[i].annotate(f"{x:.1f} \u03B7 = 0", xy=(x, y), xytext=(5, 9), textcoords='offset points', fontsize=6,
                                 ha='left', va='top')

            for i in range(0,1):
                lighthigh_x = self.isser()[0]
                if self.sostavs[0].RaschetnayaOS_N() == 2:
                    lighthigh_x[0] = -lighthigh_x[0]
                lighthigh_y = [0] * len(self.isser()[0])
                axes[i].scatter(lighthigh_x, lighthigh_y, color='red', marker='o', s=10)

                # Добавление подписей к точкам
                for (x, y) in zip(lighthigh_x, lighthigh_y):
                    axes[i].annotate(f"{x:.1f}     \u03B7 = {np.exp((-self.sostavs[i].k * np.abs(x))) * (np.cos(self.sostavs[i].k * x) + np.sin(self.sostavs[i].k * np.abs(x))):.5f}", xy=(x, y), xytext=(-20, -3), textcoords='offset points', fontsize=4.8,
                                     ha='left', va='top')

            for i in range(1,2):
                lighthigh_x = self.isser()[1]
                if self.sostavs[1].RaschetnayaOS_N() == 2:
                    lighthigh_x[0] = -lighthigh_x[0]
                lighthigh_y = [0] * len(self.isser()[1])
                axes[i].scatter(lighthigh_x, lighthigh_y, color='red', marker='o', s=10)

                # Добавление подписей к точкам
                for (x, y) in zip(lighthigh_x, lighthigh_y):
                    axes[i].annotate(f"{x:.1f}     \u03B7 = {np.exp((-self.sostavs[i].k * np.abs(x))) * (np.cos(self.sostavs[i].k * x) + np.sin(self.sostavs[i].k * np.abs(x))):.5f}", xy=(x, y), xytext=(-20, -3), textcoords='offset points', fontsize=4.8,
                                     ha='left', va='top')

            for i in range(2, 3):
                lighthigh_x = self.isser()[2]
                if self.sostavs[2].RaschetnayaOS_N() == 2:
                    lighthigh_x[0] = -lighthigh_x[0]
                lighthigh_y = [0] * len(self.isser()[2])
                axes[i].scatter(lighthigh_x, lighthigh_y, color='red', marker='o', s=10)

                # Добавление подписей к точкам
                for (x, y) in zip(lighthigh_x, lighthigh_y):
                    axes[i].annotate(f"{x:.1f}     \u03B7 = {np.exp((-self.sostavs[i].k * np.abs(x))) * (np.cos(self.sostavs[i].k * x) + np.sin(self.sostavs[i].k * np.abs(x))):.5f}", xy=(x, y), xytext=(-20, -3), textcoords='offset points', fontsize=4.8,
                                     ha='left', va='top')

            for i in range(3, 4):
                lighthigh_x = self.isser()[3]
                if self.sostavs[3].RaschetnayaOS_N() == 2:
                    lighthigh_x[0] = -lighthigh_x[0]
                lighthigh_y = [0] * len(self.isser()[3])
                axes[i].scatter(lighthigh_x, lighthigh_y, color='red', marker='o', s=10)

                # Добавление подписей к точкам
                for (x, y) in zip(lighthigh_x, lighthigh_y):
                    axes[i].annotate(f"{x:.1f}     \u03B7 = {np.exp((-self.sostavs[i].k * np.abs(x))) * (np.cos(self.sostavs[i].k * x) + np.sin(self.sostavs[i].k * np.abs(x))):.5f}", xy=(x, y), xytext=(-20, -3), textcoords='offset points', fontsize=4.8,
                                     ha='left', va='top')

            for i in range(4, 5):
                lighthigh_x = self.isser()[4]
                if self.sostavs[4].RaschetnayaOS_N() == 2:
                    lighthigh_x[0] = -lighthigh_x[0]
                lighthigh_y = [0] * len(self.isser()[4])
                axes[i].scatter(lighthigh_x, lighthigh_y, color='red', marker='o', s=10)

                # Добавление подписей к точкам
                for (x, y) in zip(lighthigh_x, lighthigh_y):
                    axes[i].annotate(
                        f"{x:.1f}     \u03B7 = {np.exp((-self.sostavs[i].k * np.abs(x))) * (np.cos(self.sostavs[i].k * x) + np.sin(self.sostavs[i].k * np.abs(x))):.5f}",
                        xy=(x, y), xytext=(-20, -3), textcoords='offset points', fontsize=4.8,
                        ha='left', va='top')

            for i in range(5, 6):
                lighthigh_x = self.isser()[5]
                if self.sostavs[5].RaschetnayaOS_N() == 2:
                    lighthigh_x[0] = -lighthigh_x[0]
                lighthigh_y = [0] * len(self.isser()[5])
                axes[i].scatter(lighthigh_x, lighthigh_y, color='red', marker='o', s=10)

                # Добавление подписей к точкам
                for (x, y) in zip(lighthigh_x, lighthigh_y):
                    axes[i].annotate(
                        f"{x:.1f}     \u03B7 = {np.exp((-self.sostavs[i].k * np.abs(x))) * (np.cos(self.sostavs[i].k * x) + np.sin(self.sostavs[i].k * np.abs(x))):.5f}",
                        xy=(x, y), xytext=(-20, 9), textcoords='offset points', fontsize=4.8,
                        ha='left', va='top')

            for i in range(6, 7):
                lighthigh_x = self.isser()[6]
                if self.sostavs[6].RaschetnayaOS_N() == 2:
                    lighthigh_x[0] = -lighthigh_x[0]
                lighthigh_y = [0] * len(self.isser()[6])
                axes[i].scatter(lighthigh_x, lighthigh_y, color='red', marker='o', s=10)

                # Добавление подписей к точкам
                for (x, y) in zip(lighthigh_x, lighthigh_y):
                    axes[i].annotate(
                        f"{x:.1f}     \u03B7 = {np.exp((-self.sostavs[i].k * np.abs(x))) * (np.cos(self.sostavs[i].k * x) + np.sin(self.sostavs[i].k * np.abs(x))):.5f}",
                        xy=(x, y), xytext=(-20, -3), textcoords='offset points', fontsize=4.8,
                        ha='left', va='top')

            for i in range(7, 8):
                lighthigh_x = self.isser()[7]
                if self.sostavs[7].RaschetnayaOS_N() == 2:
                    lighthigh_x[0] = -lighthigh_x[0]
                lighthigh_y = [0] * len(self.isser()[7])
                axes[i].scatter(lighthigh_x, lighthigh_y, color='red', marker='o', s=10)

                # Добавление подписей к точкам
                for (x, y) in zip(lighthigh_x, lighthigh_y):
                    axes[i].annotate(
                        f"{x:.1f}     \u03B7 = {np.exp((-self.sostavs[i].k * np.abs(x))) * (np.cos(self.sostavs[i].k * x) - np.sin(self.sostavs[i].k * np.abs(x))):.5f}",
                        xy=(x, y), xytext=(-20, -3), textcoords='offset points', fontsize=4.8,
                        ha='left', va='top')

        plt.tight_layout()
        plt.savefig('ПРОГИБЫ.pdf', format='pdf', bbox_inches='tight', pad_inches=0)

