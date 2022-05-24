import tkinter as tk
from sqlite import connection, select_all

select_all('tbl_vehicles')

# # <----- Form Settins ----->
# form = tk.Tk()
# form.title(dir_path)
# form.geometry('800x500')
# form.resizable(width=False, height=False)

# # <----- Panel Window ----->
# panel_right = tk.PanedWindow()
# panel_right.pack(side= tk.RIGHT)

# # <----- Form Objects ----->
# lbl_per_name = tk.Label(master=form, text='نام')
# txb_per_name = tk.Entry(master=form)
# # lbl_per_phone = tk.Label(master=form, text='تلفن')
# # txb_per_phone = tk.Entry(master=form)
# btn_per_insert = tk.Button(master=form, text='', 
#                     command=insert_record('tbl_persons', {'p_name': txb_per_name.get()}))
# btn_per_update = tk.Button(master=form, text='', command=update_record)
# btn_per_delete = tk.Button(master=form, text='', command=delete_record)

# lbl_car_name = tk.Label(master=form, text='خودرو')
# txb_car_name = tk.Entry(master=form)
# lbl_car_person__id = tk.Label(master=form, text='شناسه کاربری')
# txb_car_person__id = tk.Entry(master=form)


# panel_right.add(txb_per_name)
# panel_right.add(lbl_per_name)


# form.mainloop()