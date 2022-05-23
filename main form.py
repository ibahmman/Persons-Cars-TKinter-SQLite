import tkinter as tk
import os,pyodbc
from turtle import color


dir_path = os.getcwd()

# <----- Form Settins ----->
form = tk.Tk()
form.title(dir_path)
form.geometry('800x500')
form.resizable(width=False, height=False)

# <----- Panel Window ----->
panel_right = tk.PanedWindow()
panel_right.pack(side= tk.RIGHT)

# <----- Form Objects ----->
lbl_per_name = tk.Label(master=form, text='نام')
txb_per_name = tk.Entry(master=form)
lbl_per_phone = tk.Label(master=form, text='تلفن')
txb_per_phone = tk.Entry(master=form)

lbl_car_name = tk.Label(master=form, text='خودرو')
txb_car_name = tk.Entry(master=form)
lbl_car_person__id = tk.Label(master=form, text='شناسه کاربری')
txb_car_person__id = tk.Entry(master=form)


panel_right.add(txb_per_name)
panel_right.add(lbl_per_name)

form.mainloop()