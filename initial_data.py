import numpy
import pandas as pd


class PodvizhnoySostav:
    """Хранит и принимает исходные данные и работает с ними, выполняя расчеты. По пунктам КР (Пункты будут подписаны в
    коде с помощью ###)

    АТРИБУТЫ:
    ---------
    summer : str   winter or summer

    type_sostav : str  -- teplovoz/electrovoz or vagon

    P_ct  : int    -- Статическая нагрузка от колеса на рельс,Pст.кгс

    v     : int    -- Скорость движения, V.км/ч

    q     : int    -- Вес необрессоренных частей, отнесенных  к одному колесу, q.кгс

    JestcostRessor: int -- Жесткость комплекта рессор, Ж.кг/мм

    d     : int    -- Диаметр колеса, d.см

    n     : int    -- Количество осей в тележке, n.шт

    l_i   : list   -- Расстояние между осями тележки, li.см

    f     : float   -- Коэффициент перехода от осевых напряжений к кромочным.

    e     : float  -- Наибольшая расчетная глубина неровности на колесе, e.см

    z_max : float  -- Наибольшая расчетная глубина неровности на колесе, e.мм

    rail_type: str -- Тип рельса (приведенный износ).-/мм

    material_of_sleep: str -- Материал шпал.

    plot_of_sleepers: int -- Эпюра шпал.шт/км

    ballast: str -- type of ballast

    u     : int  -- Модуль упругости подрельсового основания, U.кг/см2

    k     : float   -- Коэффициент относительной жесткости основания и рельса, k см-1.

    l_sh  : int    -- Расстояние между осями шпал, lш.см

    L    : float  -- Коэффициент, учитывающий влияние колеб. масс подвижного состава и пути, типа рельса,
                    материала шпал, рода балласта на образование динамических неровностей пути, L

     W     : int    -- Момент сопротивления рельса относительно наибольшего удаленного волокна от подошвы, W.см3

    alpha0: float  -- Коэффициент, учитывающий отношение необрессореной массы колеса и участвующей во взаимодействии
                     массы пути, α0

    omega     : int    -- Площадь рельсовой подкладки, omega.см2

    omega_a: int   -- Площадь полушпалы с поправкой на изгиб, Ωd.см2

    b     : float  -- Ширина нижней постели шпалы , b.см

    there is a curve:  no curve/have curve

    МЕТОДЫ:
    -------
    p_max_p()   -- вычисляет динамическую нагрузку Р (верхний индекс max) + (нижний - р, и далее с индексами
                                                                                                п той же логике).

    p_cp_p()  -- вычисляем вычисляем – среднее значение динамической нагрузки колеса на рельс от вертикальных колебаний
                    надрессорного строения экипажа, кг.

    s_p()    -- Среднее квадратическое отклонение динамической нагрузки колеса на рельс, надрессорной части Sр, кг
    s_np() -- Среднее квадратическое отклонение динамической на¬грузки колеса на рельс, Sнп,  кг, от сил инерции
        необрессоренных масс

    p_max_ver()   -- вычисляет динамическую нагрузку Р (верхний индекс max) + (нижний - р).

    и т д (продолжение следует/возможно есть описание в коде ниже, если тут нет, а возможно мне надоело расписывать,
    это все равно кроме меня никто не читает)

    ПРИМЕЧАНИЕ:
    -----------
    None.

    ОШИБКИ:
    -------

    Стоит разбавить процедурное программирование ООП(Хотя бы графики обернуть в классы). Задание со *
    kx считается вручную для каждой оси.
    нет интерфейса, стабильной связи с эксель и ворд (файл ворд иногда вылетает,
    необходимо держать резервную копию), недостаточно подробное описание
    Кажется, все можно было сделать гораздо проще с помощью f-строк, не засоряя проект ненужными функциями"""

    def __init__(self, **kwargs):
        # Обработка переданных аргументов
        for key, value in kwargs.items():
            setattr(self, key, value)
        # Остальные атрибуты и их инициализация
        self.k3 = 1.3  # round(random.uniform(0.9, 1.3), 1)
        self.ballast = "Щебень"

    def z_max(self):
        if 'чс' in self.type_sostav.lower() or 'вл' in self.type_sostav.lower():
            return [10.9 + 9.6 * 10 ** (-4) * self.v ** 2, 'Электровоз']
        elif 'тэ' in self.type_sostav.lower() or 'м62' in self.type_sostav.lower() or 'чм' in self.type_sostav.lower():
            return [7.9 + 8.0 * 10 ** (-4) * self.v ** 2, 'Тепловоз']
        elif '8' in self.type_sostav.lower():
            return [9.5 + 9 * 10 ** (-4) * self.v ** 2, 'НЕТУ']
        elif '6' in self.type_sostav.lower():
            return [6 + 16 * 10 ** (-4) * self.v ** 2, 'НЕТУ']
        else:
            return [10 + 16 * 10 ** (-4) * self.v ** 2, 'НЕТУ']

    # ПУНКТ 1.2 Определение среднего и максимального вероятного
    # значения динамической силы воздействия колеса на рельс

