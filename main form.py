
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
# نمونه سازی از ابجکت های مورد نیاز
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
    # حذف تمام ایتم های لیست باکس
    lst_search.delete(0, tk.END)
    # با ارسال نام تیبل به تابع مورد نظر تمام رکورد های آنرا گرفته و درون لیست قرار میدهد
    records = select_all(tbl_name='tbl_persons')
    for index, record in enumerate(records):
        """
        حلقه روی آیتم های لیست پیمایش میکند
        به ازای هر ایتم یک عدد به ازای هر بار اجرای حلقه ایندکس یک عدد افزایش میابد
        """
        # افزودن آیتم به لیست باکس(پارامتر اول شمارنده حلقه و دوم یک رشته حاوی رکورد های دریافت شده از پایگاه داده)
        lst_search.insert(index, f'ID = {record[0]}         {record[1]}')
# نمونه سازی از یک دکمه و متصل کردن آن به تابع بالا
btn_per_select_all = tk.Button(master=form, text='همه کاربر ها', command=select_all_persons)


def select_person():
    if not txb_per_id.get().isdigit():
        messagebox.showerror('مقدار اشتباه', 'مقدار شناسه باید عدد باشد')
    else:
        # جستجوی یک رکورد در پایگاه با استفاده از مقدار های ارسال شده
        record = select_record(tbl_name='tbl_persons', id=txb_per_id.get())
        # خالی کردن تکست باکس
        txb_per_name.delete(0, tk.END)
        # افزودن رکورد دریافت شده به تکست باکس
        txb_per_name.insert(tk.END, record[1])
# نمونه سازی از یک دکمه و متصل کردن آن به تابع بالا
btn_per_select = tk.Button(master=form, text='جستجو', command=select_person)


def insert_person():
    # افزودن یک رکورد به پایگاه داده
    # تابع به برای ما یک مقدار درست یا غلط و متن ارور را باز میگرداند
    query = insert_record(tbl_name='tbl_persons', p_name=txb_per_name.get())
    if query:
        # اگر مقدار بازگردانده شده درست بود تابع نمایش همه ی کاربر ها اجرا شود
        select_all_persons()
    elif query[0] is False:
        # اگر مقدار بازگردانده شده غلط بود ارور در مسیج باکس نمایش داده شود
        messagebox.showwarning('کاربر افزوده نشد', query[1])
# نمونه سازی از یک دکمه و متصل کردن آن به تابع بالا
btn_per_insert = tk.Button(master=form, text='افزودن کاربر', command=insert_person)


def update_person():
    if not txb_per_id.get().isdigit():
        messagebox.showerror('مقدار اشتباه', 'مقدار شناسه باید عدد باشد')
    else:
        # ویرایش یک رکورد در پایگاه داده
        # تابع به برای ما یک مقدار درست یا غلط و متن ارور را باز میگرداند
        query = update_record(tbl_name='tbl_persons', target_id=txb_per_id.get(), p_name=txb_per_name.get())
        if query:
            # اگر مقدار بازگردانده شده درست بود تابع نمایش همه ی کاربر ها اجرا شود
            select_all_persons()
        elif query[0] is False:
            # اگر مقدار بازگردانده شده غلط بود ارور در مسیج باکس نمایش داده شود
            messagebox.showerror('کاربر ویرایش نشد', query[1])
# نمونه سازی از یک دکمه و متصل کردن آن به تابع بالا
btn_per_update = tk.Button(master=form, text='ویرایش کاربر', command=update_person)


def delete_person():
    if not txb_per_id.get().isdigit():
        messagebox.showerror('مقدار اشتباه', 'مقدار شناسه باید عدد باشد')
    else:
        # حذف یک رکورد از پایگاه داده
        # تابع به برای ما یک مقدار درست یا غلط و متن ارور را باز میگرداند
        query = delete_record(tbl_name='tbl_persons', target_id=txb_per_id.get())
        if query:
            # اگر مقدار بازگردانده شده درست بود تابع نمایش همه ی کاربر ها اجرا شود
            select_all_persons()
        elif query[0] is False:
            # اگر مقدار بازگردانده شده غلط بود ارور در مسیج باکس نمایش داده شود
            messagebox.showerror('کاربر حذف نشد', query[1])
# نمونه سازی از یک دکمه و متصل کردن آن به تابع بالا
btn_per_delete = tk.Button(master=form, text='حذف کاربر', command=delete_person)

