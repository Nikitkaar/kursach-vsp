#import pandas as pd

# Открываем файл Excel
##alarm = workbook_15.loc[workbook_15["R"] == '700', "P65"]
#print(list(alarm.head())[0])

import pandas as pd

workbook_15 = pd.read_excel(r'C:\Users\Администратор\PycharmProjects\kursach-vsp\Лист5.xlsx')

# Преобразовываем столбец "R" в строковый тип данных
workbook_15["R"] = workbook_15["R"].astype(str)

alarm = workbook_15.loc[workbook_15["R"] == '500', "P65"]
print(list(alarm.head())[0])
