import numpy
import random
import pandas as pd

class PodvizhnoySostav:
    """Хранит и принимает исходные данные и работает с ними, выполняя расчеты. По пунктам КР (Пункты будут подписаны в коде
    с помощью ###)

    АТРИБУТЫ:
    ---------
    summer : str   winter or summer

    type_sostav : str  -- teplovoz/electrovoz or vagon

    p_ct  : int    -- Статическая нагрузка от колеса на рельс,Pст.кгс

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

    there is a curve:  no curve \ have curve

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

    и т д (продолжение следует/возможно есть описание в коде ниже, если тут нет)

    ПРИМЕЧАНИЕ:
    -----------
    None.

    ОШИБКИ:
    -------

    def Muu: не понимаю КАК ПЕРЕДАТЬ k ИЗ MAIN/initial_data в gragic_progibov, grafic_Izgib_moments.
    kx придется просчитывать вручную для каждой оси
    нет интерфейса, связи с эксель и ворд, недостаточно подробное описание"""

    def __init__(self, type_sostav: str, season: str, curve, q: int, JestcostRessor: float, d: int,
                 n: int, l_i: list, f: float, e: float, plot_of_sleep: int, u: int, k: float, l_sh: int,
                 p_ct: int):

        self.min_value_0 = None
        self.resulted = []
        self.results = []
        self.rounded_value = None
        self.value = None
        self.type_sostav = type_sostav
        self.season = season
        self.curve = curve
        self.p_ct = p_ct
        self.q = q
        self.d = d
        self.JestcostRessor = JestcostRessor
        self.n = n
        self.l_i = l_i
        self.f = f
        self.e = e
        self.plot_of_sleep = plot_of_sleep
        self.u = u
        self.k = k
        self.l_sh = l_sh
        self.alpha_E = 25.2
        self.k3 = 1.3  # round(random.uniform(0.9, 1.3), 1)
        self.delta_t3 = 10
        self.v = 85
        self.material_of_sleepers = "Дерево"
        self.rail_type = "P50"
        self.ballast = "Щебень"
        self.L = 0.261
        self.W = 417
        self.alpha0 = 0.403
        self.omega = 518
        self.omega_a = 3092
        self.b = 23
        self.h = 55
        self.ae = 0.7

    def z_max(self):
        if 'чс' in self.type_sostav.lower() or 'вл' in self.type_sostav.lower():
            return 10.9 + 9.6 * 10 **(-4) * self.v ** 2
        elif 'тэ' in self.type_sostav.lower() or 'м62' in self.type_sostav.lower() or 'чм' in self.type_sostav.lower():
            return 10.9 + 9.6 * 10 **(-4) * self.v ** 2
        elif '8' in self.type_sostav.lower():
            return 9.5 + 9 * 10 ** (-4) * self.v ** 2
        elif '6' in self.type_sostav.lower():
            return 6 + 16 * 10 ** (-4) * self.v ** 2
        else:
            return 10 + 16 * 10 ** (-4) * self.v ** 2

    '''
    def __str__(self):
        """Возвращает форматированную строку для нижепосчитанных значений для вывода в таблице.
        Стандартный метод, возвращающий текстовое представление объекта"""
        return f"{self.type_sostav, self.season, self.curve}\n{79 * '='}   \nР_р^max:{self.JestcostRessor}*{self.z_max()}={self.p_max_p():5.2f}   " \
               f"Р_р^ср кг: 0.75 * {self.p_max_p()} = {self.p_cp_p()}\n" \
               f"Pср,кгс: {self.p_ct} + {self.p_cp_p()} = {self.p_cp()}\n" \
               f"Sр,кг: 0.08 * {self.p_max_p()} = {self.s_p()}\n\n" \
               f"Snp: 0.565 * 10^-8 * {self.L}*{self.l_sh}* sqrt{self.u}/{self.k}*sqrt{self.q}*{self.p_cp()} * {self.v}={self.s_np()}\n" \
               f"\nSnnk: 0.052 * {self.alpha0}*{self.u}*{self.v}^2 * sqrt{self.q} /// {self.d}^2 * sqrt{self.k}*{self.u} - 3.26 * {self.k}^2*sqrt{self.q}={self.s_nnk()}\n\n" \
               f"Sink: 0.735 * {self.alpha0} * 2 * {self.u}/{self.k} * {self.e} = {self.s_ink()}\n\nS:{self.s_p()}^2 + {self.s_np()}^2 + 0.95 * {self.s_nnk()}^2 + 0.05 * {self.s_ink()}^2 = {self.s()}   " \
               f"\nP_max^ver: {self.p_cp()} + 2.5 * {self.s()} = {self.p_max_ver()}\n" \
               f"                    РАСЧЕТЫ К 1.3:\npi_4k:{self.pi_4k():7.2f}   pi_3_4k:{self.pi_3_4k():7.2f}   " \
               f"pi_5_4k:{self.pi_5_4k():7.2f}   pi_7_4k:{self.pi_7_4k():7.2f}\nР_1_экв:{round(self.P_I_ekv(), 2)}   " \
               f"Р_2_экв:{round(self.P_II_ekv(), 2)}\nMu2:{self.Muu2()}   Mu3:{self.Muu3()}    Mu4:{self.Muu4()}   " \
               f"SIGMA_MU:{round(self.Sigma_Muu(), 5)}\nsigma_kp:{self.sigma_kp()}   sigma_sh:{self.sigma_sh()}   " \
               f" sigma_b:{self.sigma_br()}\nN_2:{self.N_2()}   N_3:{self.N_3()}   N_4:{self.N_4()}   " \
               f"Sigma N:{self.Sigma_N()}   Расчетные оси: Мю:{self.RaschetnayaOS_Muu()}   " \
               f"Тета: {self.RaschetnayaOS_N()}\n\t\t\t\t\tРАСЧЕТЫ К 2.2\nPIIэкв1шп:{round(self.P_II_ekvONE(), 2)}   " \
               f"PIIэкв3шп:{round(self.P_II_ekvThree(), 2)}\nsigmaH1: {self.sigma_h1()}   sigmaH2: {self.sigma_h2()}  " \
               f" sigmaH3: {self.sigma_h3()}   Sigma_H: {self.sigma_h()}\nsigmaB1: {self.sigma_b1()}   " \
               f"sigmaB3: {self.sigma_b3()}    KOFm: {self.m()}\n" \
 \
    '''
        # ПУНКТ 1.2 Определение среднего и максимального вероятного

    # значения динамической силы воздействия колеса на рельс

    def p_max_p(self):
        """вычисляет динамическую нагрузку Р (верхний индекс max) + (нижний - р)"""
        return round(self.JestcostRessor * self.z_max(), 2)

    def p_cp_p(self):
        """вычисляем – среднее значение динамической нагрузки колеса на рельс от вертикальных колебаний надрессорного
        строения экипажа, кг."""
        return round(0.75 * self.p_max_p(), 2)

    def p_cp(self):
        """Pср	–	среднее значение вертикальной нагрузки колеса на рельс, кгс"""
        return round(0.75 * self.p_max_p() + self.p_ct, 2)

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
         воз¬никающих из-за наличия на поверхности катания колес плавных изолированных неровностей, кг"""
        return round(0.735 * self.alpha0 * (2 * self.u) / self.k * self.e, 2)

    def s(self):
        """Среднее квадратическое отклонение динамической вертикальной нагрузки колеса на рельс"""
        return round(
            (self.s_p() ** 2 + self.s_np() ** 2 + 0.95 * self.s_nnk() ** 2 + 0.05 * self.s_ink() ** 2) ** (1 / 2), 2)

    def p_max_ver(self):
        """Динамическая максимальная нагрузка от колеса на рельс. Оно же Рmax_вер и еще что-то..."""
        return round(self.p_cp() + 2.5 * self.s(), 2)

    # 1.3. Определение напряжений в элементах верхнего строения пути
    # 1.Строим лин влияния

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
        if self.n == 2:
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

    def N_sh(self):
        return (numpy.cos(self.k * self.l_sh) + numpy.sin(self.k * self.l_sh)) * numpy.e ** (-self.k * self.l_sh)

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
        """Ордината функции момента от приложенной еденичной силы (линии влияния) Мю по 2-ой расчетной
        оси"""
        if (self.k * self.l_i[0]) >= 5.5:
            return 0
        else:
            return self.NNN(self.l_i[0])

    def N_3(self):
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
        # вот здесь жопа, С должна браться из таблицы

    def sigma_h1(self):
        return round(0.25 * self.A() * self.sigma_b1(), 4)  # тоже жопа

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
        return int((4000 - (1.3 * self.sigma_kp())) / 25.2)

    def xm(self):
        if self.n == 4:
            return [0, self.l_i[0], self.l_i[0] + self.l_i[1], self.l_i[0] + self.l_i[1] + self.l_i[2]]
        if self.n == 3:
            return [0, self.l_i[0], self.l_i[0] + self.l_i[1], 0]
        else:
            return [0, self.l_i[0], 0, 0]

    def xn(self):
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
        workbook_15 = pd.read_excel(r'C:\Users\Администратор\PycharmProjects\kursach-vsp\A.xlsx')
        alarm = workbook_15.loc[workbook_15["h"] == self.h, "l" + str(self.b)]
        return list(alarm.head())[0]

    def xnn1(self):
        if self.RaschetnayaOS_N() == 1 or self.n == 2:
            return [55, self.xn()[1]+55, self.xn()[2]+55, self.xn()[3]+55]
        else:
            return [-self.xn()[0]+55, 55, self.xn()[2]+55, self.xn()[3]+55]

    def xnn3(self):
        if self.RaschetnayaOS_N() == 1 or self.n == 2:
            return [55, self.xn()[1]-55, self.xn()[2]-55, self.xn()[3]-55]
        else:
            return [-self.xn()[0] - 55, -55, self.xn()[2] - 55, self.xn()[3] - 55]

    def Iter(self):
        self.results = []
        for i in self.xnn1():
            self.value = (numpy.cos(self.k * i) + numpy.sin(self.k * i)) * numpy.e ** ((-self.k) * i)
            self.rounded_value = round(self.value, 5)
            self.results.append(self.rounded_value)
        return self.results

    def Iter1(self):
        self.resulted = []
        for i in self.xnn3():
            self.value = (numpy.cos(self.k * i) + numpy.sin(self.k * i)) * numpy.e ** ((-self.k) * i)
            self.rounded_value = round(self.value, 5)
            self.resulted.append(self.rounded_value)
        return self.resulted

    def summa1(self):
        if self.RaschetnayaOS_N() == 2:
            if self.n == 4:
                return self.Iter()[0] + self.Iter()[2] + self.Iter()[3]
            else:
                return self.Iter()[0] + self.Iter()[2]
        else:
            if self.n == 4:
                return self.Iter()[1] + self.Iter()[2] + self.Iter()[3]
            elif self.n == 3:
                return self.Iter()[1] + self.Iter()[2]
            else:
                return self.Iter()[1]
    def summa2(self):
        if self.RaschetnayaOS_N() == 2:
            if self.n == 4:
                return self.Iter1()[0] + self.Iter1()[2] + self.Iter1()[3]
            else:
                return self.Iter1()[0] + self.Iter1()[2]
        else:
            if self.n == 4:
                return self.Iter1()[1] + self.Iter1()[2] + self.Iter1()[3]
            elif self.n == 3:
                return self.Iter1()[1] + self.Iter1()[2]
            else:
                return self.Iter1()[1]

    def P_II_ekvONE(self):
        return round(self.p_max_ver() * self.NNN(self.l_sh) + self.p_cp() * int(self.summa1()), 2)
    def P_II_ekvThree(self):
        return round(self.p_max_ver() * self.NNN(self.l_sh) + self.p_cp() * int(self.summa2()), 2)

    def AA(self):
        workbook_16 = pd.read_excel(r'C:\Users\Администратор\PycharmProjects\kursach-vsp\AA.xlsx')

        # Преобразовываем столбец "R" в строковый тип данных
        workbook_16["R"] = workbook_16["R"].astype(str)

        alarm = workbook_16.loc[workbook_16["R"] == str(self.curve), self.rail_type]
        return list((alarm.head()))

    def AA1(self):
        workbook_17 = pd.read_excel(r'C:\Users\Администратор\PycharmProjects\kursach-vsp\M.xlsx')

        # Преобразовываем столбец "R" в строковый тип данных
        workbook_17["R"] = workbook_17["R"].astype(str)

        alarm = workbook_17.loc[workbook_17["R"] == str(self.curve), self.rail_type]
        return list((alarm.head()))

    def sigma_norm(self, min_value_0):
        return self.sigma_kp() * 1.3 + min_value_0 * 25.2

    def Ekv_gruzi_η(self):
        if self.RaschetnayaOS_N() == 2:
            return f'I ось: x = {self.l_i[0]} см; kx = {self.k}×{self.l_i[0]} = {(self.k*self.l_i[0]):.2f}; η = {self.N_2()}\nIII ось: x = {self.l_i[1]} см; kx = {self.k}×{self.l_i[1]} = {(self.k*self.l_i[1]):.2f}; η = {self.N_3()}\nVI ось: x = {self.l_i[1]}+{self.l_i[2]} см; kx = {self.k}×{self.l_i[1]+self.l_i[2]} = {(self.k*(self.l_i[1]+self.l_i[2])):.2f}; η = {self.N_4()}'
        else:
            return f'II ось: x = {self.l_i[0]} см; kx = {self.k}×{self.l_i[0]} = {(self.k*self.l_i[0]):.2f};' \
                   f' η = {self.N_2()}\nIII ось: x = {self.l_i[1]}+{self.l_i[0]} см;' \
                   f' kx = {self.k}×{self.l_i[0]+self.l_i[1]} = {(self.k*(self.l_i[0]+self.l_i[1])):.2f}; η = {self.N_3()}\nVI ось: ' \
                   f'x = {self.l_i[0]}+{self.l_i[1]}+{self.l_i[2]} см; kx = {self.k}×{self.l_i[0]+self.l_i[1]+self.l_i[2]} =' \
                   f' {(self.k*(self.l_i[0]+self.l_i[1]+self.l_i[2])):.2f}; η = {self.N_4()}'

    def Ekv_gruzi_µ(self):
        return f'II ось: x = {self.l_i[0]} см; kx = {self.k}×{self.l_i[0]} = {(self.k * self.l_i[0]):.2f};' \
               f' µ = {self.Muu2()}\nIII ось: x = {self.l_i[1]}+{self.l_i[0]} см;' \
               f' kx = {self.k}×{self.l_i[0] + self.l_i[1]} = {(self.k * (self.l_i[0] + self.l_i[1])):.2f}; µ = {self.Muu3()}\nVI ось: ' \
               f'x = {self.l_i[0]}+{self.l_i[1]}+{self.l_i[2]} см; kx = {self.k}×{self.l_i[0] + self.l_i[1] + self.l_i[2]} =' \
               f' {(self.k * (self.l_i[0] + self.l_i[1] + self.l_i[2])):.2f}; µ = {self.Muu4()}'
