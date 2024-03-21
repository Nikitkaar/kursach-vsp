import numpy as np
import matplotlib.pyplot as plt

g = ["Локомотив Прямая Лето", "Локомотив Прямая Зима", "Локомотив Кривая Лето", "Локомотив Кривая Зима", "Вагон Прямая Лето", "Вагон Прямая Зима", "Вагон Кривая Лето", "Вагон Кривая Зима"]
k = [0.01338, 0.015163, 0.01421, 0.0154096, 0.01338, 0.015163, 0.01421, 0.0154096]

fig, axes = plt.subplots(len(k), 1, figsize=(8, 11), dpi=300)

for i in range(len(k)):
    x = np.linspace(-500, 500, 1000)
    y = np.exp((-k[i] * np.abs(x))) * (np.cos(k[i] * x) + np.sin(k[i] * np.abs(x)))

    axes[i].plot(x, y, linewidth=0.5)
    axes[i].plot(x, y, linewidth=0.5)
    axes[i].set_title('k = {:.5f}, {}'.format(k[i], g[i]), fontsize=8)
    axes[i].set_xlim(-500, 500)
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
        axes[i].annotate('{:.1f}'.format(x), xy=(x, y), xytext=(-5, -11), textcoords='offset points', fontsize=6, ha='left', va='top')
        axes[i].annotate(f"\u03B7 = 0".format(x), xy=(x, y), xytext=(5, 9), textcoords='offset points', fontsize=6,
                         ha='left', va='top')
plt.tight_layout()
plt.savefig('ПРОГИБЫ.pdf', format='pdf', bbox_inches='tight', pad_inches=0)
