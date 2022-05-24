
"""
website   : www.bahmman.com
instagram : ibahmman
telegram  : ibahmman
github    : ibahmman
"""

import tkinter as tk
from tkinter import messagebox
from sqlite import select_all, select_record, insert_record, update_record, delete_record


# <----- Form Settins ----->
form = tk.Tk()
form.title('Personal Parking')
form.geometry('305x600')
form.resizable(width=False, height=False)

# <----- Form Objects ----->
lbl_per_details = tk.Label(master=form, text='------- کاربر -------')
lbl_per_id = tk.Label(master=form, text='شناسه')
txb_per_id = tk.Entry(master=form)
lbl_per_name = tk.Label(master=form, text='نام')
txb_per_name = tk.Entry(master=form)
lbl_car_details = tk.Label(master=form, text='------- خودرو -------')
lbl_car_id = tk.Label(master=form, text='شناسه خودرو')
txb_car_id = tk.Entry(master=form)
lbl_car_name = tk.Label(master=form, text='خودرو')
txb_car_name = tk.Entry(master=form)
lbl_car_person__id = tk.Label(master=form, text='شناسه کاربر')
txb_car_person__id = tk.Entry(master=form)
lbl_lst_details = tk.Label(master=form, text='------- فهرست -------')
lst_search = tk.Listbox(master=form, width=50, height=20)

# <----- Persons Buttons Functions ----->
"""
db.db :
    tbl_persons : 
        p_id
        p_name
    tbl_vehicles :
        v_id
        v_name
        v_pid
"""
def select_all_persons():
    lst_search.delete(0, tk.END)
    records = select_all(tbl_name='tbl_persons')
    for index, record in enumerate(records):
        lst_search.insert(index, f'ID = {record[0]}         {record[1]}')
btn_per_select_all = tk.Button(master=form, text='همه کاربر ها', command=select_all_persons)


def select_person():
    record = select_record(tbl_name='tbl_persons', id=txb_per_id.get())
    txb_per_name.delete(0, tk.END)
    txb_per_name.insert(tk.END, record[1])
btn_per_select = tk.Button(master=form, text='جستجو', command=select_person)


def insert_person():
    query = insert_record(tbl_name='tbl_persons', p_name=txb_per_name.get())
    if query:
        select_all_persons()
    elif query[0] is False:
        messagebox.showwarning('کاربر افزوده نشد', query[1])
btn_per_insert = tk.Button(master=form, text='افزودن کاربر', command=insert_person)


def update_person():
    query = update_record(tbl_name='tbl_persons', target_id=txb_per_id.get(), p_name=txb_per_name.get())
    if query:
        select_all_persons()
    elif query[0] is False:
        messagebox.showerror('کاربر ویرایش نشد', query[1])
btn_per_update = tk.Button(master=form, text='ویرایش کاربر', command=update_person)


def delete_person():
    query = delete_record(tbl_name='tbl_persons', target_id=txb_per_id.get())
    if query:
        select_all_persons()
    elif query[0] is False:
        messagebox.showerror('کاربر حذف نشد', query[1])
btn_per_delete = tk.Button(master=form, text='حذف کاربر', command=delete_person)

# <----- Vehicles Buttons Functions ----->
def select_all_vehicles():
    lst_search.delete(0, tk.END)
    records = select_all(tbl_name='tbl_vehicles')
    for index, record in enumerate(records):
        id = int(record[2])
        person = select_record(tbl_name='tbl_persons', id=id)
        lst_search.insert(index, f'ID = {record[0]}          {record[1]}          ({person[1]})')
btn_car_select_all = tk.Button(master=form, text='همه خودرو ها', command=select_all_vehicles)


def select_vehicle():
    record = select_record(tbl_name='tbl_vehicles', id=txb_car_id.get())
    txb_car_name.delete(0, tk.END)
    txb_car_name.insert(tk.END, record[1])
    txb_car_person__id.delete(0, tk.END)
    txb_car_person__id.insert(tk.END, record[2])
btn_car_select = tk.Button(master=form, text='جستجو خودرو', command=select_vehicle)

def insert_vehicle():
    query = insert_record(tbl_name='tbl_vehicles', v_name=txb_car_name.get(), v_pid=txb_car_person__id.get())
    if query:
        select_all_vehicles()
    elif query[0] is False:
        messagebox.showwarning('خودرو افزوده نشد', query[1])
btn_car_insert = tk.Button(master=form, text='افزودن خودرو', command=insert_vehicle)


def update_vehicle():
    query = update_record(tbl_name='tbl_vehicles', target_id=txb_car_id.get(), 
                        v_name=txb_car_name.get(), v_pid=txb_car_person__id.get())
    if query:
        select_all_vehicles()
    elif query[0] is False:
        messagebox.showerror('خودرو ویرایش نشد', query[1])
btn_car_update = tk.Button(master=form, text='ویرایش خودرو', command=update_vehicle)


def delete_vehicle():
    query = delete_record(tbl_name='tbl_vehicles', target_id=txb_car_id.get())
    if query:
        select_all_vehicles()
    elif query[0] is False:
        messagebox.showerror('خودرو حذف نشد', query[1])
btn_car_delete = tk.Button(master=form, text='حذف خودرو', command=delete_vehicle)

# <----- Set Objects on Form ----->
lbl_per_details.grid(row=1, columnspan=5)
lbl_per_id.grid(row=2, column=1)
txb_per_id.grid(row=2, column=2)
btn_per_select.grid(row=2, column=3)
lbl_per_name.grid(row=3, column=1)
txb_per_name.grid(row=3, column=2)
btn_per_insert.grid(row=4, column=1)
btn_per_update.grid(row=4, column=2)
btn_per_delete.grid(row=4, column=3)

lbl_car_details.grid(row=5, columnspan=5)
lbl_car_id.grid(row=6, column=1)
txb_car_id.grid(row=6, column=2)
btn_car_select.grid(row=6, column=3)
lbl_car_name.grid(row=7, column=1)
txb_car_name.grid(row=7, column=2)
lbl_car_person__id.grid(row=8, column=1)
txb_car_person__id.grid(row=8, column=2)
btn_car_insert.grid(row=9, column=1)
btn_car_update.grid(row=9, column=2)
btn_car_delete.grid(row=9, column=3)
 
lbl_lst_details.grid(row=11, columnspan=5)
btn_per_select_all.grid(row=13, column=1)
btn_car_select_all.grid(row=13, column=3)
lst_search.grid(row=14, columnspan=5)

form.mainloop()