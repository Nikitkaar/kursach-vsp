from initial_data import PodvizhnoySostav
from openpyxl import Workbook

# ВВОЖУ ИСХОДНЫЕ ДАННЫЕ
# Локомотив/Вагон;
Pct = [11500, 14000]
q = [3160, 995]
JestcostRessor = [116, 200]
d = [125, 95]
n = [2, 4]
l_i = [[300, 0, 0], [185, 125, 185]]
curve = ["Прямая", 600]

# Прямая, Лето\Зима:     Кривая, Лето\Зима:
U = [260, 500, 290, 600]
k = [0.01145, 0.0, 0.01176, 0.0]
k[1] = round((U[1]/(4*2.1*10**6*2018)) ** 0.25, 5)
k[3] = round((U[3]/(4*2.1*10**6*2018)) ** 0.25, 5)
# Локомотив:     Вагон:
# Прямая/Кривая; Прямая/Кривая
f = [1.25, 1.33, 1.18, 1.37]

# U = [U[0], U[0] * 1.5, U[1], U[1] * 1.5]  # Вместе с зимой

sostavs = [
    PodvizhnoySostav("ВЛ-10", "Лето", curve[0], q[0], JestcostRessor[0], d[0], n[0], l_i[0], f[0], 0.047,
                     1840, U[0], k[0], 55, Pct[0]),
    PodvizhnoySostav("ВЛ-10", "Зима", curve[0], q[0], JestcostRessor[0], d[0], n[0], l_i[0], f[0], 0.047,
                     1840, U[1], k[1], 55, Pct[0]),
    PodvizhnoySostav("ВЛ-10", "Лето", curve[1], q[0], JestcostRessor[0], d[0], n[0], l_i[0], f[1], 0.047,
                     2000, U[2], k[2], 51, Pct[0]),
    PodvizhnoySostav("ВЛ-10", "Зима", curve[1], q[0], JestcostRessor[0], d[0], n[0], l_i[0], f[1], 0.047,
                     2000, U[3], k[3], 51, Pct[0]),
    PodvizhnoySostav("8-осный", "Лето", curve[0], q[1], JestcostRessor[1], d[1], n[1], l_i[1], f[2], 0.067,

                     1840, U[0], k[0], 55, Pct[1]),
    PodvizhnoySostav("8-осный", "Зима", curve[0], q[1], JestcostRessor[1], d[1], n[1], l_i[1], f[2], 0.067,

                     1840, U[1], k[1], 55, Pct[1]),
    PodvizhnoySostav("8-осный", "Лето", curve[1], q[1], JestcostRessor[1], d[1], n[1], l_i[1], f[3], 0.067,

                     2000, U[2], k[2], 51, Pct[1]),
    PodvizhnoySostav("8-осный", "Зима", curve[1], q[1], JestcostRessor[1], d[1], n[1], l_i[1], f[3], 0.067,

                     2000, U[3], k[3], 51, Pct[1])
]

'''
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
'''
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
    inf = round(sostav.z_max()[1], 2)
    sheet.cell(row=13, column=i, value=inf)
    inf = round(sostav.z_max()[0], 2)

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
    sheet.cell(row=58, column=i, value=inf)
    inf = sostav.l_i[0]
    sheet.cell(row=59, column=i, value=inf)
    inf = sostav.l_i[1]
    sheet.cell(row=60, column=i, value=inf)
    inf = sostav.l_i[2]
    sheet.cell(row=61, column=i, value=inf)
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
    delta_t_p0_min = min(sostavs[1].delta_t_p(), sostavs[5].delta_t_p())
    sheet.cell(row=113, column=i, value=delta_t_p0_min)
    sheet.cell(row=114, column=i, value=sostav.sigma_norm(delta_t_p0_min))
    delta_t_p1_min = min(sostavs[3].delta_t_p(), sostavs[7].delta_t_p())
    sheet.cell(row=115, column=i, value=delta_t_p1_min)
    sheet.cell(row=116, column=i, value=sostav.sigma_norm(delta_t_p1_min))

    sheet.cell(row=117, column=i, value=25.2 * delta_t_p0_min)
    sheet.cell(row=118, column=i, value=25.2 * delta_t_p1_min)

# Проходим по каждому элементу в списке и проверяем значение метода delta_t_p()
    def indexxx_0():
        global sostav
        for index, sostav in enumerate(sostavs):
            if sostav.delta_t_p() == delta_t_p0_min:
                return index
    sheet.cell(row=119, column=i, value=round(sostavs[indexxx_0()].sigma_kp() * 1.3 + 25.2 * delta_t_p0_min, 2))

    def indexxx_1():
        global sostav
        for index, sostav in enumerate(sostavs):
            if sostav.delta_t_p() == delta_t_p1_min:
                return index
    sheet.cell(row=120, column=i, value=round(sostavs[indexxx_1()].sigma_kp() * 1.3 + 25.2 * delta_t_p1_min, 2))
    sigma_kp0 = sostavs[indexxx_0()].sigma_kp()
    sheet.cell(row=121, column=i, value=sigma_kp0)
    sigma_kp1 = sostavs[indexxx_1()].sigma_kp()
    sheet.cell(row=122, column=i, value=sigma_kp1)
    AA0 = sostavs[indexxx_0()].AA()[0]
    AA1 = sostavs[indexxx_0()].AA1()[0]
    P_k0 = round((AA0 * 0.9 * 1 * 1.03) / (2**AA1), 2)
    sheet.cell(row=123, column=i, value=P_k0)
    AA2 = sostavs[indexxx_1()].AA()[0]
    AA3 = sostavs[indexxx_1()].AA1()[0]
    P_k1 = round((AA2 * 0.9 * 1.08 * 1.05) / (3**AA3), 2)
    sheet.cell(row=124, column=i, value=P_k1)
    kgs0 = round(P_k0 * 101.971621297793, 2)
    sheet.cell(row=125, column=i, value=kgs0)
    kgs1 = round(P_k1 * 101.971621297793, 2)
    sheet.cell(row=126, column=i, value=kgs1)
    P_norm0 = round(kgs0 / 1.5, 2)
    sheet.cell(row=127, column=i, value=P_norm0)
    P_norm1 = round(kgs1 / 1.5, 2)
    sheet.cell(row=128, column=i, value=P_norm1)
    if sostav.rail_type == 'P50':
        F = 65.99
    else:
        F = 82.56
    sheet.cell(row=129, column=i, value=F)
    sheet.cell(row=130, column=i, value=F * 2)
    sheet.cell(row=131, column=i, value=round(P_norm0 / (25 * 2 * F), 2))
    sheet.cell(row=132, column=i, value=round(P_norm1 / (25 * 2 * F), 2))
    sheet.cell(row=133, column=i, value=(sostav.Ekv_gruzi_η()))
    sheet.cell(row=134, column=i, value=(sostav.Ekv_gruzi_µ()))
workbook_3.save('УЛЬТИМАТИВНАЯ_Формулы.xlsx')
