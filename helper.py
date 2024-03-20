import numpy
from openpyxl import Workbook


def N_1(k, l_i):
    return (numpy.cos(k * l_i) + numpy.sin(k * l_i)) * numpy.e ** ((-k) * l_i)

def M(k, l_i):
    return (numpy.cos(k * l_i) - numpy.sin(k * l_i)) * numpy.e ** (-k * l_i)

print(round(N_1(0.015, 55), 5))


def RaschetnayaOS_N(k, l_i):
    if ((3 * numpy.pi) / (4 * k)) > l_i[0] or ((3 * numpy.pi) / (4 * k)) > l_i[1]:
        return 2
    else:
        return 1

c = [1, 2, 3]
print(c[-1])