import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Создаем фигуру и оси
fig, ax = plt.subplots()

# Создаем и добавляем прямоугольники на график
rect1 = Rectangle((0, 0), 3, 2, edgecolor='r', facecolor='none')  # Прямоугольник с шириной 2 и высотой 3
rect2 = Rectangle((4, 0), 3, 2, edgecolor='b', facecolor='none')  # Прямоугольник с шириной 1 и высотой 2
rect3 = Rectangle((8, 0), 3, 2, edgecolor='b', facecolor='none')  # Прямоугольник с шириной 1 и высотой 2

ax.add_patch(rect1)
ax.add_patch(rect2)
ax.add_patch(rect3)
# Устанавливаем пределы осей чтобы видеть прямоугольники
ax.set_xlim(0, 12)
ax.set_ylim(0, 12)

plt.show()

