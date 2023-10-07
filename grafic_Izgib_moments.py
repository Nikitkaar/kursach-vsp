import numpy as np
import matplotlib.pyplot as plt

k = [0.02323, 0.01536, 0.02276, 0.01578, 0.01536, 0.01245, 0.01987, 0.02134] # Заданные значения k

fig, axes = plt.subplots(len(k), 1, figsize=(10, 20), dpi=300) # Создаем 8 строки и 1 столбец Axes, указываем размеры изображения

x = np.arange(-500, 500) # Создаем массив x с использованием первого значения k

for i in range(len(k)):
    x = np.arange(-500, 500) # Создаем массив x с использованием текущего значения k
    y = np.exp((-k[i] * np.abs(x))) * (np.cos(k[i] * x) - np.sin(k[i] * np.abs(x))) # Вычисляем значения y для каждого значения k

    axes[i].plot(x, y, marker='o', markersize=2, linewidth=0.2) # Строим график в текущем Axes с измененными параметрами
    axes[i].set_title('k = {:.5f}'.format(k[i]), fontsize=8) # Устанавливаем заголовок для текущего Axes с измененным размером шрифта

    axes[i].set_xlim(-500, 500) # Устанавливаем границы оси x
    axes[i].set_ylim(-1, 1.5) # Устанавливаем границы оси y

    axes[i].tick_params(labelsize=6) # Изменяем размер меток на осях
    axes[i].invert_yaxis() # Инвертируем ось y

plt.tight_layout()
plt.savefig('my_plot.pdf', format='pdf', bbox_inches='tight', pad_inches=0) # Сохраняем график в формате PDF с оптимальными размерами
plt.show()
