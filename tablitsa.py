import main
import math
import matplotlib.pyplot as plt
import numpy as np

def round_up_to_10(number):
  if number >= 0:
    return math.ceil(number / 10) * 10
  else:
    return math.floor(number / 10) * 10


low = round_up_to_10(main.t_min_min)
high = round_up_to_10(main.t_max_max)

# Прямая
x = [5, 5]
y = [main.t_min_min, main.t_max_zakr]
y1 = [main.t_max_max, main.t_min_zakr]
x1 = [3, 3]

# Кривая
x2 = [17, 17]
y2 = [main.t_min_min, main.t_max_zakr_curve]
x3 = [15, 15]
y3 = [main.t_max_max, main.t_min_zakr_curve]

# Создаем фигуру и ось
fig, ax = plt.subplots()

# Рисуем линии
ax.plot(x, y, color='black', linewidth=1)
ax.plot(x1, y1, color='black', linewidth=1)
ax.plot(x2, y2, color='black', linewidth=1)
ax.plot(x3, y3, color='black', linewidth=1)

# Заштриховываем область
ax.fill_between(
    x=[0, 13],  # Координаты x для начала и конца области по оси X
    y1=main.t_max_zakr,  # Координаты y для верхней линии
    y2=main.t_min_zakr,  # Координаты y для нижней линии
    hatch='///',  # Узор штриховки
    color=None,  # Цвет заливки
    alpha=0.0  # Прозрачность заливки
)
ax.fill_between(
    x=[13, 30],  # Координаты x для начала и конца области по оси X
    y1=main.t_max_zakr_curve,  # Координаты y для верхней линии
    y2=main.t_min_zakr_curve,  # Координаты y для нижней линии
    hatch='///',  # Узор штриховки
    color=None,  # Цвет заливки
    alpha=0.0  # Прозрачность заливки
)
# Рисуем горизонтальные линии (спайны)
ax.hlines(y=main.t_max_max, xmin=0, xmax=30, color='black', linewidth=1, linestyles='--')  # Верхний спайн
ax.hlines(y=main.t_min_min, xmin=0, xmax=30, color='black', linewidth=1, linestyles='--') # Нижний спайн
ax.hlines(y=main.t_min_zakr, xmin=0, xmax=13, color='black', linewidth=1, linestyles='-.') # Нижний спайн
ax.hlines(y=main.t_max_zakr, xmin=0, xmax=13, color='black', linewidth=1, linestyles='-.') # Нижний спайн
ax.hlines(y=main.t_min_zakr_curve, xmin=13, xmax=30, color='black', linewidth=1, linestyles='-.') # Нижний спайн
ax.hlines(y=main.t_max_zakr_curve, xmin=13, xmax=30, color='black', linewidth=1, linestyles='-.') # Нижний спайн

ax.fill_between(x, x1, x2, color='lightblue', alpha=0.5) # Заштриховывание между y1 и y2

# Добавляем текст с помощью ax.text
ax.text(5, main.t_min_min-5, f'tmin min = {main.t_min_min}℃', ha='center', va='center') # ha - выравнивание по горизонтали, va - по вертикали
ax.text(5, main.t_max_max+5, f'tmax max = {main.t_max_max}℃', ha='center', va='center')
# Подписываем линию
ax.text(x=15, y=main.t_max_zakr, s=f't max закр = {main.t_max_zakr_curve}℃', va='bottom', ha='left', fontsize=10)
ax.text(x=2, y=main.t_max_zakr, s=f't max закр = {main.t_max_zakr}℃', va='bottom', ha='left', fontsize=10)
ax.text(x=2, y=main.t_min_zakr - 7, s=f't min закр = {main.t_min_zakr}℃', va='bottom', ha='left', fontsize=10)
ax.text(x=15, y=main.t_min_zakr_curve - 7, s=f't min закр = {main.t_min_zakr_curve}℃', va='bottom', ha='left', fontsize=10)
ax.text(x=18, y=main.t_min_zakr_curve - 40, s=f'[∆tp] = {main.delta_t_p1_min}℃', va='bottom', ha='left', fontsize=10, rotation=90)
ax.text(x=4, y=main.t_min_zakr_curve - 42, s=f'[∆tp] = {main.delta_t_p0_min}℃', va='bottom', ha='left', fontsize=7, rotation=90)
ax.text(x=2, y=main.t_min_zakr, s=f'[∆ty] = {main.t_у}℃', va='bottom', ha='left', fontsize=7, rotation=90)
ax.text(x=14, y=main.t_min_zakr_curve, s=f'[∆ty] = {main.t_у_curve}℃', va='bottom', ha='left', fontsize=7, rotation=90)
ax.text(x=15, y=main.t_min_min - 12, s=f'Кривая R = {main.curve[1]}м\ntопт = 30±5℃', va='bottom', ha='left', fontsize=10)

# Рисуем график
ax.plot(x, y, x1, y1, x2, y2, x3, y3)

# Добавляем стрелки с помощью quiver
ax.quiver(x[-1], y[-1]-3.5, 0, 0.5, color='blue', scale=20)  # u=0, v=0.5 - стрелка вверх
ax.quiver(x1[0], y1[1]+3.5, 0, -0.5, color='red', scale=20)  # u=0, v=-0.5 - стрелка вниз
ax.quiver(x2[-1], y2[-1]-3.5, 0, 0.5, color='blue', scale=20)  # u=0, v=0.5 - стрелка вверх
ax.quiver(x3[0], y3[1]+3.5, 0, -0.5, color='red', scale=20)  # u=0, v=-0.5 - стрелка вниз

ax.set_ylim(low-10, high+10)

# Настройка оси X: без подписи, без градуировки
ax.set_xlabel("")
ax.set_xticks([])

# Настройка подписи оси Y
ax.set_ylabel("Температура, градусы Цельсия (t°C)", rotation=90, labelpad=10)

# Удаление верхнего spine
ax.spines['top'].set_visible(False)


# Перенос правого spine
ax.spines['right'].set_position(('data', 13))

# Добавляем стрелки на оси X и Y
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
ax.plot((1), (0), ls="", marker=">", ms=5, color="k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot((0), (1), ls="", marker="^", ms=5, color="k", transform=ax.get_xaxis_transform(), clip_on=False)

# Установка делений оси Y (с шагом 10)
ax.set_yticks(np.arange(low, high + 10, 10))
ax.set_yticklabels(np.arange(low, high + 10, 10))


plt.savefig('Температурные Диаграммы.pdf', format='pdf', bbox_inches='tight', pad_inches=0)

print(low, high)
print(main.t_min_min, main.t_max_max)

