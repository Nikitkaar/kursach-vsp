from New_class import Shpala
from veroyatnost_raspredel_temp import GrafVerTemp
from progibi import Grafics_progibov
from temperature_diagramm import TempDiagramm
from izgibi import Grafics_izgibov
from initial_data import PodvizhnoySostav
from openpyxl import Workbook
from User_Interface import DataEntryForm  # Импортируйте ваш класс пользовательского интерфейса
from tkinter import messagebox
import pandas as pd
import tkinter as tk
from tkinter import ttk

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Ввод данных")
        self.geometry("400x300")

        # Создаем экземпляр DataEntryForm и размещаем его
        self.data_entry_form = DataEntryForm(master=self)
        self.data_entry_form.pack()

        # Создаем кнопку для выполнения расчета
        ttk.Button(self, text="Выполнить расчет", command=self.calculate).pack(pady=10)

    def calculate(self):
        # Получаем значение станции из DataEntryForm
        station = self.data_entry_form.get_station_name()

        if not station:
            messagebox.showwarning("Ошибка", "Пожалуйста, введите название станции.")
            return

        # Чтение данных из файла Excel
        try:
            first_data = pd.read_excel(r'C:\Users\Администратор\PycharmProjects\kursach-vsp\ввод_исходных_данных.xlsx', sheet_name="Дополненное_издание(25")
            redaction = list(first_data.loc[first_data[1] == 21, "I"])[0]
            # Здесь можно использовать введенную станцию
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при чтении файла: {e}")
            return

        # Создание Excel файла для записи данных
        workbook = Workbook()
        sheet = workbook.active

        # Замените на ваш процесс записи данных
        for i, sostav in enumerate(['Example1', 'Example2'], start=1):  # Замените на ваши данные
            sheet.cell(row=147, column=i, value=station)  # Используйте полученную переменную station

        # Сохранение файла
        workbook.save(r'C:\Users\Администратор\PycharmProjects\kursach-vsp\output.xlsx')

        # Вывод результатов
        messagebox.showinfo("Результаты", f"Станция: {station} записана в файл.")

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()



# Чтение данных из файла Excel
first_data = pd.read_excel(r'C:\Users\Администратор\PycharmProjects\kursach-vsp\ввод_исходных_данных.xlsx', sheet_name="Дополненное_издание(25")
redaction = list(first_data.loc[first_data[1] == 21, "I"])[0]
#station = list(first_data.loc[first_data[1] == 2, "I"])[0]
t_min_min = list(first_data.loc[first_data[1] == 6, "I"])[0]
t_max_max = list(first_data.loc[first_data[1] == 7, "I"])[0]
Ta = t_max_max - t_min_min
rail_type = list(first_data.loc[first_data[1] == 17, "I"])[0]
v = list(first_data.loc[first_data[1] == 5, "I"])[0]
val = list(first_data.loc[first_data[1] == 19, "I"])[0]  # РУЧНОЙ ВВОД ИЗ Таблицы (номер строки выбора характеристик пути, в зависимости от его конструкции)
          # Железобетон: Р65 - 10; Р50 - 12       Дерево: Р65 - 17; Р50 - 23
capacity = list(first_data.loc[first_data[1] == 20, "I"])[0]
material_of_sleepers = list(first_data.loc[first_data[1] == 16, "I"])[0]
h = list(first_data.loc[first_data[1] == 18, "I"])[0]
Type = [list(first_data.loc[first_data[1] == 3, "I"])[0], list(first_data.loc[first_data[1] == 3, "II"])[0]]  # РУЧНОЙ ВВОД ИЗ ДАНО
t_opt = list(first_data.loc[first_data[1] == 27, "I"])[0]

# Чтение данных из файла Excel
df = pd.read_excel(r'C:\Users\Администратор\PycharmProjects\kursach-vsp\ОценочныеКритерииПрочностиПути.xlsx', sheet_name="Локомотив")


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
Loko_0 = df.loc[df['Критерии'] == '[бкр]', criteria].values[0]
Loko_1 = df.loc[df['Критерии'] == '[бш]', criteria].values[0]
Loko_2 = df.loc[df['Критерии'] == '[бб]', criteria].values[0]

df = pd.read_excel(r'C:\Users\Администратор\PycharmProjects\kursach-vsp\ОценочныеКритерииПрочностиПути.xlsx', sheet_name="Лист2")
Vag_0 = df.loc[df['Критерии'] == '[бкр]', criteria].values[0]
Vag_1 = df.loc[df['Критерии'] == '[бш]', criteria].values[0]
Vag_2 = df.loc[df['Критерии'] == '[бб]', criteria].values[0]
Vag_3 = df.loc[df['Критерии'] == '[бз]', criteria].values[0]


