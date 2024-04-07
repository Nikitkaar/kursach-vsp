import pandas as pd



#workbook_15 = pd.read_excel(r'C:\Users\Администратор\PycharmProjects\kursach-vsp\РасчетныеХарактеристикиЛокомотивовВагонов.xlsx')
"""
# Преобразовываем столбец "G" в строковый тип данных
workbook_15["G"] = workbook_15["G"].astype(str)

alarm = workbook_15.loc[workbook_15["G"] == 'ВЛ-60']
print(list(alarm.head()))
"""

Type = "ВЛ60"
JestcostRessor = 'G'
workbook_7 = pd.read_excel(r'C:\Users\Администратор\PycharmProjects\kursach-vsp\РасчетныеХарактеристикиЛокомотивовВагонов.xlsx')

# Преобразовываем столбец "R" в строковый тип данных
#workbook_7["G"] = workbook_7["G"].astype(str)

alarm = workbook_7.loc[workbook_7["Type"] == str(Type), JestcostRessor]

