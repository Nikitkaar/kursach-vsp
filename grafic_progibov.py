import numpy as np
import matplotlib.pyplot as plt
import main

g = ["Локомотив Прямая Лето", "Локомотив Прямая Зима", "Локомотив Кривая Лето", "Локомотив Кривая Зима", "Вагон Прямая Лето", "Вагон Прямая Зима", "Вагон Кривая Лето", "Вагон Кривая Зима"]
k = main.k * 2

def isser():
    result = []

    for sostav in main.sostavs:
        i = sostav.xn()
        if i != 0:
            result.append(i)

    # Удаление всех нулей из вложенных списков
    result = [[item for item in sublist if item != 0] for sublist in result]

    return result

fig, axes = plt.subplots(len(k), 1, figsize=(8, 11), dpi=300)

for i in range(len(k)):
    x = np.linspace(-550, 550, 1100)
    y = np.exp((-k[i] * np.abs(x))) * (np.cos(k[i] * x) + np.sin(k[i] * np.abs(x)))

    axes[i].plot(x, y, linewidth=0.5)
    axes[i].plot(x, y, linewidth=0.5)
    axes[i].set_title('k = {:.5f}, {}'.format(k[i], g[i]), fontsize=8)
    axes[i].set_xlim(-550, 550)
    axes[i].set_ylim(-1, 1.5)
    axes[i].tick_params(labelsize=6)
    axes[i].invert_yaxis()
    axes[i].spines['left'].set_position(('data', 1.5))
    axes[i].spines['bottom'].set_position(('data', 0))
    axes[i].spines['top'].set_visible(False) # Удаление верхней границы спайнов
    axes[i].spines['right'].set_visible(False) # Удаление правой границы спайнов

    # Отметка точек на графике
    highlight_x = [3 * np.pi / (4 * k[i]), -3 * np.pi / (4 * k[i])]
    highlight_y = [np.exp((-k[i] * np.abs(3 * np.pi / (4 * k[i])))) * (
                np.cos(k[i] * 3 * np.pi / (4 * k[i])) - np.sin(k[i] * np.abs(3 * np.pi / (4 * k[i])))),
                   np.exp((-k[i] * np.abs(-3 * np.pi / (4 * k[i])))) * (
                               np.cos(k[i] * -3 * np.pi / (4 * k[i])) - np.sin(k[i] * np.abs(-3 * np.pi / (4 * k[i]))))]

    axes[i].scatter(highlight_x, highlight_y, color='none', edgecolors='blue', marker='o')

