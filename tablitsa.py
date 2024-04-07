import pandas as pd

Type = ["ВЛ10", "8-миосный"]

workbook_9 = pd.read_excel(
    r'C:\Users\Администратор\PycharmProjects\kursach-vsp\Коэффициенты_f.xlsx')
list(workbook_9.loc[workbook_9["Type"] == Type[1], "Прямая"])[0]

print(list(workbook_9.loc[workbook_9["Type"] == Type[1], "Прямая"])[0])