workbook_7 = pd.read_excel(
    r'C:\Users\Администратор\PycharmProjects\kursach-vsp\РасчетныеХарактеристикиЛокомотивовВагонов.xlsx')
alarm = list(workbook_7.loc[workbook_7["Type"] == Type[0], 'Pct'])[0]
alarms_0 = list(workbook_7.loc[workbook_7["Type"] == Type[0], 'q'])[0]
alarms_1 = list(workbook_7.loc[workbook_7["Type"] == Type[1], 'q'])[0]
alarms_2 = workbook_7.loc[workbook_7["Type"] == Type[0], 'G']
alarms_3 = workbook_7.loc[workbook_7["Type"] == Type[1], 'G']
alarms_4 = workbook_7.loc[workbook_7["Type"] == Type[0], 'd']
alarms_5 = workbook_7.loc[workbook_7["Type"] == Type[1], 'd']
alarms_6 = workbook_7.loc[workbook_7["Type"] == Type[0], 'n']
alarms_7 = workbook_7.loc[workbook_7["Type"] == Type[1], 'n']
alarms_8 = workbook_7.loc[workbook_7["Type"] == Type[0], 'l_i']
fcr_vag = list(workbook_7.loc[workbook_7["Type"] == Type[1], 'fсг'])[0]
fcr_loc = list(workbook_7.loc[workbook_7["Type"] == Type[0], 'fсг'])[0]

if redaction == "new" and redaction != "old" and redaction != None:
    kd = [list(first_data.loc[first_data[1] == 11, "I"])[0], round(0.1+(0.2*(v / fcr_vag)), 2)]   # ВВОД ИСХОДНЫХ ДАННЫХ
else:
    kd = [0, 0]
# Разделить строку по запятым и преобразовать каждый элемент в числовой формат
alarms_8_1 = [int(x) for x in list(alarms_8)[0].split(',')]
alarms_9 = workbook_7.loc[workbook_7["Type"] == Type[1], 'l_i']
alarms_9_1 = [int(x) for x in list(alarms_9)[0].split(',')]

workbook_8 = pd.read_excel(r'C:\Users\Администратор\PycharmProjects\kursach-vsp\РасчетныеХарактеристикиПути.xlsx')
val_0 = list(workbook_8.loc[workbook_8["№"] == val, 'U'])[0]
val_1 = list(workbook_8.loc[workbook_8["№"] == val - 1, 'U'])[0]
val_2 = list(workbook_8.loc[workbook_8["№"] == val, 'k'])[0]
val_3 = list(workbook_8.loc[workbook_8["№"] == val - 1, 'k'])[0]
L = float(list(workbook_8.loc[workbook_8["№"] == val, 'L'])[0])
alfa1 = list(workbook_8.loc[workbook_8["№"] == val - 1, 'α1'])[0]
epsiland = list(workbook_8.loc[workbook_8["№"] == val - 1, 'eps'])[0]
betaa = list(workbook_8.loc[workbook_8["№"] == val - 1, 'beta'])[0]
gamma = list(workbook_8.loc[workbook_8["№"] == val - 1, 'gamma'])[0]

W = int(list(workbook_8.loc[workbook_8["№"] == val, 'W(6)'])[0])
alpha0 = float(list(workbook_8.loc[workbook_8["№"] == val, 'α0'])[0])
omega = int(list(workbook_8.loc[workbook_8["№"] == val, 'ω'])[0])
omega_a = int(list(workbook_8.loc[workbook_8["№"] == val, 'Ωа'])[0])
b = float(list(workbook_8.loc[workbook_8["№"] == val, 'b'])[0])
ae = float(list(workbook_8.loc[workbook_8["№"] == val, 'æ'])[0])


