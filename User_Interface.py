import tkinter as tk
from tkinter import ttk

class DataEntryForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.create_widgets()
        self.station_name = None  # Переменная для хранения названия станции

    def create_widgets(self):
        # Создаем метки и поля ввода для каждого параметра
        tk.Label(self, text="Станция:").grid(row=0, column=0)
        self.station_entry = tk.Entry(self)
        self.station_entry.grid(row=0, column=1)

        tk.Label(self, text="t_min_min:").grid(row=1, column=0)
        self.t_min_min_entry = tk.Entry(self)
        self.t_min_min_entry.grid(row=1, column=1)

        tk.Label(self, text="t_max_max:").grid(row=2, column=0)
        self.t_max_max_entry = tk.Entry(self)
        self.t_max_max_entry.grid(row=2, column=1)

        tk.Label(self, text="Тип рельсов:").grid(row=3, column=0)
        self.rail_type_combobox = ttk.Combobox(self, values=["Р50", "Р65", "Р75"])
        self.rail_type_combobox.grid(row=3, column=1)

        tk.Label(self, text="Скорость v:").grid(row=4, column=0)
        self.v_entry = tk.Entry(self)
        self.v_entry.grid(row=4, column=1)

        tk.Label(self, text="Вал (из таблицы):").grid(row=5, column=0)
        self.val_entry = tk.Entry(self)
        self.val_entry.grid(row=5, column=1)

        tk.Label(self, text="Грузоподъемность:").grid(row=6, column=0)
        self.capacity_entry = tk.Entry(self)
        self.capacity_entry.grid(row=6, column=1)

        tk.Label(self, text="Материал шпал:").grid(row=7, column=0)
        self.material_of_sleepers_combobox = ttk.Combobox(self, values=["Железобетон", "Дерево"])
        self.material_of_sleepers_combobox.grid(row=7, column=1)

        tk.Label(self, text="Высота h:").grid(row=8, column=0)
        self.h_entry = tk.Entry(self)
        self.h_entry.grid(row=8, column=1)

        tk.Label(self, text="Тип поезда:").grid(row=9, column=0)
        self.type_entry = tk.Entry(self)
        self.type_entry.grid(row=9, column=1)

        # Кнопка для получения значений
        self.submit_button = tk.Button(self, text="Получить данные", command=self.get_data)
        self.submit_button.grid(row=10, columnspan=2)

    def get_data(self):
        # Получаем данные из поля ввода станции
        self.station_name = self.station_entry.get()  # Сохраняем название станции в переменной класса
        print(f"Станция: {self.station_name}")  # Печатаем название станции

if __name__ == "__main__":
    root = tk.Tk()
    app = DataEntryForm(master=root)
    app.mainloop()

    # Теперь вы можете получить название станции из переменной класса
    x = app.station_name
    print(x)