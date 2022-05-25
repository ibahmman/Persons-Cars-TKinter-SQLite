
"""
website   : www.bahmman.com
instagram : ibahmman
telegram  : ibahmman
github    : ibahmman
"""

import os, sqlite3


# <----- SQLite3 Setting ----->
def connection(file_dir = os.getcwd(), file_name = 'db.db'):
    """
    کلاس برای ساخت ارتباط با پایگاه داده
    پارامتر اول مسیر پایگاه داده
    پارامتر دوم نام پایگاه داده
    مقدار پیشفرض پارامتر ها مسیر جاری پروژه است
    """
    try:
        conn = sqlite3.connect(f'{file_dir}\{file_name}')
    except:
        pass
    else:
        return conn


# <----- Database Functions ----->
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
def select_all(conn = connection(), tbl_name = None):
    """
    انتخاب تمام ردیف های یک تیبل
    پارامتر اول ارتباط با دیتابیس
    پارامتر دوم نام تیبل
    """
    records = list()
    try:
        # اگر نام تیبل به تابع ارسال شد برنامه بدون ایراد ادامه یابد در غیر این صورت وارد قسمت ارور شود
        assert tbl_name is not None, 'Table name is not set.!'
        curs = conn.cursor()
        # ارسال کوعری انتخاب همه ی موارد در تیبل به پایگاه داده
        curs.execute(f"SELECT * FROM {tbl_name}")
        # دریافت تمام رکورد ها
        rows = curs.fetchall()
        curs.close()
    except AssertionError as e:
        # اگر نام تیبل به تابع ارسال نشد وارد این بخش میشود و ارور مورد نظر را باز میگرداند
        return e
    else:
        # زمانی که ارتباط با پایگاه داده به مشکل نخورد یکی یکی رکورد ها وارد لیست میشوند
        for row in rows:
            records.append(row)
        # بازگرداندن لیست به محل فراخانی تابع
        return records
# print(select_all(tbl_name='tbl_persons'))


def select_record(conn = connection(), tbl_name = None, id = None):
    """
    انتخاب یک مورد از پایگاه داده بر اساس ایدی داده شده
    پارامتر اول برقراری ارتباط با پایگاه داده
    پارامتر دوم نام تیبل مورد نظر
    پارامتر سوم ایدی
    """
    try:
        # اگر نام تیبل به تابع ارسال شد برنامه بدون ایراد ادامه یابد در غیر این صورت وارد قسمت ارور شود
        assert tbl_name is not None, 'Table name is not set.!'
        # اگر ایدی به تابع ارسال شد برنامه بدون ایراد ادامه یابد در غیر این صورت وارد قسمت ارور شود 
        assert id is not None, 'ID is not set.!'
        curs = conn.cursor()
        # ارسال کوعری جستجو یک مورد در تیبل مورد نظر بر اساس ایدی
        curs.execute(f'SELECT * FROM {tbl_name} WHERE id = {id}')
        # دریافت تمام رکورد ها
        rows = curs.fetchall()
        print(rows)
        assert rows, 'مورد یافت نشد'
        curs.close()
    except AssertionError as e:
        # اگر نام تیبل به تابع ارسال نشد وارد این بخش میشود و ارور مورد نظر را باز میگرداند
        return False, e
    else:
        # بازگرداندن مقدار یافت شده به محل فراخانی تابع
        return rows[0]
# print(select_record(tbl_name='tbl_persons', id=2))


def insert_record(conn = connection(), tbl_name = None, **kwargs):
    """
    افزودن یک رکورد تازه در پایگاه داده
    پارامتر اول برقرای ارتباط با دیتابیس
    پارامتر دوم نام تیبل مورد نظر
    در ادامه نام فیلد را نوشته و مقدار انرا ارسال کرده
    v_name = Mustang, v_pid = 1 
    """
    # با یک حلقه تک خطی تمام کلید ها را از دیکشنری دریافت شده گرفته و با متد جوین آنهارا به رشته تبدیل کرده با فاصله ی کاما
    columns = ', '.join([(k) for k in kwargs.keys()])
    # با حلقه و شرط تک خطی روی مقدار های دذیکشنری داده شده پیمایش میکند
    # اگر مقدار داده شده رشته بود انرا درود کوتیشن  قرار میدهد در غیر این صورت همان مقدار را وارد لیست میکند
    # با استفاده از متد جوین همه ی لیست را وارد یک استرینگ میکند و بین انها کاما قرار میدهد
    values = ', '.join([f"'{v}'" if isinstance(v, str) else (str(v)) for v in kwargs.values()])
    
    try:
        # اگر نام تیبل به تابع ارسال شد برنامه بدون ایراد ادامه یابد در غیر این صورت وارد قسمت ارور شود
        assert tbl_name is not None, 'Table name is not set.!'
        curs = conn.cursor()
        # ارسال کوعری افزودن فیلد های داده شده به تیبل معرفی شده
        curs.execute(f'INSERT INTO {tbl_name} ({columns}) VALUES({values})')
        conn.commit()
        curs.close()
    except AssertionError as e:
        # اگر نام تیبل به تابع داده نشده بود یک تاپل با مقدار غلط و مقدار دوم متن ارور باز گرداند
        return False, e
    else:
        # اگر رکورد به درستی افزوده شد مقدار درست را باز گرداند
        return True