# ВВОЖУ ИСХОДНЫЕ ДАННЫЕ
# Локомотив/Вагон;
P_ct = [alarm, list(first_data.loc[first_data[1] == 4, "II"])[0]]  # РУЧНОЙ ВВОД ИЗ ДАНО
q = [alarms_0, alarms_1]
JestcostRessor = [list(alarms_2)[0], list(alarms_3)[0]]
d = [list(alarms_4)[0], list(alarms_5)[0]]
n = [list(alarms_6)[0], list(alarms_7)[0]]
l_i = [list(alarms_8_1), list(alarms_9_1)]
curve = ["Прямая", list(first_data.loc[first_data[1] == 13, "II"])[0]]  # РУЧНОЙ ВВОД ИЗ ДАНО
Pmax_p = [float(kd[0]*(P_ct[0] - q[0])), float(kd[1]*(P_ct[1] - q[1]))]
# Прямая, Лето\Зима:     Кривая, Лето\Зима:
U = [val_0, list(first_data.loc[first_data[1] == 15, "I"])[0], val_1, list(first_data.loc[first_data[1] == 15, "II"])[0]]  # РУЧНОЙ ВВОД
k = [val_2, 0.0, val_3, 0.0]

if rail_type == 'P50' or rail_type == 'Р50':
    J0 = 2018
elif rail_type == 'P65' or rail_type == 'Р65':
    J0 = 3547
else:
    J0 = 4490

k[1] = round((U[1] / (4 * 2.1 * 10 ** 6 * J0)) ** 0.25, 5)
k[3] = round((U[3] / (4 * 2.1 * 10 ** 6 * J0)) ** 0.25, 5)
workbook_9 = pd.read_excel(
    r'C:\Users\Администратор\PycharmProjects\kursach-vsp\Коэффициенты_f.xlsx')
f0 = list(workbook_9.loc[workbook_9["Type"] == Type[0], curve[0]])[0]
f1 = list(workbook_9.loc[workbook_9["Type"] == Type[0], curve[1]])[0]
f2 = list(workbook_9.loc[workbook_9["Type"] == Type[1], curve[0]])[0]
f3 = list(workbook_9.loc[workbook_9["Type"] == Type[1], curve[1]])[0]
# Локомотив:     Вагон:
# Прямая/Кривая; Прямая/Кривая
if redaction == "new" and redaction != "old":   # при новой редакции ребята обычно сами дают значения f
#f = [f0, f1, f2, f3]
    f = [list(first_data.loc[first_data[1] == 9, "I"])[0], list(first_data.loc[first_data[1] == 10, "I"])[0],
         list(first_data.loc[first_data[1] == 9, "II"])[0], list(first_data.loc[first_data[1] == 10, "II"])[0]]
else:
    f = [f0, f1, f2, f3]


