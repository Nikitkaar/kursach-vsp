import numpy
from openpyxl import Workbook

'''
def N_1(k, l_i):
    return round((numpy.cos(k * l_i) + numpy.sin(k * l_i)) * numpy.e ** ((-k) * l_i), 5)

def M(k, l_i):
    return (numpy.cos(k * l_i) - numpy.sin(k * l_i)) * numpy.e ** (-k * l_i)

print(round(N_1(0.015, 55), 5))


def RaschetnayaOS_N(k, l_i):
    if ((3 * numpy.pi) / (4 * k)) > l_i[0] or ((3 * numpy.pi) / (4 * k)) > l_i[1]:
        return 2
    else:
        return 1

U = [260, 500, 290, 600]
k = [0.01145, 0.0, 0.01176, 0.0]
k[1] = round((U[1]/(4*2.1*10**6*2018))**(0.25), 5)
k[3] = round((U[3]/(4*2.1*10**6*2018))**(0.25), 5)

c = [1, 2, 3]
print(N_1(0.01145, 70))
'''

from openpyxl import Workbook, load_workbook

# Предполагаем, что у вас уже есть workbook_3 и sheet
# Загружаем данные из ячеек 67 строки в список
row_values = [cell.value for cell in sheet[67]]

# Находим минимальное значение
min_value = min(row_values)

print("Минимальное значение из 67 строки:", min_value)

