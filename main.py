from initial_data import PodvizhnoySostav
from openpyxl import Workbook

# ВВОЖУ ИСХОДНЫЕ ДАННЫЕ
# Локомотив/Вагон;;;
Pct = [12000, 12500]
q = [2760, 1070]
JestcostRessor = [116, 195]
d = [125, 95]
n = [2, 3]
l_i = [[300], [175, 175]]
# Локомотив:     Вагон:
# Прямая/Кривая; Прямая/Кривая
f = [1.08, 1.37, 1.13, 1.34]
Zmax = [15.6, 13.84]
# Прямая:     Кривая:
# Зима/Лето;  Зима/Лето
U = [660, 260, 690, 290]
k = [0.01403, 0.01145, 0.01441, 0.01176]

sostavs = [
    PodvizhnoySostav("ВЛ-23", "Зима", "Прямая", q[0], JestcostRessor[0], d[0], n[0], l_i[0], f[0], 0.047, Zmax[0],
                     1840, U[0], k[0], 55, Pct[0]),
    PodvizhnoySostav("ВЛ-23", "Лето", "Прямая", q[0], JestcostRessor[0], d[0], n[0], l_i[0], f[0], 0.047, Zmax[0],
                     1840, U[1], k[1], 55, Pct[0]),
    PodvizhnoySostav("ВЛ-23", "Зима", "Кривая", q[0], JestcostRessor[0], d[0], n[0], l_i[0], f[1], 0.047, Zmax[0],
                     2000, U[2], k[2], 51, Pct[0]),
    PodvizhnoySostav("ВЛ-23", "Лето", "Кривая" , q[0], JestcostRessor[0], d[0], n[0], l_i[0], f[1], 0.047, Zmax[0],
                     2000, U[3], k[3], 51, Pct[0]),
    PodvizhnoySostav("Вагон", "Зима", "Прямая", q[1], JestcostRessor[1], d[1], n[1], l_i[1], f[2], 0.067, Zmax[1],
                     1840, U[0], k[0], 55, Pct[1]),
    PodvizhnoySostav("Вагон", "Лето", "Прямая", q[1], JestcostRessor[1], d[1], n[1], l_i[1], f[2], 0.067, Zmax[1],
                     1840, U[1], k[1], 55, Pct[1]),
    PodvizhnoySostav("Вагон", "Зима", "Кривая", q[1], JestcostRessor[1], d[1], n[1], l_i[1], f[3], 0.067, Zmax[1],
                     2000, U[2], k[2], 51, Pct[1]),
    PodvizhnoySostav("Вагон", "Лето", "Кривая", q[1], JestcostRessor[1], d[1], n[1], l_i[1], f[3], 0.067, Zmax[1],
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

workbook = Workbook()
sheet = workbook.active

# РАБОТА С ЭКСЕЛЬ, ЗАПИСЬ НУЖНЫХ ДАННЫХ В ТАБЛИЦУ

for i, sostav in enumerate(sostavs, start=1):
    info = sostav.p_max_ver()
    sheet.cell(row=1, column=i, value=info)
    info = sostav.s()
    sheet.cell(row=2, column=i, value=info)
    info = sostav.s_ink()
    s = sheet.cell(row=3, column=i, value=info)
    informat = sostav.s_nnk()
    f = sheet.cell(row=4, column=i, value=informat)
    informat = sostav.s_np()
    b = sheet.cell(row=5, column=i, value=informat)
    informat = sostav.s_p()
    j = sheet.cell(row=6, column=i, value=informat)
    informat = sostav.p_cp()
    k = sheet.cell(row=7, column=i, value=informat)
    informat = sostav.p_cp_p()
    w = sheet.cell(row=8, column=i, value=informat)

workbook.save('файл.xlsx')
