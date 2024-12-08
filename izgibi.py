import numpy as np
import matplotlib.pyplot as plt


class Izgibi:

    g = ["Локомотив Прямая Зима", "Локомотив Кривая Лето", "Локомотив Прямая Лето", "Локомотив Кривая Зима", "Вагон Прямая Зима", "Вагон Кривая Лето", "Вагон Прямая Лето", "Вагон Кривая Зима"]
    def __init__(self, **kwargs):
        # Обработка переданных аргументов
        self.sostavs = kwargs.get('sostavs', None)  # Если sostavs не передан, будет None
        self.l_i_loc = kwargs.get("l_i_loco")
        self.l_i_vagon = kwargs.get("l_i_vagon")
        self.k = kwargs.get('k') * 2
        print(self.k)
        # Остальные атрибуты и их инициализация
        self.result = []

    def grafic_mader(self):
        print("начало кода функц график мэйдер ИЗГИБЫ")
        fig, axes = plt.subplots(8, 1, figsize=(8, 11), dpi=300)

        for i in range(len(self.k)):
            x = np.linspace(-550, 550, 1100)
            y = np.exp(-self.k[i] * np.abs(x)) * (np.cos(self.k[i] * x) - np.sin(self.k[i] * np.abs(x)))

            axes[i].plot(x, y, linewidth=0.5)
            axes[i].set_title('k = {:.5f}, {}'.format(self.k[i], self.g[i]), fontsize=8)
            axes[i].set_xlim(-550, 550)
            axes[i].set_ylim(-1, 1.5)
            axes[i].tick_params(labelsize=6)
            axes[i].invert_yaxis()

            axes[i].spines['left'].set_position(('data', 1.5))
            axes[i].spines['bottom'].set_position(('data', 0))
            axes[i].spines['top'].set_visible(False)
            axes[i].spines['right'].set_visible(False)

            self.highlight_x = [np.pi / (4 * self.k[i]), 5 * np.pi / (4 * self.k[i]), -np.pi / (4 * self.k[i]),
                                -5 * np.pi / (4 * self.k[i])]
            self.highlight_y = [
                np.exp(-self.k[i] * np.abs(val)) * (np.cos(self.k[i] * val) - np.sin(self.k[i] * np.abs(val)))
                for val in self.highlight_x
            ]

            # Отображение выделенных точек
            axes[i].scatter(self.highlight_x, self.highlight_y, color='none', edgecolors='blue', marker='o')

            # Добавление подписей к точкам
            for (x, y) in zip(self.highlight_x, self.highlight_y):
                axes[i].annotate(f'{x:.1f}', xy=(x, y), xytext=(-5, -7), textcoords='offset points', fontsize=6,
                                 ha='left', va='top')
                axes[i].annotate(f"\u03BC = 0", xy=(x, y), xytext=(5, -11), textcoords='offset points', fontsize=6,
                                 ha='left', va='top')

            # Обработка l_i для красных точек
            if self.sostavs is not None and len(self.sostavs) > i:
                if i < 4:
                    l_i = [sostav for sostav in self.sostavs[i].l_i if
                           sostav != 0]  # Для первых 4 графиков
                else:
                    l_i = [sostav for sostav in self.sostavs[i].l_i if
                           sostav != 0]  # Для последних 4 графиков

                if l_i:  # Если l_i содержит значения
                    x1 = l_i[0]
                    x2 = l_i[1] + l_i[0] if len(l_i) > 1 else l_i[0]
                    x3 = l_i[1] + l_i[2] + l_i[0] if len(l_i) > 2 else (l_i[0] + l_i[1] if len(l_i) == 2 else l_i[0])

                    # Эти координаты y для красных точек
                    lighthigh_x = [x1, x2, x3]
                    lighthigh_y = [np.exp(-self.k[i] * np.abs(x1)) * (np.cos(self.k[i] * x1) - np.sin(self.k[i] * np.abs(x1))),
                                   np.exp(-self.k[i] * np.abs(x2)) * (np.cos(self.k[i] * x2) - np.sin(self.k[i] * np.abs(x2))),
                                   np.exp(-self.k[i] * np.abs(x3)) * (np.cos(self.k[i] * x3) - np.sin(self.k[i] * np.abs(x3)))]

                    axes[i].scatter(lighthigh_x, lighthigh_y, color='red', marker='o', s=10)

                    # Добавление подписей к красным точкам
                    for x, y in zip(lighthigh_x, lighthigh_y):
                        axes[i].annotate(f"{x:.1f}  \u03BC = {y:.5f}", xy=(x, y), xytext=(-20, 9), textcoords='offset points',
                                         fontsize=4.8, ha='left', va='top')

        print('graf made for i in range самый конец кода кароч ИЗГИБЫ')

        plt.tight_layout()
        plt.savefig('ИЗГИБЫ.pdf', format='pdf', bbox_inches='tight', pad_inches=0)

