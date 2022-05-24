import os, sqlite3

dir_path = os.getcwd()

# <----- SQLite3 Setting ----->
def connection(file_dir, file_name):
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
def select_all(conn = connection(dir_path, 'db.db'), tbl_name = None):
    records = list()
    try:
        assert tbl_name is None, 'Table name is not set.!'
        curs = conn.cursor()
        curs.execute(f"SELECT * FROM {tbl_name}")
        rows = curs.fetchall()
        curs.close()
    except AssertionError as e:
        return e
    else:
        for row in rows:
            records.append(row)
        return records
    finally:
        conn.close()
# print(select_all(tbl_name='tbl_persons'))


def select_record(conn = connection(dir_path, 'db.db'), tbl_name = None, id = None):
    try:
        assert tbl_name is None, 'Table name is not set.!'
        assert id is None, 'ID is not set.!'
        curs = conn.cursor()
        curs.execute(f'SELECT * FROM {tbl_name} WHERE id = {id}')
        rows = curs.fetchall()
        curs.close()
    except AssertionError as e:
        return e
    else:
        return rows[0]
    finally:
        conn.close()
# print(select_record(connection(dir_path, 'db.db'), 'tbl_persons', 2))


def insert_record(conn = connection(dir_path, 'db.db'), tbl_name = None, **kwargs):
    columns = ', '.join([(k) for k in kwargs.keys()])
    values = ', '.join([f"'{v}'" if isinstance(v, str) else (str(v)) for v in kwargs.values()])
    
    try:
        assert tbl_name is None, 'Table name is not set.!'
        curs = conn.cursor()
        curs.execute(f'INSERT INTO {tbl_name} ({columns}) VALUES({values})')
        conn.commit()
        curs.close()
    except AssertionError as e:
        return False, e
    else:
        return True
    finally:
        conn.close()
# print(insert_record(connection(dir_path, 'db.db'), 'tbl_vehicles', v_name='Benz', v_pid=1))


def update_record(conn = connection(dir_path, 'db.db'), tbl_name = None, target_id = None, **kwargs):
    items = list()
    for k, v in kwargs.items():
        item = k + ' = '
        if isinstance(v, str):
            item += f"'{v}'"
        else:
            item += str(v)
        items.append(item)

    items = ', '.join(items)
    try:
        assert tbl_name is None, 'Table name is not set.!'
        assert target_id is None, 'Target ID is not set.!'
        curs = conn.cursor()
        curs.execute(f'UPDATE {tbl_name} SET {items} WHERE id = {target_id}')
        conn.commit()
        curs.close()
    except AssertionError as e:
        return False, e
    else:
        return True
    finally:
        conn.close()
# print(update_record(connection(dir_path, 'db.db'), 'tbl_vehicles', 1, v_name='Ferrari', v_pid=2))

def delete_record(conn = connection(dir_path, 'db.db'), tbl_name = None, target_id = None):
    try:
        assert tbl_name is None, 'Table name is not set.!'
        assert target_id is None, 'Target ID is not set.!'
        curs = conn.cursor()
        curs.execute(f'DELETE FROM {tbl_name} WHERE id = {target_id}')
        conn.commit()
        curs.close()
    except AssertionError as e:
        return False, e
    else:
        return True
    finally:
        conn.close()
# print(delete_record())