sostavs = [
    PodvizhnoySostav(type_sostav=Type[0], season="Лето", curve=curve[0], q=q[0], JestcostRessor=JestcostRessor[0],
                     d=d[0], n=n[0], l_i=l_i[0], f=f[0], e=0.047, u=U[2], k=k[2], P_ct=P_ct[0], l_sh=55, v=v, L=L,
                     alpha0=alpha0, W=W, rail_type=rail_type, material_of_sleepers=material_of_sleepers, omega=omega,
                     omega_a=omega_a, b=b, ae=ae, h=h, fcr=fcr_loc, kd=kd[0], redaction = redaction),
    PodvizhnoySostav(type_sostav=Type[0], season="Зима", curve=curve[0], q=q[0], JestcostRessor=JestcostRessor[0],
                     d=d[0], n=n[0], l_i=l_i[0], f=f[0], e=0.047, u=U[1], k=k[1], P_ct=P_ct[0], l_sh=55, v=v, L=L,
                     alpha0=alpha0, W=W, rail_type=rail_type, material_of_sleepers=material_of_sleepers, omega=omega,
                     omega_a=omega_a, b=b, ae=ae, h=h, fcr=fcr_loc, kd=kd[0], redaction = redaction),
    PodvizhnoySostav(type_sostav=Type[0], season="Лето", curve=curve[1], q=q[0], JestcostRessor=JestcostRessor[0],
                     d=d[0], n=n[0], l_i=l_i[0], f=f[1], e=0.047, u=U[0], k=k[0], P_ct=P_ct[0], l_sh=51, v=v, L=L,
                     alpha0=alpha0, W=W, rail_type=rail_type, material_of_sleepers=material_of_sleepers,
                     omega=omega, omega_a=omega_a, b=b, ae=ae, h=h, fcr=fcr_loc, kd=kd[0], redaction = redaction),
    PodvizhnoySostav(type_sostav=Type[0], season="Зима", curve=curve[1], q=q[0], JestcostRessor=JestcostRessor[0],
                     d=d[0], n=n[0], l_i=l_i[0], f=f[1], e=0.047, u=U[3], k=k[3], P_ct=P_ct[0], l_sh=51, v=v, L=L,
                     alpha0=alpha0, W=W, rail_type=rail_type, material_of_sleepers=material_of_sleepers,
                     omega=omega, omega_a=omega_a, b=b, ae=ae, h=h, fcr=fcr_loc, kd=kd[0], redaction = redaction),
    PodvizhnoySostav(type_sostav=Type[1], season="Лето", curve=curve[0], q=q[1], JestcostRessor=JestcostRessor[1],
                     d=d[1], n=n[1], l_i=l_i[1], f=f[2], e=0.067, u=U[2], k=k[2], P_ct=P_ct[1], l_sh=55, v=v, L=L,
                     alpha0=alpha0, W=W, rail_type=rail_type, material_of_sleepers=material_of_sleepers, omega=omega,
                     omega_a=omega_a, b=b, ae=ae, h=h, fcr=fcr_vag, kd=kd[1], redaction = redaction),
    PodvizhnoySostav(type_sostav=Type[1], season="Зима", curve=curve[0], q=q[1], JestcostRessor=JestcostRessor[1],
                     d=d[1], n=n[1], l_i=l_i[1], f=f[2], e=0.067, u=U[1], k=k[1], P_ct=P_ct[1], l_sh=55, v=v, L=L,
                     alpha0=alpha0, W=W, rail_type=rail_type, material_of_sleepers=material_of_sleepers, omega=omega,
                     omega_a=omega_a, b=b, ae=ae, h=h, fcr=fcr_vag, kd=kd[1], redaction = redaction),
    PodvizhnoySostav(type_sostav=Type[1], season="Лето", curve=curve[1], q=q[1], JestcostRessor=JestcostRessor[1],
                     d=d[1], n=n[1], l_i=l_i[1], f=f[3], e=0.067, u=U[0], k=k[0], P_ct=P_ct[1], l_sh=51, v=v, L=L,
                     alpha0=alpha0, W=W, rail_type=rail_type, material_of_sleepers=material_of_sleepers, omega=omega,
                     omega_a=omega_a, b=b, ae=ae, h=h, fcr=fcr_vag, kd=kd[1], redaction = redaction),
    PodvizhnoySostav(type_sostav=Type[1], season="Зима", curve=curve[1], q=q[1], JestcostRessor=JestcostRessor[1],
                     d=d[1], n=n[1], l_i=l_i[1], f=f[3], e=0.067, u=U[3], k=k[3], P_ct=P_ct[1], l_sh=51, v=v, L=L,
                     alpha0=alpha0, W=W, rail_type=rail_type, material_of_sleepers=material_of_sleepers, omega=omega,
                     omega_a=omega_a, b=b, ae=ae, h=h, fcr=fcr_vag, kd=kd[1], redaction = redaction),
]

"""Минимальные температуры на прямой и кривой соответственно"""
delta_t_p0_min = min(sostavs[1].delta_t_p(), sostavs[5].delta_t_p())
delta_t_p1_min = min(sostavs[3].delta_t_p(), sostavs[7].delta_t_p())


def indexxx_0():
    """возвращаем индекс sostavs, с минимальным delta_t_p на прямой"""
    global sostav
    for index, sostav in enumerate(sostavs):
        if sostav.delta_t_p() == delta_t_p0_min:
            return index

def indexxx_1():
    """возвращаем индекс sostavs, с минимальным delta_t_p на кривой"""
    global sostav
    for index, sostav in enumerate(sostavs):
        if sostav.delta_t_p() == delta_t_p1_min:
            return index


if rail_type == 'P50':
    "Площадь поперечного сечения рельса"
    F = 65.99
else:
    F = 82.56

# РАБОТА С ЭКСЕЛЬ, ЗАПИСЬ ДАННЫХ В ТАБЛИЦУ (с помощью специальной вставки они переходят в ворд-документ отчета)
# ГЛАВНАЯ ТАБЛИЦА

workbook_3 = Workbook()
sheet = workbook_3.active

