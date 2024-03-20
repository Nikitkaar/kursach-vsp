import numpy as np
import matplotlib.pyplot as plt

k = [0.01338, 0.01338]
li = [55, -120, 230]
li_1 = [-230, -55, 120]

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
    highlight_y = [np.exp((-k[i] * np.abs(3 * np.pi / (4 * k[i])))) * (
    np.cos(k[i] * 3 * np.pi / (4 * k[i])) - np.sin(k[i] * np.abs(3 * np.pi / (4 * k[i])))),
    np.exp((-k[i] * np.abs(-3 * np.pi / (4 * k[i])))) * (
    np.cos(k[i] * -3 * np.pi / (4 * k[i])) - np.sin(k[i] * np.abs(-3 * np.pi / (4 * k[i]))) )]

    axes[i].scatter(highlight_x, highlight_y, color='none', edgecolors='blue', marker='o')

    for (x, y) in zip(highlight_x, highlight_y):
        axes[i].annotate('{:.3f}'.format(x), xy=(x, y), xytext=(5, -5), textcoords='offset points', fontsize=6, ha='left', va='top')

    if i == 0: # Добавляем метки точек на верхний график по li
        for point in li:
            axes[i].scatter(point, np.exp((-k[i] * np.abs(point))) * (np.cos(k[i] * point) + np.sin(k[i] * np.abs(point))), color='red', marker='o')
    else:
        for point in li_1: # Добавляем метки точек на нижний график по li_1
            axes[i].scatter(point, np.exp((-k[i] * np.abs(point))) * (np.cos(k[i] * point) + np.sin(k[i] * np.abs(point))), color='red', marker='o')

plt.subplots_adjust(hspace=20)

plt.tight_layout()
plt.savefig('ШПАЛА.pdf', format='pdf', bbox_inches='tight', pad_inches=0)
