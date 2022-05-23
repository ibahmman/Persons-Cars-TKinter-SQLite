import tkinter as tk
import os,pyodbc


dir_path = os.getcwd()

# <----- Form Settins ----->
form = tk.Tk()
form.title(dir_path)
form.geometry('800x500')
form.resizable(width=False, height=False)

# <----- Form Objects ----->
lbl_per_name = tk.Label(master=form, text='نام :')
txb_per_name = tk.Entry(master=form)
lbl_per_phone = tk.Label(master=form, text='تلفن :')
txb_per_phone = tk.Entry(master=form)

lbl_car_name = tk.Label(master=form, text='خودرو :')
txb_car_name = tk.Entry(master=form)
lbl_car_person__id = tk.Label(master=form, text='شناسه کاربری :')
txb_car_person__id = tk.Entry(master=form)



form.mainloop()