for i, sostav in enumerate(sostavs, start=1):

    sheet.cell(row=1, column=4, value=Type[0])
    sheet.cell(row=1, column=5, value=Type[1])

    sheet.cell(row=2, column=i, value=sostav.curve)

    sheet.cell(row=3, column=i, value=sostav.season)

    sheet.cell(row=4, column=4, value=P_ct[0])
    sheet.cell(row=4, column=5, value=P_ct[1])
    sheet.cell(row=4, column=6, value="Pcт")

    sheet.cell(row=5, column=1, value=v)
    sheet.cell(row=5, column=2, value="Скорость")

    sheet.cell(row=6, column=4, value=q[0])
    sheet.cell(row=6, column=5, value=q[1])
    sheet.cell(row=6, column=6, value="q")

    sheet.cell(row=7, column=4, value=JestcostRessor[0])
    sheet.cell(row=7, column=5, value=JestcostRessor[1])
    sheet.cell(row=7, column=6, value="JestcostRessor")

    sheet.cell(row=8, column=4, value=d[0])
    sheet.cell(row=8, column=5, value=d[1])
    sheet.cell(row=8, column=6, value="d")

    sheet.cell(row=9, column=4, value=n[0])
    sheet.cell(row=9, column=5, value=n[1])
    sheet.cell(row=9, column=i, value="n")

    sheet.cell(row=10, column=i, value=rail_type)

    sheet.cell(row=11, column=i, value=round(sostav.f, 2))
    sheet.cell(row=11, column=9, value="f")

    sheet.cell(row=12, column=4, value=sostavs[0].e)
    sheet.cell(row=12, column=5, value=sostavs[4].e)
    sheet.cell(row=12, column=6, value="e")

    sheet.cell(row=13, column=4, value=sostavs[0].z_max()[1])
    sheet.cell(row=13, column=5, value=sostavs[4].z_max()[1])
    sheet.cell(row=13, column=6, value="z_max")

    sheet.cell(row=133, column=i, value= sostav.Ekv_gruzi_η())
    sheet.cell(row=133, column=9, value="Ekv_gruzi_η")

    sheet.cell(row=134, column=i, value= sostav.Ekv_gruzi_µ())
    sheet.cell(row=134, column=9, value="Ekv_gruzi_µ")

    if sostav.n == 4:
        inf = f'{sostav.l_i[0]}+{sostav.l_i[1]}+{sostav.l_i[2]}'
    elif sostav.n == 3:
        inf = f'{sostav.l_i[0]}+{sostav.l_i[1]}'
    else:
        inf = str(sostav.l_i[0])
    sheet.cell(row=14, column=i, value=inf)

    sheet.cell(row=15, column=4, value=round(sostavs[0].z_max()[0], 2))
    sheet.cell(row=15, column=5, value=round(sostavs[4].z_max()[0], 2))
    sheet.cell(row=15, column=6, value="z_max")

    sheet.cell(row=16, column=i, value=material_of_sleepers)

    sheet.cell(row=17, column=i, value=sostav.u)
    sheet.cell(row=17, column=9, value="u")

    sheet.cell(row=18, column=i, value=sostav.k)
    sheet.cell(row=18, column=9, value="k")

    sheet.cell(row=19, column=1, value=L)
    sheet.cell(row=19, column=2, value="L")

    sheet.cell(row=20, column=i, value= sostav.W)

    sheet.cell(row=21, column=i, value= sostav.alpha0)

    sheet.cell(row=22, column=i, value= sostav.omega)

    sheet.cell(row=23, column=i, value= sostav.omega_a)

    sheet.cell(row=24, column=i, value= sostav.b)

    inf = sostav.p_max_p()
    sheet.cell(row=25, column=i, value=inf)
    sheet.cell(row=25, column=9, value='p_max_p')

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
    sheet.cell(row=33, column=9, value='p_max_ver')

    inf = sostav.pi_4k()
    sheet.cell(row=34, column=i, value=inf)

    inf = sostav.pi_5_4k()
    sheet.cell(row=35, column=i, value=inf)

    inf = sostav.pi_3_4k()
    sheet.cell(row=36, column=i, value=inf)

    inf = sostav.pi_7_4k()
    sheet.cell(row=37, column=i, value=inf)

    inf = round(sostav.P_I_ekv(), 0)
    sheet.cell(row=38, column=i, value=inf)

    inf = sostav.Muu2()
    sheet.cell(row=39, column=i, value=inf)

    inf = sostav.Muu3()
    sheet.cell(row=40, column=i, value=inf)

    inf = sostav.Muu4()
    sheet.cell(row=41, column=i, value=inf)

    inf = sostav.Sigma_Muu()
    sheet.cell(row=42, column=i, value=inf)

    inf = round(sostav.P_II_ekv())
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
    sheet.cell(row=48, column=9, value="номер оси n")

    inf = sostav.sigma_kp()
    sheet.cell(row=49, column=i, value=inf)

    inf = sostav.sigma_sh()
    sheet.cell(row=50, column=i, value=inf)

    inf = sostav.sigma_br()
    sheet.cell(row=51, column=i, value=inf)

    inf = sostav.ae
    sheet.cell(row=52, column=i, value=inf)

    sheet.cell(row=53, column=i, value=sostav.NNN(55))
    sheet.cell(row=53, column=9, value="Тета от длинны шпалы")

    sheet.cell(row=54, column=i, value=J0)
    sheet.cell(row=54, column=9, value="Момент инерции рельса")

    inf = sostav.m()
    sheet.cell(row=55, column=i, value=inf)

    inf = sostav.sigma_h2()
    sheet.cell(row=56, column=i, value=inf)
    sheet.cell(row=56, column=9, value="sigma_h2()")




    sheet.cell(row=57, column=i, value=sostav.A())
    sheet.cell(row=57, column=9, value='А, коэффициент расстояния между шпал')

    sheet.cell(row=58, column=i, value=sostav.C1())
    sheet.cell(row=58, column=9, value='C1')

    inf = sostav.l_i[0]
    sheet.cell(row=59, column=i, value=inf)
    sheet.cell(row=59, column=9, value='l_i[0]')

    inf = sostav.l_i[1]
    sheet.cell(row=60, column=i, value=inf)
    sheet.cell(row=60, column=9, value='l_i[1]')

    inf = sostav.l_i[2]
    sheet.cell(row=61, column=i, value=inf)
    sheet.cell(row=61, column=9, value='l_i[2]')

    sheet.cell(row=63, column=8, value=h)
    sheet.cell(row=63, column=9, value='высота насыпи')

    sheet.cell(row=62, column=i, value=Vag_3)
    sheet.cell(row=62, column=9, value='[бз_Вагон]')

    inf = sostav.C2()
    sheet.cell(row=64, column=i, value=inf)
    sheet.cell(row=64, column=9, value='C2')

    inf = sostav.delta_t_p()
    sheet.cell(row=67, column=i, value=inf)
    sheet.cell(row=67, column=9, value="[∆t_р]")

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

    sheet.cell(row=75, column=1, value=Loko_0)
    sheet.cell(row=76, column=1, value=Loko_1)
    sheet.cell(row=77, column=1, value=Loko_2)
    sheet.cell(row=75, column=2, value="Loko_[бкр]")
    sheet.cell(row=76, column=2, value="Loko_[бш]")
    sheet.cell(row=77, column=2, value="Loko_[бб]")

    sheet.cell(row=78, column=1, value=Vag_0)
    sheet.cell(row=79, column=1, value=Vag_1)
    sheet.cell(row=80, column=1, value=Vag_2)
    sheet.cell(row=78, column=2, value="Vag_[бкр]")
    sheet.cell(row=79, column=2, value="Vag_[бш]")
    sheet.cell(row=80, column=2, value="Vag_[бб]")

    inf = sostav.xn()[2]
    sheet.cell(row=81, column=i, value=inf)
    sheet.cell(row=81, column=9, value="xn")

    inf = round(sostav.summa1(), 5)
    sheet.cell(row=82, column=i, value=inf)
    sheet.cell(row=82, column=9, value="сигма тета 1 шпала")

    sheet.cell(row=83, column=i, value=fcr_loc)
    sheet.cell(row=83, column=9, value='fcr_loc')

    sheet.cell(row=84, column=i, value=fcr_vag)
    sheet.cell(row=84, column=9, value='fcr_vag')

    sheet.cell(row=85, column=i, value=alfa1)
    sheet.cell(row=85, column=9, value='alfa1')

    sheet.cell(row=86, column=i, value=betaa)
    sheet.cell(row=86, column=9, value='Beta')

    sheet.cell(row=87, column=i, value=gamma)
    sheet.cell(row=87, column=9, value='Gamma')

    sheet.cell(row=88, column=i, value=epsiland)
    sheet.cell(row=88, column=9, value='Epsiland')

    sheet.cell(row=89, column=i, value=kd[0])
    sheet.cell(row=89, column=9, value='kd_loc')

    sheet.cell(row=90, column=i, value=kd[1])
    sheet.cell(row=90, column=9, value='kd_vag')

    sheet.cell(row=96, column=i, value=sostav.p_max_p_zmax())
    sheet.cell(row=96, column=9, value='Pmax_p_zmax')

    sheet.cell(row=97, column=i, value=sostav.p_max_p_kd())
    sheet.cell(row=97, column=9, value='Pmax_p_kd')



    inf = round(sostav.summa2(), 5)
    sheet.cell(row=95, column=i, value=inf)
    sheet.cell(row=95, column=9, value="сигма тета 3 шпала")

    inf = sostav.P_II_ekvONE()
    sheet.cell(row=100, column=i, value=inf)
    sheet.cell(row=100, column=9, value="P_II_ekvONE")

    inf = sostav.P_II_ekvThree()
    sheet.cell(row=101, column=i, value=inf)
    sheet.cell(row=101, column=9, value="P_II_ekvThree")

    inf = sostavs[4].sigma_b1()
    sheet.cell(row=102, column=i, value=inf)
    sheet.cell(row=102, column=9, value='sigma_b1')

    inf = sostavs[4].sigma_h1()
    sheet.cell(row=103, column=i, value=inf)
    sheet.cell(row=103, column=9, value='sigma_h1')

    inf = sostavs[4].sigma_b3()
    sheet.cell(row=104, column=i, value=inf)
    sheet.cell(row=104, column=9, value='sigma_b3')

    inf = sostavs[4].sigma_h3()
    sheet.cell(row=105, column=i, value=inf)
    sheet.cell(row=105, column=9, value='sigma_h3')

    inf = sostavs[4].sigma_h()
    sheet.cell(row=106, column=i, value=inf)
    sheet.cell(row=106, column=9, value="∑_h")

    inf = sostav.AA()[0]
    sheet.cell(row=107, column=i, value=inf)
    sheet.cell(row=107, column=9, value="Параметр А Першин")

    inf = sostav.AA1()[0]
    sheet.cell(row=108, column=i, value=inf)
    sheet.cell(row=108, column=9, value="Параметр µ Першин")

    sheet.cell(row=113, column=i, value=delta_t_p0_min)
    sheet.cell(row=113, column=9, value="[∆t_р_min]Прямая")
    sheet.cell(row=114, column=i, value=round(sostavs[indexxx_0()].sigma_kp() * 1.3 + 25.2 * delta_t_p0_min, 2))
    sheet.cell(row=114, column=9, value="нормальные суммарные напряжения(Прямая)")

    sheet.cell(row=115, column=i, value=delta_t_p1_min)
    sheet.cell(row=115, column=9, value="[∆t_р_min]Кривая")
    sheet.cell(row=116, column=i, value=round(sostavs[indexxx_1()].sigma_kp() * 1.3 + 25.2 * delta_t_p1_min, 2))
    sheet.cell(row=116, column=9, value="нормальные суммарные напряжения(Кривая)")

    sheet.cell(row=135, column=i, value=sostavs[4].Ekv_gruzi_η_shpala_1())
    sheet.cell(row=135, column=9, value="Ekv_gruzi_η_shpala_1")

    sheet.cell(row=136, column=i, value=sostavs[4].Ekv_gruzi_η_shpala_3())
    sheet.cell(row=136, column=9, value="Ekv_gruzi_η_shpala_3")

    sheet.cell(row=117, column=i, value=25.2 * delta_t_p0_min)
    sheet.cell(row=118, column=i, value=25.2 * delta_t_p1_min)
    sheet.cell(row=117, column=9, value="σ_t(Прямая)")
    sheet.cell(row=118, column=9, value="σ_t(Кривая)")

    sigma_kp0 = sostavs[indexxx_0()].sigma_kp()
    sheet.cell(row=121, column=i, value=sigma_kp0)
    sheet.cell(row=121, column=9, value="σ_кп^зима_ПРямая")

    sigma_kp1 = sostavs[indexxx_1()].sigma_kp()
    sheet.cell(row=122, column=i, value=sigma_kp1)
    sheet.cell(row=122, column=9, value="σ_кп^зима_Кривая")

    AA0 = sostavs[indexxx_0()].AA()[0]
    AA1 = sostavs[indexxx_0()].AA1()[0]
    P_k0 = round((AA0 * 0.9 * 1 * 1.03) / (2 ** AA1), 2)
    sheet.cell(row=123, column=i, value=P_k0)
    sheet.cell(row=123, column=9, value="критическая температурная сила Pк(Прямая)")

    AA2 = sostavs[indexxx_1()].AA()[0]
    AA3 = sostavs[indexxx_1()].AA1()[0]
    P_k1 = round((AA2 * 0.9 * 1.08 * 1.05) / (3 ** AA3), 2)
    sheet.cell(row=124, column=i, value=P_k1)
    sheet.cell(row=124, column=9, value="критическая температурная сила Pк(Кривая)")

    kgs0 = round(P_k0 * 101.971621297793, 2)
    sheet.cell(row=125, column=i, value=kgs0)
    sheet.cell(row=125, column=9, value="Pк(Прямая)кгс")

    kgs1 = round(P_k1 * 101.971621297793, 2)
    sheet.cell(row=126, column=i, value=kgs1)
    sheet.cell(row=126, column=9, value="Pк(Кривая)кгс")

    P_norm0 = round(kgs0 / 1.5, 2)
    sheet.cell(row=127, column=i, value=P_norm0)
    sheet.cell(row=127, column=9, value="[P]Прямая")

    P_norm1 = round(kgs1 / 1.5, 2)
    sheet.cell(row=128, column=i, value=P_norm1)
    sheet.cell(row=128, column=9, value="[P]Кривая")

    sheet.cell(row=129, column=i, value=F)
    sheet.cell(row=129, column=9, value="F")

    sheet.cell(row=130, column=i, value=F * 2)
    sheet.cell(row=130, column=9, value="F * 2")

    t_y = round(P_norm0 / (25 * 2 * F))
    sheet.cell(row=131, column=i, value=t_y)
    sheet.cell(row=131, column=9, value="[∆t_уПрямая]")
    t_y_curve = round(P_norm1 / (25 * 2 * F))
    sheet.cell(row=132, column=i, value=t_y_curve)
    sheet.cell(row=132, column=9, value="[∆t_у_curve]")


    sheet.cell(row=141, column=i, value=delta_t_p0_min + round(P_norm0 / (25 * 2 * F), 2) - 10)
    sheet.cell(row=141, column=9, value="[T] прямая")
    sheet.cell(row=140, column=i, value=delta_t_p1_min + round(P_norm1 / (25 * 2 * F), 2) - 10)
    sheet.cell(row=140, column=9, value="[T] кривая")
    sheet.cell(row=139, column=i, value=Ta)
    sheet.cell(row=139, column=9, value="Tа")
    sheet.cell(row=138, column=i, value=t_min_min)
    sheet.cell(row=138, column=9, value="t_min_min")
    sheet.cell(row=137, column=i, value=t_max_max)
    sheet.cell(row=137, column=9, value="t_max_max")

    t_max_zakr = min(t_min_min + delta_t_p0_min, t_max_max)
    sheet.cell(row=142, column=i, value=t_max_zakr)
    sheet.cell(row=142, column=9, value="t_max_zakr")
    t_max_zakr_curve = min(t_min_min + delta_t_p1_min, t_max_max)
    sheet.cell(row=143, column=i, value=t_max_zakr_curve)
    sheet.cell(row=143, column=9, value="t_max_zakr_curve")
    t_min_zakr = max(t_max_max - t_y, t_min_min)
    sheet.cell(row=144, column=i, value=t_min_zakr)
    sheet.cell(row=144, column=9, value='t_min_zakr')
    t_min_zakr_curve = max(t_max_max - t_y_curve, t_min_min)
    sheet.cell(row=145, column=i, value=t_min_zakr_curve)
    sheet.cell(row=145, column=9, value='t_min_zakr_curve')
    sheet.cell(row=146, column=9, value='Грузонапряженность')
    sheet.cell(row=146, column=i, value=capacity)
    sheet.cell(row=147, column=9, value='Станция')
    sheet.cell(row=147, column=i, value=station)

    vvv = GrafVerTemp(t_max_max=t_max_max, t_min_min=t_min_min,
                       t_min_zakr=min(t_min_zakr, t_min_zakr_curve), t_max_zakr=t_max_zakr,
                       t_y=min(t_y, t_y_curve), delta_t_p=min(delta_t_p1_min, delta_t_p0_min), t_opt=t_opt)
    vvv.grafic_maker_()


    aaa = TempDiagramm(t_max_max=t_max_max, t_min_min=t_min_min, t_y_curve=t_y_curve, curve=curve[1],
                       t_min_zakr=t_min_zakr, t_max_zakr=t_max_zakr, t_min_zakr_curve=t_min_zakr_curve,
                       t_max_zakr_curve=t_max_zakr_curve, t_y=t_y, delta_t_p1_min=delta_t_p1_min,
                       delta_t_p0_min=delta_t_p0_min)
    aaa.grafic_maker()


# Уже заняты 133 и 134
# Почему-то возвращают только первое вхождение если строки кода стоят здесь, а не выше

workbook_3.save('УЛЬТИМАТИВНАЯ_Формулы.xlsx')

xxx = Shpala(sostavs=sostavs[4])
xxx.grafic()  # Вызов метода для построения графиков

yyy = Grafics_progibov(sostavs=sostavs, k = k)
yyy.grafic_mader()

zzz = Grafics_izgibov(sostavs=sostavs, k = k)
zzz.grafic_mader_()

