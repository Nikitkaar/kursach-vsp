import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import main

k = [main.k[2], main.k[2]]

def summa_l_0():
    """Расстояния от колесных пар до 1-ой шпалы."""
    if main.sostavs[4].RaschetnayaOS_N() == 1 or main.sostavs[4].n == 2:
        if main.sostavs[4].n == 4:
            return [55, main.sostavs[4].l_i[0] + 55, main.sostavs[4].l_i[0] + main.sostavs[4].l_i[1] + 55, main.sostavs[4].l_i[0] + main.sostavs[4].l_i[1] + main.sostavs[4].l_i[2] + 55]
        elif main.sostavs[4].n == 3:
            return [55, main.sostavs[4].l_i[0] + 55, main.sostavs[4].l_i[0] + main.sostavs[4].l_i[1] + 55]
        else:
            return [55, main.sostavs[4].l_i[0] + 55]
    else:
        if main.sostavs[4].n == 4:
            return [-main.sostavs[4].l_i[0] + 55, 55, main.sostavs[4].l_i[1] + 55, main.sostavs[4].l_i[1] + main.sostavs[4].l_i[2] + 55]
        else:
            return [-main.sostavs[4].l_i[0] + 55, 55, main.sostavs[4].l_i[1] + 55]


def summa_l_1():
    """Расстояния от колесных пар до 3-ей шпалы."""
    if main.sostavs[4].RaschetnayaOS_N() == 1 or main.sostavs[4].n == 2:
        if main.sostavs[4].n == 4:
            return [-55, main.sostavs[4].l_i[0] - 55, main.sostavs[4].l_i[0] + main.sostavs[4].l_i[1] - 55, main.sostavs[4].l_i[0] + main.sostavs[4].l_i[1] + main.sostavs[4].l_i[2] - 55]
        elif main.sostavs[4].n == 3:
            return [-55, main.sostavs[4].l_i[0] - 55, main.sostavs[4].l_i[0] + main.sostavs[4].l_i[1] - 55]
        else:
            return [-55, main.sostavs[4].l_i[0] - 55]
    else:
        if main.sostavs[4].n == 4:
            return [-main.sostavs[4].l_i[0] - 55, -55, main.sostavs[4].l_i[1] - 55, main.sostavs[4].l_i[1] + main.sostavs[4].l_i[2] - 55]
        else:
            return [-main.sostavs[4].l_i[0] - 55, -55, main.sostavs[4].l_i[1] - 55]

li = summa_l_0()
li_1 = summa_l_1()

fig, axes = plt.subplots(len(k), 1, figsize=(8, 6), dpi=300)

for i in range(len(k)):
    x = np.linspace(-500, 500, 1000)
    y = np.exp((-k[i] * np.abs(x))) * (np.cos(k[i] * x) + np.sin(k[i] * np.abs(x)))

    axes[i].plot(x, y, linewidth=0.5)
    axes[i].set_title('k = {:.5f}'.format(k[i]), fontsize=8)
    axes[i].set_xlim(-400, 450)
    axes[i].set_ylim(-1, 1.5)
    axes[i].tick_params(labelsize=6)
    axes[i].invert_yaxis()
    axes[i].spines['left'].set_position(('data', 1.5))
    axes[i].spines['bottom'].set_position(('data', 0))
    axes[i].spines['top'].set_visible(False)
    axes[i].spines['right'].set_visible(False)

    highlight_x = [3 * np.pi / (4 * k[i]), -3 * np.pi / (4 * k[i])]
    highlight_y = [0, 0]

    axes[i].scatter(highlight_x, highlight_y, color='none', edgecolors='blue', marker='o')

    for (x, y) in zip(highlight_x, highlight_y):
        axes[i].annotate(f'{x:.1f}     \u03B7 = 0', xy=(x, y), xytext=(-15, 15), textcoords='offset points', fontsize=6, ha='left', va='top')

    for i in range(0, 1):
        lighthigh_x = summa_l_0()
        lighthigh_y = [0] * len(lighthigh_x)
        axes[i].scatter(lighthigh_x, lighthigh_y, color='red', marker='o', s=10)
        axes[i].scatter(lighthigh_x, [x - 0.7 for x in lighthigh_y], color='None', edgecolors = 'blue', marker='o', s=1000)
        # Добавление подписей к точкам
        for (x, y) in zip(lighthigh_x, lighthigh_y):
            axes[i].annotate(f"{x:.1f}     \u03B7 = {np.exp((-k[i] * np.abs(x))) * (np.cos(k[i] * x) + np.sin(k[i] * np.abs(x))):.5f}", xy=(x, y), xytext=(-20, -3), textcoords='offset points', fontsize=4.8,
                             ha='left', va='top')
        # Создаем и добавляем прямоугольники на график
        rect1 = Rectangle((-13.8, 0), 27.6, -0.15, edgecolor='r', facecolor='none')  # Прямоугольник с шириной 2 и высотой 3
        rect2 = Rectangle((55-(55/4), 0), 27.6, -0.15, edgecolor='b', facecolor='none')  # Прямоугольник с шириной 1 и высотой 2
        rect3 = Rectangle((110-(55/4), 0), 27.6, -0.15, edgecolor='b', facecolor='none')  # Прямоугольник с шириной 1 и высотой 2
        axes[i].add_patch(rect1)
        axes[i].add_patch(rect2)
        axes[i].add_patch(rect3)
    for i in range(1, 2):
        lighthigh_x = summa_l_1()
        lighthigh_y = [0] * len(lighthigh_x)
        axes[i].scatter(lighthigh_x, lighthigh_y, color='red', marker='o', s=10)
        axes[i].scatter(lighthigh_x, [x - 0.7 for x in lighthigh_y], color='None', edgecolors = 'blue', marker='o', s=1000)
        # Создаем и добавляем прямоугольники на график
        rect1 = Rectangle((-13.8, 0), 27.6, -0.15, edgecolor='r', facecolor='none')  # Прямоугольник с шириной 2 и высотой 3
        rect2 = Rectangle((-55+(55/4), 0), -27.6, -0.15, edgecolor='b', facecolor='none')  # Прямоугольник с шириной 1 и высотой 2
        rect3 = Rectangle((-110+(55/4), 0), -27.6, -0.15, edgecolor='b', facecolor='none')  # Прямоугольник с шириной 1 и высотой 2
        axes[i].add_patch(rect1)
        axes[i].add_patch(rect2)
        axes[i].add_patch(rect3)
        # Добавление подписей к точкам
        for (x, y) in zip(lighthigh_x, lighthigh_y):
            axes[i].annotate(f"{x:.1f}     \u03B7 = {np.exp((-k[i] * np.abs(x))) * (np.cos(k[i] * x) + np.sin(k[i] * np.abs(x))):.5f}",
            xy=(x, y), xytext=(-20, -3), textcoords='offset points', fontsize=4.8,
            ha='left', va='top')
plt.subplots_adjust(hspace=20)

plt.tight_layout()
plt.savefig('ШПАЛА.pdf', format='pdf', bbox_inches='tight', pad_inches=0)

