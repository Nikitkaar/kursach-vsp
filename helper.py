import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import pandas as pd


"""def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(name="Alice", age=30, city="New York")

def my_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(1, 2, 3, name="Alice", age=30)
"""

import pandas as pd

# Чтение данных из файла Excel
df = pd.read_excel(r'C:\Users\Администратор\PycharmProjects\kursach-vsp\ОценочныеКритерииПрочностиПути.xlsx', sheet_name="Локомотив")

# Ваша переменная capacity
capacity = 20.7

# Получение критерия для capacity
if capacity > 50:
    criteria = ">50"
elif 50 >= capacity > 25:
    criteria = "50-25"
elif 25 >= capacity > 10:
    criteria = "24-10"
else:
    criteria = "<10"

# Получение значения из пересечения строки [бк] и столбца с критерием
Loko_0 = df.loc[df['Критерии'] == '[бк]', criteria].values[0]
Loko_1 = df.loc[df['Критерии'] == '[бк]', criteria].values[0]
Loko_2 = df.loc[df['Критерии'] == '[бк]', criteria].values[0]

df = pd.read_excel(r'C:\Users\Администратор\PycharmProjects\kursach-vsp\ОценочныеКритерииПрочностиПути.xlsx', sheet_name="Лист2")
Vag_0 = df.loc[df['Критерии'] == '[бк]', criteria].values[0]
Vag_1 = df.loc[df['Критерии'] == '[бк]', criteria].values[0]
Vag_2 = df.loc[df['Критерии'] == '[бк]', criteria].values[0]
print(round(Vag_0))