# <----- Vehicles Buttons Functions ----->
def select_all_vehicles():
    # حذف تمام ایتم های لیست باکس
    lst_search.delete(0, tk.END)
    # با ارسال نام تیبل به تابع مورد نظر تمام رکورد های آنرا گرفته و درون لیست قرار میدهد
    records = select_all(tbl_name='tbl_vehicles')
    for index, record in enumerate(records):
        """
        حلقه روی آیتم های لیست پیمایش میکند
        به ازای هر ایتم یک عدد به ازای هر بار اجرای حلقه ایندکس یک عدد افزایش میابد
        ایدی کاربر مالک خودرو را جداسازی کرده کاربر را یافته و درون متغیر جای داده
        """
        id = int(record[2])
        # if not isinstance(id, int) and id[0] is False:
        #     delete_record(tbl_name='tbl_vehicles', target_id=record[0])
        # جستجوی کاربر صاحب خودرو در پایگاه داده و قرار دادن در متغیر
        person = select_record(tbl_name='tbl_persons', id=id)
        # افزودن آیتم به لیست باکس(پارامتر اول شمارنده حلقه و دوم یک رشته حاوی رکورد های دریافت شده از پایگاه داده)
        lst_search.insert(index, f'ID = {record[0]}          {record[1]}          ({person[1]})')
# نمونه سازی از یک دکمه و متصل کردن آن به تابع بالا
btn_car_select_all = tk.Button(master=form, text='همه خودرو ها', command=select_all_vehicles)


def select_vehicle():
    if not txb_car_id.get().isdigit():
        messagebox.showerror('مقدار اشتباه', 'مقدار شناسه باید عدد باشد')
    else:
        # جستجوی یک رکورد در پایگاه با استفاده از مقدار های ارسال شده
        record = select_record(tbl_name='tbl_vehicles', id=txb_car_id.get())
        # خالی کردن تکست باکس
        txb_car_name.delete(0, tk.END)
        # افزودن رکورد دریافت شده به تکست باکس
        txb_car_name.insert(tk.END, record[1])
        # خالی کردن تکست باکس
        txb_car_person__id.delete(0, tk.END)
        # افزودن رکورد دریافت شده به تکست باکس
        txb_car_person__id.insert(tk.END, record[2])
# نمونه سازی از یک دکمه و متصل کردن آن به تابع بالا
btn_car_select = tk.Button(master=form, text='جستجو خودرو', command=select_vehicle)

def insert_vehicle():
    if txb_car_person__id.get().isdigit():
        # افزودن یک رکورد به پایگاه داده
        # تابع به برای ما یک مقدار درست یا غلط و متن ارور را باز میگرداند
        query = insert_record(tbl_name='tbl_vehicles', v_name=txb_car_name.get(), v_pid=txb_car_person__id.get())
        if query:
            # اگر مقدار بازگردانده شده درست بود تابع نمایش همه ی خودرو ها اجرا شود
            select_all_vehicles()
        elif query[0] is False:
            # اگر مقدار بازگردانده شده غلط بود ارور در مسیج باکس نمایش داده شود
            messagebox.showwarning('خودرو افزوده نشد', query[1])
    else:
        messagebox.showerror('مقدار اشتباه', 'مقدار شناسه ها باید عدد باشد')
# نمونه سازی از یک دکمه و متصل کردن آن به تابع بالا
btn_car_insert = tk.Button(master=form, text='افزودن خودرو', command=insert_vehicle)


def update_vehicle():
    if txb_car_id.get().isdigit() and txb_car_person__id.get().isdigit():
        # ویرایش یک رکورد در پایگاه داده
        # تابع به برای ما یک مقدار درست یا غلط و متن ارور را باز میگرداند
        query = update_record(tbl_name='tbl_vehicles', target_id=txb_car_id.get(), 
                            v_name=txb_car_name.get(), v_pid=txb_car_person__id.get())
        if query:
            # اگر مقدار بازگردانده شده درست بود تابع نمایش همه ی خودرو ها اجرا شود
            select_all_vehicles()
        elif query[0] is False:
            # اگر مقدار بازگردانده شده غلط بود ارور در مسیج باکس نمایش داده شود
            messagebox.showerror('خودرو ویرایش نشد', query[1])
    else:
        messagebox.showerror('مقدار اشتباه', 'مقدار شناسه ها باید عدد باشد')
# نمونه سازی از یک دکمه و متصل کردن آن به تابع بالا
btn_car_update = tk.Button(master=form, text='ویرایش خودرو', command=update_vehicle)


def delete_vehicle():
    if not txb_car_id.get().isdigit():
        messagebox.showerror('مقدار اشتباه', 'مقدار شناسه باید عدد باشد')
    else:
        # حذف یک رکورد از پایگاه داده
        # تابع به برای ما یک مقدار درست یا غلط و متن ارور را باز میگرداند
        query = delete_record(tbl_name='tbl_vehicles', target_id=txb_car_id.get())
        if query:
            # اگر مقدار بازگردانده شده درست بود تابع نمایش همه ی خودرو ها اجرا شود
            select_all_vehicles()
        elif query[0] is False:
            # اگر مقدار بازگردانده شده غلط بود ارور در مسیج باکس نمایش داده شود
            messagebox.showerror('خودرو حذف نشد', query[1])
# نمونه سازی از یک دکمه و متصل کردن آن به تابع بالا
btn_car_delete = tk.Button(master=form, text='حذف خودرو', command=delete_vehicle)

# <----- Set Objects on Form ----->
# قرار دادن آبجکت های نمونه سازی شده روی فرم
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