#    def p_max_p(self): - старая формула
#        """вычисляет динамическую нагрузку Р (верхний индекс max) + (нижний - р)"""
#        return round(self.JestcostRessor * self.z_max()[0], 2)

    def p_max_p(self):
        """вычисляет динамическую нагрузку Р (верхний индекс max) + (нижний - р)"""
        return self.Pmax_p

    def p_cp_p(self):
        """вычисляем – среднее значение динамической нагрузки колеса на рельс от вертикальных колебаний надрессорного
        строения экипажа, кг."""
        return round(0.75 * self.p_max_p(), 2)

    def p_cp(self):
        """Pср	–	среднее значение вертикальной нагрузки колеса на рельс, кгс"""
        return round(0.75 * self.p_max_p() + self.P_ct, 2)

    def s_p(self):
        """Среднее квадратическое отклонение динамической нагрузки колеса на рельс, от вертикальных колебаний
                                                                                    надрессорного строения  Sр, кг"""
        return round(0.08 * self.p_max_p(), 2)

    def s_np(self):
        """Среднее квадратическое отклонение динамической на¬грузки колеса на рельс, Sнп,  кг, от сил инерции
        необрессоренных масс """
        return round(
            0.565 * 10 ** -8 * self.L * self.l_sh * (self.u / self.k) ** (1 / 2) * self.q ** (1 / 2) * self.p_cp() * \
            self.v, 2)

    def s_nnk(self):
        """Среднее квадратическое отклонение динамической нагрузки колеса на рельс ,Sннк, кг, от сил инерции
        необрессоренной массы"""
        return round((0.052 * self.alpha0 * self.u * self.v ** 2 * self.q ** (1 / 2)) / (
                self.d ** 2 * (self.k * self.u - 3.26 * self.k ** 2 * self.q) ** (1 / 2)), 2)

    def s_ink(self):
        """среднее квадратическое отклонение динамической нагрузки колеса на рельс от сил инерции необрессоренной массы,
         возникающих из-за наличия на поверхности катания колес плавных изолированных неровностей, кг"""
        return round(0.735 * self.alpha0 * (2 * self.u) / self.k * self.e, 2)

    def s(self):
        """Среднее квадратическое отклонение динамической вертикальной нагрузки колеса на рельс"""
        return round(
            (self.s_p() ** 2 + self.s_np() ** 2 + 0.95 * self.s_nnk() ** 2 + 0.05 * self.s_ink() ** 2) ** (1 / 2), 2)

    def p_max_ver(self):
        """Динамическая максимальная нагрузка от колеса на рельс. Оно же Рmax_вер (максимальное вероятное)"""
        return round(self.p_cp() + 2.5 * self.s(), 2)

    # 1.3. Определение напряжений в элементах верхнего строения пути
    # 1.Строим линии влияния

    def pi_4k(self):
        return round(3.14 / (4.0 * self.k), 2)

    def pi_3_4k(self):
        return round(3 * 3.14 / (4.0 * self.k), 2)

    def pi_7_4k(self):
        return round(7 * 3.14 / (4.0 * self.k), 2)

    def pi_5_4k(self):
        return round(5 * 3.14 / (4.0 * self.k), 2)

    def RaschetnayaOS_Muu(self):
        if (numpy.pi / (4 * self.k)) > self.l_i[0] or self.l_i[0]:
            return 1
        else:
            return 1

    def RaschetnayaOS_N(self):
        if self.n == 2:
            return 1
        elif ((3 * numpy.pi) / (4 * self.k)) > self.l_i[0] or ((3 * numpy.pi) / (4 * self.k)) > self.l_i[1]:
            return 2
        else:
            return 1

    # 2.Cчитаем эквивалентные грузы

    def Muu2(self):
        """Ордината функции момента от приложенной еденичной силы (линии влияния) Мю по 2-ой расчетной
        оси"""
        if (self.k * self.l_i[0]) >= 5.5:
            return 0
        else:
            return round(self.MMM(self.l_i[0]), 5)

    def Muu3(self):
        if self.n == 2 or (self.k * (self.l_i[0] + self.l_i[1])) >= 5.5:
            return 0
        else:
            return round(self.MMM(self.l_i[0] + self.l_i[1]), 5)

    def Muu4(self):
        if self.n == 2 or self.n == 3:
            return 0
        else:
            if (self.k * sum(self.l_i)) >= 5.5:
                return 0
            else:
                return round(self.MMM(self.l_i[0] + self.l_i[1] + self.l_i[2]), 5)

    def Sigma_Muu(self):
        return self.Muu2() + self.Muu4() + self.Muu3()

    def MMM(self, x):
        return (numpy.cos(self.k * x) - numpy.sin(self.k * x)) * (numpy.e ** (-self.k * x))

    def P_I_ekv(self):
        if self.RaschetnayaOS_Muu() == 1 and self.n == 2:
            return self.p_max_ver() + self.p_cp() * self.MMM(self.l_i[0])
        elif self.RaschetnayaOS_Muu() == 1 and self.n == 3:
            return self.p_max_ver() + self.p_cp() * self.MMM(self.l_i[0]) + self.p_cp() * self.MMM(
                self.l_i[0] + self.l_i[1])
        elif self.RaschetnayaOS_Muu() == 1 and self.n == 4:
            return self.p_max_ver() + self.p_cp() * self.MMM(self.l_i[0]) + self.p_cp() * self.MMM(
                self.l_i[0] + self.l_i[1]) + self.p_cp() * self.MMM(self.l_i[0] + self.l_i[1] + self.l_i[2])
        elif self.RaschetnayaOS_Muu() == 2 and self.n == 2:
            return self.p_max_ver() + self.p_cp() * self.MMM(self.l_i[0])
        elif self.RaschetnayaOS_Muu() == 2 and self.n == 3:
            return self.p_max_ver() + self.p_cp() * self.MMM(self.l_i[0]) + self.p_cp() * self.MMM(self.l_i[1])
        elif self.RaschetnayaOS_Muu() == 2 and self.n == 4:
            return self.p_max_ver() + self.p_cp() * self.MMM(self.l_i[0]) + self.p_cp() * self.MMM(
                self.l_i[1]) + self.p_cp() * self.MMM(
                self.l_i[1] + self.l_i[2])

    def N_2(self):
        """Ордината функции момента от приложенной еденичной силы (линии влияния) Мю по 2-ой и расчетной
        оси"""
        if (self.k * self.l_i[0]) >= 5.5:
            return 0
        else:
            return self.NNN(self.l_i[0])

    def N_3(self):
        """Ордината функции момента от приложенной еденичной силы (линии влияния) Мю по 3-ей расчетной
        оси"""
        if self.n < 3:
            return 0
        elif self.RaschetnayaOS_N() == 1:
            if (self.k * (self.l_i[0] + self.l_i[1])) >= 5.5:
                return 0
            else:
                return self.NNN(self.l_i[0] + self.l_i[1])
        else:
            return self.NNN(self.l_i[1])

    def N_4(self):
        """Ордината функции момента от приложенной еденичной силы (линии влияния) Мю по 4-ей расчетной
        оси"""
        if self.n < 4:
            return 0
        elif self.RaschetnayaOS_N() == 1:
            if self.k * (sum(self.l_i)) >= 5.5 or self.n < 4:
                return 0
            else:
                return self.NNN(self.l_i[0] + self.l_i[1] + self.l_i[2])
        else:
            if (self.k * (self.l_i[1] + self.l_i[2])) >= 5.5:
                return 0
            else:
                return self.NNN(self.l_i[1] + self.l_i[2])

    def Sigma_N(self):
        return self.N_2() + self.N_3() + self.N_4()

    def P_II_ekv(self):
        if self.RaschetnayaOS_N() == 1 and self.n == 2:
            return self.p_max_ver() + self.p_cp() * self.NNN(self.l_i[0])
        elif self.RaschetnayaOS_N() == 1 and self.n == 3:
            return self.p_max_ver() + self.p_cp() * self.NNN(self.l_i[0]) + self.p_cp() * self.NNN(
                self.l_i[0] + self.l_i[1])
        elif self.RaschetnayaOS_N() == 1 and self.n == 4:
            return self.p_max_ver() + self.p_cp() * self.NNN(self.l_i[0]) + self.p_cp() * self.NNN(
                self.l_i[0] + self.l_i[1]) + self.p_cp() * self.NNN(self.l_i[0] + self.l_i[1] + self.l_i[2])
        elif self.RaschetnayaOS_N() == 2 and self.n == 2:
            return self.p_max_ver() + self.p_cp() * self.NNN(self.l_i[0])
        elif self.RaschetnayaOS_N() == 2 and self.n == 3:
            return self.p_max_ver() + self.p_cp() * self.NNN(self.l_i[0]) + self.p_cp() * self.NNN(self.l_i[1])
        elif self.RaschetnayaOS_N() == 2 and self.n == 4:
            return self.p_max_ver() + self.p_cp() * self.NNN(self.l_i[0]) + self.p_cp() * self.NNN(
                self.l_i[1]) + self.p_cp() * self.NNN(
                self.l_i[1] + self.l_i[2])

    def sigma_kp(self):
        return round(self.P_I_ekv() * self.f / (4 * self.k * self.W), 2)

    def sigma_sh(self):
        return round(self.P_II_ekv() * self.k * self.l_sh / (2 * self.omega), 2)

    def sigma_br(self):
        return round(((self.k * self.l_sh) / (2 * self.omega_a)) * self.P_II_ekv(), 2)

    ### 2.2 Определение напряжений на основной площадке земполотна

    def m(self):
        if (8.9 / (self.sigma_br() + 4.5)) >= 1.0:
            return round(8.9 / (self.sigma_br() + 4.5), 2)
        else:
            return 1

    def sigma_h2(self):
        return round(
            self.sigma_br() * self.ae * (2.55 * self.C2() + (0.635 * self.C1() - 1.275 * self.C2()) * self.m()), 3)

    def sigma_h1(self):
        return round(0.25 * self.A() * self.sigma_b1(), 4)

    def sigma_b1(self):
        return round((self.k * self.l_sh / (2 * self.omega_a)) * self.P_II_ekvONE(), 2)

    def NNN(self, x: int):
        return round((numpy.cos(self.k * x) + numpy.sin(self.k * x)) * (numpy.e ** ((-self.k) * x)), 5)

    def sigma_h3(self):
        return round(0.25 * self.A() * self.sigma_b3(), 4)

    def sigma_b3(self):
        return round((self.k * self.l_sh / (2 * self.omega_a)) * self.P_II_ekvThree(), 3)

    def sigma_h(self):
        return round(self.sigma_h1() + self.sigma_h2() + self.sigma_h3(), 3)

    ### 3.1 Расчет бс пути по условию устойчивости
    def delta_t_p(self):
        return round((4000 - (1.3 * self.sigma_kp())) / 25.2)

    def xm(self):
        """Расстояния от оси колесной пары до рассчетной оси µ"""
        if self.n == 4:
            return [0, self.l_i[0], self.l_i[0] + self.l_i[1], self.l_i[0] + self.l_i[1] + self.l_i[2]]
        if self.n == 3:
            return [0, self.l_i[0], self.l_i[0] + self.l_i[1], 0]
        else:
            return [0, self.l_i[0], 0, 0]

    def xn(self):
        """Расстояния от оси колесной пары до рассчетной оси η"""
        if self.RaschetnayaOS_N() == 1 or self.n == 2:
            return self.xm()
        else:
            if self.n == 4:
                return [self.l_i[0], 0, self.l_i[1], self.l_i[1] + self.l_i[2]]
            if self.n == 3:
                return [self.l_i[0], 0, self.l_i[1], 0]

    # Открываем файл Excel
    def C1(self):
        workbook_12 = pd.read_excel(r'C:\Users\Администратор\PycharmProjects\kursach-vsp\C1.xlsx')
        return list(workbook_12.loc[workbook_12["H"] == self.h, "l" + str(self.b)])[0]

    def C2(self):
        workbook_11 = pd.read_excel(r'C:\Users\Администратор\PycharmProjects\kursach-vsp\C2.xlsx')
        return list(workbook_11.loc[workbook_11["H"] == self.h, "l" + str(self.b)])[0]

    def A(self):
        """коэффициент, учитывающий расстояние между шпалами, ширину шпалы и глубину"""
        workbook_15 = pd.read_excel(r'C:\Users\Администратор\PycharmProjects\kursach-vsp\A.xlsx')
        return list(workbook_15.loc[workbook_15["h"] == self.h, "l" + str(self.b)].head())[0]

    def summa1(self):
        """Напряжения от 1-0й шпалы. Складывает η от всех осей, кроме ближайшей к расчетной"""
        if self.RaschetnayaOS_N() == 1 or self.n == 2:
            if self.n == 4:
                return self.NNN(self.l_i[0] + 55) + self.NNN(self.l_i[0] + self.l_i[1] + 55) + self.NNN(
                    self.l_i[0] + self.l_i[1] + self.l_i[2] + 55)
            elif self.n == 3:
                return self.NNN(self.l_i[0] + 55) + self.NNN(self.l_i[0] + self.l_i[1] + 55)
            else:
                return self.NNN(self.l_i[0] + 55)
        else:
            if self.n == 4:
                return self.NNN(self.l_i[0] - 55) + self.NNN(self.l_i[1] + 55) + self.NNN(
                    self.l_i[1] + self.l_i[2] + 55)
            else:
                return self.NNN(self.l_i[0] - 55) + self.NNN(self.l_i[1] + 55)

    def summa2(self):
        """Напряжения от 3-ей шпалы.Складывает η от всех осей, кроме ближайшей к расчетной"""
        if self.RaschetnayaOS_N() == 1 or self.n == 2:
            if self.n == 4:
                return self.NNN(self.l_i[0] - 55) + self.NNN(self.l_i[1] + 55) + self.NNN(
                    self.l_i[1] + self.l_i[2] + 55)
            elif self.n == 3:
                return self.NNN(self.l_i[0] - 55) + self.NNN(self.l_i[1] + 55)
            else:
                return self.NNN(self.l_i[0] - 55)
        else:
            if self.n == 4:
                return self.NNN(self.l_i[0] + 55) + self.NNN(self.l_i[1] - 55) + self.NNN(
                    self.l_i[1] + self.l_i[2] - 55)
            else:
                return self.NNN(self.l_i[0] + 55) + self.NNN(self.l_i[1] - 55)

    def P_II_ekvONE(self):
        return round(self.p_max_ver() * self.NNN(55) + self.p_cp() * self.summa1(), 2)

    def P_II_ekvThree(self):
        return round(self.p_max_ver() * self.NNN(55) + self.p_cp() * self.summa2(), 2)

    def AA(self):
        "Параметр А, зависящий от радиуса кривой и типа рельса"
        workbook_16 = pd.read_excel(r'C:\Users\Администратор\PycharmProjects\kursach-vsp\AA.xlsx')

        # Преобразовываем столбец "R" в строковый тип данных
        workbook_16["R"] = workbook_16["R"].astype(str)

        alarm = workbook_16.loc[workbook_16["R"] == str(self.curve), self.rail_type]
        return list((alarm.head()))

    def AA1(self):
        "Параметр µ, зависящий от радиуса кривой и типа рельса"
        workbook_17 = pd.read_excel(r'C:\Users\Администратор\PycharmProjects\kursach-vsp\M.xlsx')

        # Преобразовываем столбец "R" в строковый тип данных
        workbook_17["R"] = workbook_17["R"].astype(str)

        alarm = workbook_17.loc[workbook_17["R"] == str(self.curve), self.rail_type]
        return list((alarm.head()))

    def Ekv_gruzi_η(self):
        if self.RaschetnayaOS_N() == 2:
            return f'I ось: x = {self.l_i[0]} см; kx = {self.k}×{self.l_i[0]} = {(self.k * self.l_i[0]):.2f}; η = {self.N_2()}\nIII ось: x = {self.l_i[1]} см; kx = {self.k}×{self.l_i[1]} = {(self.k * self.l_i[1]):.2f}; η = {self.N_3()}\nVI ось: x = {self.l_i[1]}+{self.l_i[2]} см; kx = {self.k}×{self.l_i[1] + self.l_i[2]} = {(self.k * (self.l_i[1] + self.l_i[2])):.2f}; η = {self.N_4()}'
        else:
            return f'II ось: x = {self.l_i[0]} см; kx = {self.k}×{self.l_i[0]} = {(self.k * self.l_i[0]):.2f};' \
                   f' η = {self.N_2()}\nIII ось: x = {self.l_i[1]}+{self.l_i[0]} см;' \
                   f' kx = {self.k}×{self.l_i[0] + self.l_i[1]} = {(self.k * (self.l_i[0] + self.l_i[1])):.2f}; η = {self.N_3()}\nVI ось: ' \
                   f'x = {self.l_i[0]}+{self.l_i[1]}+{self.l_i[2]} см; kx = {self.k}×{self.l_i[0] + self.l_i[1] + self.l_i[2]} =' \
                   f' {(self.k * (self.l_i[0] + self.l_i[1] + self.l_i[2])):.2f}; η = {self.N_4()}'

    def Ekv_gruzi_µ(self):
        return f'II ось: x = {self.l_i[0]} см; kx = {self.k}×{self.l_i[0]} = {(self.k * self.l_i[0]):.2f}; µ = {self.Muu2():.5f}\n' \
               f'III ось: x = {self.l_i[1]}+{self.l_i[0]} см; kx = {self.k}×{self.l_i[0] + self.l_i[1]} = {(self.k * (self.l_i[0] + self.l_i[1])):.2f}; µ = {self.Muu3():.5f}\n' \
               f'VI ось: x = {self.l_i[0]}+{self.l_i[1]}+{self.l_i[2]} см; kx = {self.k}×{self.l_i[0] + self.l_i[1] + self.l_i[2]} = {(self.k * (self.l_i[0] + self.l_i[1] + self.l_i[2])):.2f}; µ = {self.Muu4():.5f}'

    def Ekv_gruzi_η_shpala_1(self):
        if self.RaschetnayaOS_N() == 1:
            if self.n == 4:
                return f'ηI: x = 55 см; kx = {self.k}×55 = {(self.k * 55):.2f}; η = {self.NNN(55):.5f}\n' \
                       f'ηII: x = {self.l_i[0]} + 55 см; kx = {self.k}×{self.l_i[0] + 55} = {(self.k * (self.l_i[0] + 55)):.2f}; η = {self.NNN(self.l_i[0] + 55):.5f}\n' \
                       f'ηIII: x = {self.l_i[0] + self.l_i[1]} + 55 см; kx = {self.k} × {self.l_i[0] + self.l_i[1] + 55} = {self.k * (self.l_i[0] + self.l_i[1] + 55):.2f}; η = {self.NNN(self.l_i[0] + self.l_i[1] + 55):.5f}\n' \
                       f'ηIV: x = {self.l_i[0]} + {self.l_i[1]}+{self.l_i[2]}+55; kx = {self.k}×{self.l_i[0] + self.l_i[1] + self.l_i[2] + 55} = {self.k * (self.l_i[0] + self.l_i[1] + self.l_i[2] + 55):.2f}; η = {self.NNN(self.l_i[0] + self.l_i[1] + self.l_i[2] + 55):.5f}'
            if self.n == 3:
                return f'ηI: x = 55 см; kx = {self.k}×55 = {(self.k * 55):.2f}; η = {self.NNN(55):.5f}\n' \
                       f'ηII: x = {self.l_i[0]} + 55 см; kx = {self.k}×{self.l_i[0] + 55} = {(self.k * (self.l_i[0] + 55)):.2f}; η = {self.NNN(self.l_i[0] + 55):.5f}\n' \
                       f'ηIII: x = {self.l_i[0] + self.l_i[1]} + 55 см; kx = {self.k} × {self.l_i[0] + self.l_i[1] + 55} = {self.k * (self.l_i[0] + self.l_i[1] + 55):.2f}; η = {self.NNN(self.l_i[0] + self.l_i[1] + 55):.5f}\n'
            else:
                return f'ηI: x = 55 см; kx = {self.k}× 55 = {(self.k * 55):.2f}; η = {self.NNN(55):.5f}\n' \
                       f'ηII: x = {self.l_i[0]} + 55 см; kx = {self.k} × {self.l_i[0] + 55} = {self.k * (self.l_i[0] + 55):.2f}; η = {self.NNN(self.l_i[0] + 55):.5f}\n'
        else:
            if self.n == 4:
                return f'ηI: x = {self.l_i[0]} - 55 см; kx = {self.k}×{self.l_i[0] - 55} = {(self.k * (self.l_i[0] - 55)):.2f}; η = {self.NNN(self.l_i[0]-55):.5f}\n' \
                       f'ηII: x = 55 см; kx = {self.k}×55 = {(self.k * 55):.2f}; η = {self.NNN(55):.5f}\n' \
                       f'ηIII: x = {self.l_i[1]}+55 см; kx = {self.k}×{self.l_i[1] + 55} = {self.k * (self.l_i[1] + 55):.2f}; η = {self.NNN(self.l_i[1] + 55):.5f}\n' \
                       f'ηIV: x = {self.l_i[1]}+{self.l_i[2]}+55; kx = {self.k}×{self.l_i[1] + self.l_i[2] + 55} = {self.k * (self.l_i[1] + self.l_i[2] + 55):.2f}; η = {self.NNN(self.l_i[1] + self.l_i[2] + 55):.5f}'
            else:
                return f'ηI: x = {self.l_i[0]} - 55 см; kx = {self.k}×{self.l_i[0] - 55} = {(self.k * (self.l_i[0] - 55)):.2f}; η = {self.NNN(self.l_i[0]):.5f}\n' \
                       f'ηII: x = 55 см; kx = {self.k}×55 = {(self.k * 55):.2f}; η = {self.NNN(55):.5f}\n' \
                       f'ηIII: x = {self.l_i[1]}+55 см; kx = {self.k}×{self.l_i[1] + 55} = {self.k * self.l_i[1] + 55:.2f}; η = {self.NNN(self.l_i[1] + 55):.5f}\n'

    def Ekv_gruzi_η_shpala_3(self):
        if self.RaschetnayaOS_N() == 1:
            if self.n == 4:
                return f'ηI: x = 55 см; kx = {self.k} × 55 = {(self.k * 55):.2f}; η = {self.NNN(self.l_sh):.5f}\n' \
                       f'ηII: x = {self.l_i[0]} - 55 см; kx = {self.k}×{self.l_i[0] - 55} = {(self.k * (self.l_i[0] - 55)):.2f}; η = {self.NNN(self.l_i[0] - 55):.5f}\n' \
                       f'ηIII: x = {self.l_i[0] + self.l_i[1]} - 55 см; kx = {self.k} × {self.l_i[0] + self.l_i[1] - 55} = {self.k * (self.l_i[0] + self.l_i[1] - 55):.2f}; η = {self.NNN(self.l_i[0] + self.l_i[1] - 55):.5f}\n' \
                       f'ηIV: x = {self.l_i[0] + self.l_i[1] + self.l_i[2]} - 55 см; kx = {self.k} × {self.l_i[0] + self.l_i[1] + self.l_i[2] - 55} = {self.k * (self.l_i[0] + self.l_i[1] + self.l_i[2] - 55):.2f}; η = {self.NNN(self.l_i[0] + self.l_i[1] + self.l_i[2] - 55):.5f}\n'
            if self.n == 3:
                return f'ηI: x = 55 см; kx = {self.k} × 55 = {(self.k * 55):.2f}; η = {self.NNN(self.l_sh):.5f}\n' \
                       f'ηII: x = {self.l_i[0]} - 55 см; kx = {self.k} × {self.l_i[0] - 55} = {(self.k * (self.l_i[0] - 55)):.2f}; η = {self.NNN((self.l_i[0] - 55)):.5f}\n' \
                       f'ηIII: x = {self.l_i[0] + self.l_i[1]} - 55 см; kx = {self.k} × {self.l_i[0] + self.l_i[1] - 55} = {self.k * (self.l_i[0] + self.l_i[1] - 55):.2f}; η = {self.NNN(self.l_i[0] + self.l_i[1] - 55):.5f}\n'
            else:
                return f'ηI: x = 55 см; kx = {self.k} × 55 = {(self.k * 55):.2f}; η = {self.NNN(self.l_sh):.5f}\n' \
                       f'ηII: x = {self.l_i[0]} - 55 см; kx = {self.k} × {self.l_i[0] - 55} = {(self.k * (self.l_i[0] - 55)):.2f}; η = {self.NNN((self.l_i[0] - 55)):.5f}\n'
        else:
            if self.n == 4:
                return f'ηI: x = {self.l_i[0]} + 55 см; kx = {self.k}×{self.l_i[0] + 55} = {(self.k * (self.l_i[0] + 55)):.2f}; η = {self.NNN(self.l_i[0] + 55):.5f}\n' \
                       f'ηII: x = 55 см; kx = {self.k}×55 = {(self.k * 55):.2f}; η = {self.NNN(55):.5f}\n' \
                       f'ηIII: x = {self.l_i[1]} - 55 см; kx = {self.k}×{self.l_i[1] - 55} = {self.k * (self.l_i[1] - 55):.2f}; η = {self.NNN(self.l_i[1] - 55):.5f}\n' \
                       f'ηIV: x = {self.l_i[1]} + {self.l_i[2]}-55; kx = {self.k}×{self.l_i[1] + self.l_i[2] - 55} = {self.k * (self.l_i[1] + self.l_i[2] - 5):.2f}; η = {self.NNN(self.l_i[1] + self.l_i[2] - 55):.5f}'
            if self.n == 3:
                return f'ηI: x = {self.l_i[0]} + 55 см; kx = {self.k}×{self.l_i[0] + 55} = {(self.k * (self.l_i[0] + 55)):.2f}; η = {self.NNN(self.l_i[0] + 55):.5f}\n' \
                       f'ηII: x = 55 см; kx = {self.k}×55 = {(self.k * 55):.2f}; η = {self.NNN(55):.5f}\n' \
                       f'ηIII: x = {self.l_i[1]} - 55 см; kx = {self.k}×{self.l_i[1] - 55} = {self.k * self.l_i[1] - 55:.2f}; η = {self.NNN(self.l_i[1] - 55):.5f}\n'