# print(insert_record(connection(dir_path, 'db.db'), 'tbl_vehicles', v_name='Benz', v_pid=1))


def update_record(conn = connection(), tbl_name = None, target_id = None, **kwargs):
    """
    ویرایش یک رکورد در پایگاه داده
    پارامتر اول برقرای ارتباط با دیتابیس
    پارامتر دوم نام تیبل مورد نظر
    پارامتر سوم ایدی رکورد مورد نظر
    در ادامه نام فیلد را نوشته و مقدار انرا ارسال کرده
    p_name = Bahman
    """
    items = list()
    # حلقه در ایتم های دیکشنری پیمایش میکند کلید ها و مقدار ها را جدا میکند
    for k, v in kwargs.items():
        """
        حلقه در ایتم های دیکشنری پیمایش میکند کلید ها و مقدار ها را جدا میکند
        هر دفعه کلید و اوپراتور مساوی را درون رشته آیتم قرار میدهد
        اگر نوع مقدار داده شده رشته بود آنرا درود کوتیشن گزاشته و به متغیر آیتم اضافه کند
        در غیر این صورت مقدار را بدون دست کاری به متغیر آیتم اضافه کند
        """
        item = k + ' = '
        if isinstance(v, str):
            item += f"'{v}'"
        else:
            item += str(v)
        # آیتم ساخته شده را به لیست مورد نظر اضافه میکند
        items.append(item)
    # آیتم های لیست را با استفاده از کامکا جدا سازی میکند همه ی متن را به رشته تبدیل میکند و وارد متغیر آیتم میکند
    items = ', '.join(items)
    try:
        # اگر نام تیبل به تابع ارسال شد برنامه بدون ایراد ادامه یابد در غیر این صورت وارد قسمت ارور شود
        assert tbl_name is not None, 'Table name is not set.!'
        # اگر ایدی به تابع ارسال شد برنامه بدون ایراد ادامه یابد در غیر این صورت وارد قسمت ارور شود 
        assert target_id is not None, 'Target ID is not set.!'
        curs = conn.cursor()
        # ارسال کوعری ویرایش یک رکورد در تیبل با استفاده از ایدی مورد نظر
        curs.execute(f'UPDATE {tbl_name} SET {items} WHERE id = {target_id}')
        conn.commit()
        curs.close()
    except AssertionError as e:
        # اگر نام تیبل به تابع داده نشده بود یک تاپل با مقدار غلط و مقدار دوم متن ارور باز گرداند
        return False, e
    else:
        # اگر رکورد به درستی افزوده شد مقدار درست را باز گرداند
        return True
# print(update_record(connection(dir_path, 'db.db'), 'tbl_vehicles', 1, v_name='Ferrari', v_pid=2))


def delete_record(conn = connection(), tbl_name = None, target_id = None):
    """
    حذف یک رکورد در تیبل با استفاده از ایدی
    پارامتر اول برقرای ارتباط با دیتابیس
    پارامتر دوم نام تیبل مورد نظر
    پارامتر سوم ایدی رکورد مورد نظر
    """
    try:
        # اگر نام تیبل به تابع ارسال شد برنامه بدون ایراد ادامه یابد در غیر این صورت وارد قسمت ارور شود
        assert tbl_name is not None, 'Table name is not set.!'
        # اگر ایدی به تابع ارسال شد برنامه بدون ایراد ادامه یابد در غیر این صورت وارد قسمت ارور شود 
        assert target_id is not None, 'Target ID is not set.!'
        curs = conn.cursor()
        # حذف یک رکورد در تیبل زمانی که مقدار ایدی یافت شد
        curs.execute(f'DELETE FROM {tbl_name} WHERE id = {target_id}')
        conn.commit()
        curs.close()
    except AssertionError as e:
        # اگر نام تیبل به تابع داده نشده بود یک تاپل با مقدار غلط و مقدار دوم متن ارور باز گرداند
        return False, e
    else:
        # اگر ایدی به تابع ارسال شد برنامه بدون ایراد ادامه یابد در غیر این صورت وارد قسمت ارور شود 
        return True
# print(delete_record())