# Добавление подписей к точкам
    for (x, y) in zip(highlight_x, highlight_y):
        axes[i].annotate(f"{x:.1f} \u03B7 = 0", xy=(x, y), xytext=(5, 9), textcoords='offset points', fontsize=6,
                         ha='left', va='top')

    for i in range(0,1):
        lighthigh_x = isser()[0]
        if main.sostavs[0].RaschetnayaOS_N() == 2:
            lighthigh_x[0] = -lighthigh_x[0]
        lighthigh_y = [0] * len(isser()[0])
        axes[i].scatter(lighthigh_x, lighthigh_y, color='red', marker='o', s=10)

        # Добавление подписей к точкам
        for (x, y) in zip(lighthigh_x, lighthigh_y):
            axes[i].annotate(f"{x:.1f}     \u03B7 = {np.exp((-k[i] * np.abs(x))) * (np.cos(k[i] * x) + np.sin(k[i] * np.abs(x))):.5f}", xy=(x, y), xytext=(-20, -3), textcoords='offset points', fontsize=4.8,
                             ha='left', va='top')

    for i in range(1,2):
        lighthigh_x = isser()[1]
        if main.sostavs[1].RaschetnayaOS_N() == 2:
            lighthigh_x[0] = -lighthigh_x[0]
        lighthigh_y = [0] * len(isser()[1])
        axes[i].scatter(lighthigh_x, lighthigh_y, color='red', marker='o', s=10)

        # Добавление подписей к точкам
        for (x, y) in zip(lighthigh_x, lighthigh_y):
            axes[i].annotate(f"{x:.1f}     \u03B7 = {np.exp((-k[i] * np.abs(x))) * (np.cos(k[i] * x) + np.sin(k[i] * np.abs(x))):.5f}", xy=(x, y), xytext=(-20, -3), textcoords='offset points', fontsize=4.8,
                             ha='left', va='top')

    for i in range(2,3):
        lighthigh_x = isser()[2]
        if main.sostavs[2].RaschetnayaOS_N() == 2:
            lighthigh_x[0] = -lighthigh_x[0]
        lighthigh_y = [0] * len(isser()[2])
        axes[i].scatter(lighthigh_x, lighthigh_y, color='red', marker='o', s=10)

        # Добавление подписей к точкам
        for (x, y) in zip(lighthigh_x, lighthigh_y):
            axes[i].annotate(f"{x:.1f}     \u03B7 = {np.exp((-k[i] * np.abs(x))) * (np.cos(k[i] * x) + np.sin(k[i] * np.abs(x))):.5f}", xy=(x, y), xytext=(-20, -3), textcoords='offset points', fontsize=4.8,
                             ha='left', va='top')

    for i in range(3,4):
        lighthigh_x = isser()[3]
        if main.sostavs[3].RaschetnayaOS_N() == 2:
            lighthigh_x[0] = -lighthigh_x[0]
        lighthigh_y = [0] * len(isser()[3])
        axes[i].scatter(lighthigh_x, lighthigh_y, color='red', marker='o', s=10)

        # Добавление подписей к точкам
        for (x, y) in zip(lighthigh_x, lighthigh_y):
            axes[i].annotate(f"{x:.1f}     \u03B7 = {np.exp((-k[i] * np.abs(x))) * (np.cos(k[i] * x) + np.sin(k[i] * np.abs(x))):.5f}", xy=(x, y), xytext=(-20, -3), textcoords='offset points', fontsize=4.8,
                             ha='left', va='top')

    for i in range(4,5):
        lighthigh_x = isser()[4]
        if main.sostavs[4].RaschetnayaOS_N() == 2:
            lighthigh_x[0] = -lighthigh_x[0]
        lighthigh_y = [0] * len(isser()[4])
        axes[i].scatter(lighthigh_x, lighthigh_y, color='red', marker='o', s=10)

        # Добавление подписей к точкам
        for (x, y) in zip(lighthigh_x, lighthigh_y):
            axes[i].annotate(
                f"{x:.1f}     \u03B7 = {np.exp((-k[i] * np.abs(x))) * (np.cos(k[i] * x) + np.sin(k[i] * np.abs(x))):.5f}",
                xy=(x, y), xytext=(-20, -3), textcoords='offset points', fontsize=4.8,
                ha='left', va='top')

    for i in range(5,6):
        lighthigh_x = isser()[5]
        if main.sostavs[5].RaschetnayaOS_N() == 2:
            lighthigh_x[0] = -lighthigh_x[0]
        lighthigh_y = [0] * len(isser()[5])
        axes[i].scatter(lighthigh_x, lighthigh_y, color='red', marker='o', s=10)

        # Добавление подписей к точкам
        for (x, y) in zip(lighthigh_x, lighthigh_y):
            axes[i].annotate(
                f"{x:.1f}     \u03B7 = {np.exp((-k[i] * np.abs(x))) * (np.cos(k[i] * x) + np.sin(k[i] * np.abs(x))):.5f}",
                xy=(x, y), xytext=(-20, 9), textcoords='offset points', fontsize=4.8,
                ha='left', va='top')

    for i in range(6,7):
        lighthigh_x = isser()[6]
        if main.sostavs[6].RaschetnayaOS_N() == 2:
            lighthigh_x[0] = -lighthigh_x[0]
        lighthigh_y = [0] * len(isser()[6])
        axes[i].scatter(lighthigh_x, lighthigh_y, color='red', marker='o', s=10)

        # Добавление подписей к точкам
        for (x, y) in zip(lighthigh_x, lighthigh_y):
            axes[i].annotate(
                f"{x:.1f}     \u03B7 = {np.exp((-k[i] * np.abs(x))) * (np.cos(k[i] * x) + np.sin(k[i] * np.abs(x))):.5f}",
                xy=(x, y), xytext=(-20, -3), textcoords='offset points', fontsize=4.8,
                ha='left', va='top')

    for i in range(7,8):
        lighthigh_x = isser()[7]
        if main.sostavs[7].RaschetnayaOS_N() == 2:
            lighthigh_x[0] = -lighthigh_x[0]
        lighthigh_y = [0] * len(isser()[7])
        axes[i].scatter(lighthigh_x, lighthigh_y, color='red', marker='o', s=10)

        # Добавление подписей к точкам
        for (x, y) in zip(lighthigh_x, lighthigh_y):
            axes[i].annotate(
                f"{x:.1f}     \u03B7 = {np.exp((-k[i] * np.abs(x))) * (np.cos(k[i] * x) + np.sin(k[i] * np.abs(x))):.5f}",
                xy=(x, y), xytext=(-20, -3), textcoords='offset points', fontsize=4.8,
                ha='left', va='top')

plt.tight_layout()
plt.savefig('ПРОГИБЫ.pdf', format='pdf', bbox_inches='tight', pad_inches=0)
