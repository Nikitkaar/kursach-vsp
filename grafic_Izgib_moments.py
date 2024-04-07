import numpy as np
import matplotlib.pyplot as plt

from main import k
from main import sostavs
g = ["Локомотив Прямая Лето", "Локомотив Прямая Зима", "Локомотив Кривая Лето", "Локомотив Кривая Зима", "Вагон Прямая Лето", "Вагон Прямая Зима", "Вагон Кривая Лето", "Вагон Кривая Зима"]
k = main.k * 2

def isser():
    result = []

    for sostav in main.sostavs:
        i = sostav.xm()
        if i != 0:
            result.append(i)

    # Удаление всех нулей из вложенных списков
    result = [[item for item in sublist if item != 0] for sublist in result]

    return result[0:7:4]


def isser_1():
    result = [
              [main.sostavs[0].Muu2(), main.sostavs[0].Muu3(), main.sostavs[0].Muu4()],
              [main.sostavs[1].Muu2(), main.sostavs[1].Muu3(), main.sostavs[1].Muu4()],
              [main.sostavs[2].Muu2(), main.sostavs[2].Muu3(), main.sostavs[2].Muu4()],
              [main.sostavs[3].Muu2(), main.sostavs[3].Muu3(), main.sostavs[3].Muu4()],
              [main.sostavs[4].Muu2(), main.sostavs[4].Muu3(), main.sostavs[4].Muu4()],
              [main.sostavs[5].Muu2(), main.sostavs[5].Muu3(), main.sostavs[5].Muu4()],
              [main.sostavs[6].Muu2(), main.sostavs[6].Muu3(), main.sostavs[6].Muu4()],
              [main.sostavs[7].Muu2(), main.sostavs[7].Muu3(), main.sostavs[7].Muu4()],
              ]
    # Удаление всех нулей из вложенных списков
    result = [[item for item in sublist if item != 0] for sublist in result]
    return result

fig, axes = plt.subplots(len(k), 1, figsize=(8, 11), dpi=300)

for i in range(len(k)):
    x = np.linspace(-550, 550, 1100)
    y = np.exp((-k[i] * np.abs(x))) * (np.cos(k[i] * x) - np.sin(k[i] * np.abs(x)))

    axes[i].plot(x, y, linewidth=0.5)
    axes[i].set_title('k = {:.5f}, {}'.format(k[i], g[i]), fontsize=8)
    axes[i].set_xlim(-550, 550)
    axes[i].set_ylim(-1, 1.5)
    axes[i].tick_params(labelsize=6)
    axes[i].invert_yaxis()
    axes[i].spines['left'].set_position(('data', 1.5))
    axes[i].spines['bottom'].set_position(('data', 0))
    axes[i].spines['top'].set_visible(False)  # Удаление верхней границы спайнов
    axes[i].spines['right'].set_visible(False)  # Удаление правой границы спайнов

    highlight_x = [np.pi / (4 * k[i]), 5 * np.pi / (4 * k[i]), -np.pi / (4 * k[i]), -5 * np.pi / (4 * k[i])]
    highlight_y = [np.exp((-k[i] * np.abs(np.pi / (4 * k[i])))) * (
            np.cos(k[i] * np.pi / (4 * k[i])) - np.sin(k[i] * np.abs(np.pi / (4 * k[i])))),
                   np.exp((-k[i] * np.abs(5 * np.pi / (4 * k[i])))) * (
                           np.cos(k[i] * 5 * np.pi / (4 * k[i])) - np.sin(
                       k[i] * np.abs(5 * np.pi / (4 * k[i])))),
                   np.exp((-k[i] * np.abs(-np.pi / (4 * k[i])))) * (
                           np.cos(k[i] * -np.pi / (4 * k[i])) - np.sin(k[i] * np.abs(-np.pi / (4 * k[i])))),
                   np.exp((-k[i] * np.abs(-5 * np.pi / (4 * k[i])))) * (
                           np.cos(k[i] * -5 * np.pi / (4 * k[i])) - np.sin(
                       k[i] * np.abs(-5 * np.pi / (4 * k[i]))))]
    axes[i].scatter(highlight_x, highlight_y, color='none', edgecolors='blue', marker='o')
    # Добавление подписей к точкам
    for (x, y) in zip(highlight_x, highlight_y):
        axes[i].annotate('{:.1f}'.format(x), xy=(x, y), xytext=(-5, -7), textcoords='offset points', fontsize=6,
                         ha='left', va='top')
        axes[i].annotate(f"\u03BC = 0".format(x), xy=(x, y), xytext=(5, -11), textcoords='offset points', fontsize=6,
                         ha='left', va='top')

    for i in range(0, 4):
        lighthigh_x = isser()[0]
        lighthigh_y = [0] * len(isser()[0])
        axes[i].scatter(lighthigh_x, lighthigh_y, color='red', marker='o', s=10)

        # Добавление подписей к точкам
        for (x, y) in zip(lighthigh_x, lighthigh_y):
            axes[i].annotate(f"{x:.1f}     \u03BC = {np.exp((-k[i] * np.abs(x))) * (np.cos(k[i] * x) - np.sin(k[i] * np.abs(x))):.5f}", xy=(x, y), xytext=(-20, 9), textcoords='offset points', fontsize=4.8,
                             ha='left', va='top')

    for i in range(4, 8):
        lighthigh_x = isser()[1]
        lighthigh_y = [0] * len(isser()[1])
        axes[i].scatter(lighthigh_x, lighthigh_y, color='red', marker='o', s=10)

        # Добавление подписей к точкам
        for (x, y) in zip(lighthigh_x, lighthigh_y):
            axes[i].annotate(f"{x:.1f}     \u03BC = {np.exp((-k[i] * np.abs(x))) * (np.cos(k[i] * x) - np.sin(k[i] * np.abs(x))):.5f}", xy=(x, y), xytext=(-20, 9), textcoords='offset points', fontsize=4.8,
                             ha='left', va='top')

plt.tight_layout()
plt.savefig('ИЗГИБЫ.pdf', format='pdf', bbox_inches='tight', pad_inches=0)
