import numpy as np
import matplotlib.pyplot as plt

# Заданные данные
x1 = -42
x2 = 58
mean = (x2 - x1) / 2 - 45
std_dev = 30

# Генерация данных для построения нормального распределения
x = np.linspace(x1 - 10, x2 + 10, 1000)
y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)

# Построение графика
plt.figure(figsize=(8, 6))
plt.plot(x, y, color='b')
plt.xlabel('Значения X')
plt.ylabel('Плотность вероятности')
plt.title('Нормальное распределение')
plt.axvline(x=mean, color='r', linestyle='--', label='Вершина графика')
plt.legend()

plt.grid(True)
plt.show()

