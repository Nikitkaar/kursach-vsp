import matplotlib.pyplot as plt
import numpy as np


class GrafVerTemp:

    def __init__(self, **kwargs):
        self.t_y = kwargs.get('t_y')
        #self.t_y = 52
        self.t_max_max = kwargs.get('t_max_max')  # максимум
        self.delta_t_p_true = kwargs.get('delta_t_p') #пишем на графике
        #self.delta_t_p_true = 75
        self.t_min_min = kwargs.get('t_min_min')  # минимум
        self.delta_t_p = min(kwargs.get('delta_t_p')+self.t_min_min, self.t_max_max)
        #self.delta_t_p = self.delta_t_p_true + self.t_min_min
        self.mean = kwargs.get('mean',  (self.t_max_max+self.t_min_min)/2)  # среднее значение
        self.std_dev = kwargs.get('std_dev', 25)  # более широкое стандартное отклонение для пологой вершины
        self.x_left = self.round_to_tens(self.t_min_min)
        self.x_right = self.round_to_tens(self.t_max_max)
        self.t_opt = kwargs.get('t_opt', 30)
    @staticmethod
    def round_to_tens(number):
        # Определяем знак числа
        sign = 1 if number >= 0 else -1
        number = abs(number)
        rounded_number = ((number + 5) // 10) * 10
        return sign * rounded_number

    def grafic_maker_(self):
        plt.clf()
        plt.figure(figsize=(12, 6))  # Изменяем размер графика, увеличивая ширину

        # Define the data
        x = np.linspace(self.t_min_min, self.t_max_max, 1000)

        # Используем параметрическое нормальное распределение
        y = (1 / (self.std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - self.mean) / self.std_dev) ** 2)

        # Нормируем значения y так, чтобы вероятность в крайних точках была равной
        y_normalized = y / np.max(y) * (1 / (self.t_max_max - self.t_min_min))

        # Создаем график
        plt.plot(x, y_normalized)

        # Вычисляем значения функции в точках, соответствующих выходу, максимальному и минимальному количеству
        y_min = (1 / (self.std_dev * np.sqrt(2 * np.pi))) * np.exp(
            -0.5 * ((self.t_min_min - self.mean) / self.std_dev) ** 2) \
                / np.max(y) * (1 / (self.t_max_max - self.t_min_min))

        # Вычисляем значение функции для t_opt - 30
        violet_y = (1 / (self.std_dev * np.sqrt(2 * np.pi))) * np.exp(
            -0.5 * ((self.t_opt - 30 - self.mean) / self.std_dev) ** 2) \
                   / np.max(y) * (1 / (self.t_max_max - self.t_min_min))

        violet_y1 = (1 / (self.std_dev * np.sqrt(2 * np.pi))) * np.exp(
            -0.5 * ((self.t_opt - 5 - self.mean) / self.std_dev) ** 2) \
                   / np.max(y) * (1 / (self.t_max_max - self.t_min_min))

        violet_y2 = (1 / (self.std_dev * np.sqrt(2 * np.pi))) * np.exp(
            -0.5 * ((self.t_opt + 5 - self.mean) / self.std_dev) ** 2) \
                   / np.max(y) * (1 / (self.t_max_max - self.t_min_min))

        violet_y3 = (1 / (self.std_dev * np.sqrt(2 * np.pi))) * np.exp(
            -0.5 * ((self.t_opt + 20 - self.mean) / self.std_dev) ** 2) \
                   / np.max(y) * (1 / (self.t_max_max - self.t_min_min))

        # Отметим среднее значение и границы штриховой линией
        plt.vlines(self.mean, 0, np.max(y_normalized), color='red', linestyle='--', label=f'Средняя за год температура = {self.mean}℃')
        plt.vlines(self.t_max_max, 0, np.min(y_normalized), color='red', linestyle='-')
        plt.vlines(self.t_min_min, 0, np.min(y_normalized), color='red', linestyle='-')
        plt.vlines(self.delta_t_p, 0, y_min, color='red', linestyle='-')

        plt.vlines(self.t_opt-5, y_min, violet_y1, color='red', linestyle='-')
        plt.vlines(self.t_opt+5, y_min, violet_y2, color='red', linestyle='-')
        plt.vlines(self.t_opt+20, y_min, violet_y3, color='red', linestyle='-')

        # Устанавливаем верх фиолетовой вертикали на значение функции
        plt.vlines(self.t_opt - 30, y_min, violet_y, color='violet', linestyle='-')

        plt.vlines(self.t_max_max - self.t_y, 0, y_min, color='blue', linestyle='-')

        # Добавим горизонтальный отрезок между максимальной и минимальной температурами
        plt.hlines(0, self.t_min_min, self.t_max_max, colors='orange', linestyles='-')
        plt.hlines(y_min, self.t_min_min, self.t_max_max, colors='red', linestyles='-')
        plt.hlines(y_min, self.t_opt - 5, self.t_opt - 30, colors='green', linestyles='-')
        plt.hlines(y_min, self.t_opt + 5, self.t_opt + 20, colors='black', linestyles='-')
        plt.hlines(y_min / 2, self.t_max_max, self.t_max_max - self.t_y, colors='yellow', linestyles='-')


        # Добавление стрелки с заданными координатами
        arrow_start = (self.t_max_max, y_min / 2)  # Начальные координаты стрелки
        arrow_end = (self.t_max_max - self.t_y, y_min / 2)  # Конечные координаты стрелки
        plt.annotate('', xy=arrow_end, xytext=arrow_start,
                     arrowprops=dict(arrowstyle='->', color='yellow', lw=1.0))
        # Подпись к стрелке
        plt.text(arrow_end[0] + 1, arrow_end[1] + 0.0002, f'[∆ty] = {self.t_y}℃', fontsize=10, ha='left')

        plt.annotate('', xy=(self.t_min_min + 63, 0), xytext=(self.t_min_min, 0),
                     arrowprops=dict(arrowstyle='->', color='black', lw=1.0))
        # Подпись к стрелке
        plt.text(self.t_min_min + 55, 0.0002, f'tзаз = 70℃', fontsize=10, ha='left')

        plt.annotate('', xy=(self.delta_t_p, 0), xytext=(self.t_min_min, 0),
                     arrowprops=dict(arrowstyle='->', color='gray', lw=1.0))
        # Подпись к стрелке
        plt.text(self.delta_t_p - 7, 0.0002, f'[∆tp] = {self.delta_t_p_true}℃', fontsize=10, ha='left')
        plt.text(self.t_max_max - 7, 0.0015, f'ω1', fontsize=20, ha='left')
        plt.text(self.t_min_min + 15, 0.0015, f'ω2', fontsize=20, ha='left')


        plt.hlines(0, self.t_min_min, self.delta_t_p, colors='orange', linestyles='-')
        plt.hlines(0, self.t_min_min, self.t_min_min + 63, colors='black', linestyles='-') # ВОТ ТУТ ЖОПА с ТЕМПЕРАТУРОЙ ЗАЗОРА

        # Заштриховываем область между графиком функции и фиолетовой и красной линиями
        # Под синей линией и до фиолетовой линии
        plt.fill_between(x, y_normalized, y_min, where=(x <= (self.t_opt - 30)),
                         color='lightblue', alpha=0.0, hatch='-|-', label=f'ω1 и ω2 - ограничения работы путевых машин')

        # Под синей линией и от фиолетовой линии до x=s_t_opt+20
        plt.fill_between(x, y_min, y_normalized, where=(x >= (self.t_opt + 20)),
                         color='lightgreen', alpha=0.0, hatch='|')

        # Заштриховываем область от t_opt - 5 до t_opt + 5
        plt.fill_between(x, y_normalized, y_min, where=(x >= (self.t_opt - 5)) & (x <= (self.t_opt + 5)),
                         color='lightcoral', alpha=0.0,  hatch='///')

        # Устанавливаем метки на ось X через каждые 5 градусов
        ticks_x = list(range(self.x_left, self.x_right + 1, 5))
        plt.xticks(ticks_x)

        # Настройка ограничений по высоте оси Y
        plt.ylim(-0.001, np.max(y_normalized) * 1.02)  # Добавляем небольшой запас и более низкую верхнюю границу
        plt.xlim(self.t_min_min - 10, self.t_max_max + 10)  # Устанавливаем ограничения по ширине оси X

        # Добавление стрелок на левые и нижние оси
        plt.plot((0), (np.max(y_normalized) * 1.02), ls="", marker="^", ms=5, color="black", transform=plt.gca().get_yaxis_transform(),
                 clip_on=False)
        plt.plot((self.t_max_max + 10), (0), ls="", marker=">", ms=5, color="black", transform=plt.gca().get_xaxis_transform(),
                 clip_on=False)
        # Добавляем текст с максимальными и минимальными значениями на график
        plt.text(self.t_max_max+5, 0.22 * np.max(y_normalized), f'Макс: {self.t_max_max}℃', fontsize=10,
                 ha='right', color='blue')
        plt.text(self.t_min_min-7, 0.22 * np.max(y_normalized), f'Мин: {self.t_min_min}℃', fontsize=10,
                 ha='left', color='blue')
        plt.text(self.t_opt-1, 0.15 * np.max(y_normalized), '10', fontsize=10,
                 ha='left', color='blue')
        plt.text(self.t_opt-2, violet_y1, f'tопт = {self.t_opt}±5℃', fontsize=10,
                 ha='left', color='blue')
        plt.text(self.t_opt - 18, 0.15 * np.max(y_normalized), '25', fontsize=10,
                 ha='left', color='blue')
        plt.text(self.t_opt + 11, 0.15 * np.max(y_normalized), '15', fontsize=10,
                 ha='left', color='blue')
        # Set the title and labels
        plt.title("График плотности вероятности распределения температуры рельса в годичном цикле")
        plt.xlabel("t℃")
        plt.ylabel("Вероятность распределения")

        # Убираем верхний и правый spines
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        # Добавление легенды в правый верхний угол
        plt.legend(loc='upper right')

        # Показать и сохранить график
        plt.savefig('График оптимальной температуры.pdf', format='pdf', bbox_inches='tight', pad_inches=0)

