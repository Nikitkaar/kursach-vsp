from initial_data import PodvizhnoySostav
from openpyxl import Workbook

# ВВОЖУ ИСХОДНЫЕ ДАННЫЕ
# Локомотив/Вагон;;;
Pct = [11500, 13400]
q = [3170, 1070]
JestcostRessor = [142, 195]
d = [120, 95]
n = [3, 3]
l_i = [[220, 220, 0.0], [175, 175, 0]]
curve = ["Прямая", 700]
# Локомотив:     Вагон:
# Прямая/Кривая; Прямая/Кривая
f = [1.17, 1.26, 1.13, 1.32]
Zmax = [16.3, 15.0]
# Прямая, Лето\Зима:     Кривая, Лето\Зима:
U = [1000, 1500, 1100, 1600]
k = [0.01338, 0.015163, 0.01421, 0.0154096]
# U = [U[0], U[0] * 1.5, U[1], U[1] * 1.5]  # Вместе с зимой

sostavs = [
    PodvizhnoySostav("ВЛ-23", "Лето", curve[0], q[0], JestcostRessor[0], d[0], n[0], l_i[0], f[0], 0.047, Zmax[0],
                     1840, U[0], k[0], 55, Pct[0]),
    PodvizhnoySostav("ВЛ-23", "Зима", curve[0], q[0], JestcostRessor[0], d[0], n[0], l_i[0], f[0], 0.047, Zmax[0],
                     1840, U[1], k[1], 55, Pct[0]),
    PodvizhnoySostav("ВЛ-23", "Лето", curve[1], q[0], JestcostRessor[0], d[0], n[0], l_i[0], f[1], 0.047, Zmax[0],
                     2000, U[2], k[2], 51, Pct[0]),
    PodvizhnoySostav("ВЛ-23", "Зима", curve[1], q[0], JestcostRessor[0], d[0], n[0], l_i[0], f[1], 0.047, Zmax[0],
                     2000, U[3], k[3], 51, Pct[0]),
    PodvizhnoySostav("6-осный Вагон", "Лето", curve[0], q[1], JestcostRessor[1], d[1], n[1], l_i[1], f[2], 0.067,
                     Zmax[1],
                     1840, U[0], k[0], 55, Pct[1]),
    PodvizhnoySostav("6-осный Вагон", "Зима", curve[0], q[1], JestcostRessor[1], d[1], n[1], l_i[1], f[2], 0.067,
                     Zmax[1],
                     1840, U[1], k[1], 55, Pct[1]),
    PodvizhnoySostav("6-осный Вагон", "Лето", curve[1], q[1], JestcostRessor[1], d[1], n[1], l_i[1], f[3], 0.067,
                     Zmax[1],
                     2000, U[2], k[2], 51, Pct[1]),
    PodvizhnoySostav("6-осный Вагон", "Зима", curve[1], q[1], JestcostRessor[1], d[1], n[1], l_i[1], f[3], 0.067,
                     Zmax[1],
                     2000, U[3], k[3], 51, Pct[1])
]


def printHead(s):
    print("=" * 79)
    print(s)
    print("=" * 79)


# Выводит содержимое расчетов
def printList():
    printHead("РАСЧЕТЫ:")
    for i in range(len(sostavs)):
        # Заметьте, что выводится объект products[i]
        # Возвращаемая строка указана в методе __str__ класса
        print(f"{(i + 1)}.{sostavs[i]}")


printList()

# ГЛАВНАЯ ТАБЛИЦА

workbook_3 = Workbook()
sheet = workbook_3.active

# РАБОТА С ЭКСЕЛЬ, ЗАПИСЬ НУЖНЫХ ДАННЫХ В ТАБЛИЦУ

