import tkinter as tk
from tkinter import ttk

class DataEntryForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.station_name = None

    def create_widgets(self):
        tk.Label(self, text="Станция:").grid(row=0, column=0)
        self.station_entry = tk.Entry(self)
        self.station_entry.grid(row=0, column=1)

        # Другие элементы ввода...

        self.submit_button = tk.Button(self, text="Получить данные", command=self.get_data)
        self.submit_button.grid(row=10, columnspan=2)

    def get_data(self):
        self.station_name = self.station_entry.get()
        print(f"Станция: {self.station_name}")

    def get_station_name(self):
        return self.station_name  # Возвращаем название станции