for i, sostav in enumerate(sostavs, start=1):
    info = sostav.type_sostav
    sheet.cell(row=1, column=i, value=info)
    info = sostav.curve
    sheet.cell(row=2, column=i, value=info)
    info = sostav.season
    sheet.cell(row=3, column=i, value=info)
    info = sostav.p_ct
    sheet.cell(row=4, column=i, value=info)
    informa = sostav.v
    sheet.cell(row=5, column=i, value=informa)
    inf = sostav.q
    sheet.cell(row=6, column=i, value=inf)
    inf = sostav.JestcostRessor
    sheet.cell(row=7, column=i, value=inf)
    inf = sostav.d
    sheet.cell(row=8, column=i, value=inf)
    inf = sostav.n
    sheet.cell(row=9, column=i, value=inf)
    inf = sostav.rail_type
    sheet.cell(row=10, column=i, value=inf)
    inf = sostav.f
    sheet.cell(row=11, column=i, value=inf)
    inf = sostav.e
    sheet.cell(row=12, column=i, value=inf)
    inf = sostav.z_max
    # sheet.cell(row=13, column=i, value=inf)
    # inf = sostav.type_of_rail
    # sheet.cell(row=14, column=i, value=inf)
    # inf = sostav.радиус кривой
    sheet.cell(row=15, column=i, value=inf)
    inf = sostav.material_of_sleepers
    sheet.cell(row=16, column=i, value=inf)
    inf = sostav.u
    sheet.cell(row=17, column=i, value=inf)
    inf = sostav.k
    sheet.cell(row=18, column=i, value=inf)
    inf = sostav.L
    sheet.cell(row=19, column=i, value=inf)
    inf = sostav.W
    sheet.cell(row=20, column=i, value=inf)
    inf = sostav.alpha0
    sheet.cell(row=21, column=i, value=inf)
    inf = sostav.omega
    sheet.cell(row=22, column=i, value=inf)
    inf = sostav.omega_a
    sheet.cell(row=23, column=i, value=inf)
    inf = sostav.b
    sheet.cell(row=24, column=i, value=inf)
    inf = sostav.p_max_p()
    sheet.cell(row=25, column=i, value=inf)
    inf = sostav.p_cp_p()
    sheet.cell(row=26, column=i, value=inf)
    inf = sostav.p_cp()
    sheet.cell(row=27, column=i, value=inf)
    inf = sostav.s_p()
    sheet.cell(row=28, column=i, value=inf)
    inf = sostav.s_np()
    sheet.cell(row=29, column=i, value=inf)
    inf = sostav.s_nnk()
    sheet.cell(row=30, column=i, value=inf)
    inf = sostav.s_ink()
    sheet.cell(row=31, column=i, value=inf)
    inf = sostav.s()
    sheet.cell(row=32, column=i, value=inf)
    inf = sostav.p_max_ver()
    sheet.cell(row=33, column=i, value=inf)
    inf = sostav.pi_4k()
    sheet.cell(row=34, column=i, value=inf)
    inf = sostav.pi_5_4k()
    sheet.cell(row=35, column=i, value=inf)
    inf = sostav.pi_3_4k()
    sheet.cell(row=36, column=i, value=inf)
    inf = sostav.pi_7_4k()
    sheet.cell(row=37, column=i, value=inf)
    inf = round(sostav.P_I_ekv(), 2)
    sheet.cell(row=38, column=i, value=inf)
    inf = sostav.Muu2()
    sheet.cell(row=39, column=i, value=inf)
    inf = sostav.Muu3()
    sheet.cell(row=40, column=i, value=inf)
    inf = sostav.Muu4()
    sheet.cell(row=41, column=i, value=inf)
    inf = sostav.Sigma_Muu()
    sheet.cell(row=42, column=i, value=inf)
    inf = round(sostav.P_II_ekv(), 2)
    sheet.cell(row=43, column=i, value=inf)
    inf = sostav.N_2()
    sheet.cell(row=44, column=i, value=inf)
    inf = sostav.N_3()
    sheet.cell(row=45, column=i, value=inf)
    inf = sostav.N_4()
    sheet.cell(row=46, column=i, value=inf)
    inf = sostav.Sigma_N()
    sheet.cell(row=47, column=i, value=inf)
    inf = sostav.RaschetnayaOS_N()
    sheet.cell(row=48, column=i, value=inf)
    inf = sostav.sigma_kp()
    sheet.cell(row=49, column=i, value=inf)
    inf = sostav.sigma_sh()
    sheet.cell(row=50, column=i, value=inf)
    inf = sostav.sigma_br()
    sheet.cell(row=51, column=i, value=inf)
    inf = sostav.ae
    sheet.cell(row=52, column=i, value=inf)
    inf = sostav.m()
    sheet.cell(row=55, column=i, value=inf)
    inf = sostav.sigma_h2()
    sheet.cell(row=56, column=i, value=inf)
    inf = sostav.A()
    sheet.cell(row=57, column=i, value=inf)
    inf = sostav.C1()
    sheet.cell(row=63, column=i, value=inf)
    inf = sostav.C2()
    sheet.cell(row=64, column=i, value=inf)
    inf = sostav.delta_t_p()
    sheet.cell(row=67, column=i, value=inf)
    inf = sostav.k3
    sheet.cell(row=68, column=i, value=inf)
    inf = sostav.curve

    sheet.cell(row=70, column=i, value=inf)
    inf = sostav.xm()[0]
    sheet.cell(row=71, column=i, value=inf)
    inf = sostav.xm()[1]
    sheet.cell(row=72, column=i, value=inf)
    inf = sostav.xm()[2]
    sheet.cell(row=73, column=i, value=inf)
    inf = sostav.xm()[3]
    sheet.cell(row=74, column=i, value=inf)
    inf = sostav.xn()[0]
    sheet.cell(row=75, column=i, value=inf)
    inf = sostav.xn()[1]
    sheet.cell(row=76, column=i, value=inf)
    inf = sostav.xn()[2]
    sheet.cell(row=77, column=i, value=inf)
    inf = sostav.xn()[3]
    sheet.cell(row=78, column=i, value=inf)
    inf = sostav.l_i[1]
    sheet.cell(row=79, column=i, value=inf)
    inf = sostav.xn()[2]
    sheet.cell(row=81, column=i, value=inf)
    inf = sostav.xnn1()[0]
    sheet.cell(row=82, column=i, value=inf)
    inf = sostav.xnn1()[1]
    sheet.cell(row=83, column=i, value=inf)
    inf = sostav.xnn1()[2]
    sheet.cell(row=84, column=i, value=inf)
    inf = sostav.xnn1()[3]
    sheet.cell(row=85, column=i, value=inf)
    inf = sostav.Iter()[0]
    sheet.cell(row=86, column=i, value=inf)
    inf = sostav.Iter()[1]
    sheet.cell(row=87, column=i, value=inf)
    inf = sostav.Iter()[2]
    sheet.cell(row=88, column=i, value=inf)
    inf = sostav.Iter()[3]
    sheet.cell(row=89, column=i, value=inf)
    inf = sostav.summa1()
    sheet.cell(row=90, column=i, value=inf)
    inf = sostav.Iter1()[0]
    sheet.cell(row=91, column=i, value=inf)
    inf = sostav.Iter1()[1]
    sheet.cell(row=92, column=i, value=inf)
    inf = sostav.Iter1()[2]
    sheet.cell(row=93, column=i, value=inf)
    inf = sostav.Iter1()[3]
    sheet.cell(row=94, column=i, value=inf)
    inf = sostav.summa2()
    sheet.cell(row=95, column=i, value=inf)
    inf = sostav.xnn3()[0]
    sheet.cell(row=96, column=i, value=inf)
    inf = sostav.xnn3()[1]
    sheet.cell(row=97, column=i, value=inf)
    inf = sostav.xnn3()[2]
    sheet.cell(row=98, column=i, value=inf)
    inf = sostav.xnn3()[3]
    sheet.cell(row=99, column=i, value=inf)
    inf = sostav.P_II_ekvONE()
    sheet.cell(row=100, column=i, value=inf)
    inf = sostav.P_II_ekvThree()
    sheet.cell(row=101, column=i, value=inf)
    inf = sostav.sigma_b1()
    sheet.cell(row=102, column=i, value=inf)
    inf = sostav.sigma_h1()
    sheet.cell(row=103, column=i, value=inf)
    inf = sostav.sigma_b3()
    sheet.cell(row=104, column=i, value=inf)
    inf = sostav.sigma_h3()
    sheet.cell(row=105, column=i, value=inf)
    inf = sostav.sigma_h()
    sheet.cell(row=106, column=i, value=inf)
    inf = sostav.AA()[0]
    sheet.cell(row=107, column=i, value=inf)
    inf = sostav.AA1()[0]
    sheet.cell(row=108, column=i, value=inf)




workbook_3.save('УЛЬТИМАТИВНАЯ_Формулы.xlsx')

print(sostav.AA()[0])
