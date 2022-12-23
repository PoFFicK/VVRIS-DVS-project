import sqlite3
from sqlite3 import Error
 
def create_connection(path):
    conn=None
    try:
        conn = sqlite3.connect(path)
        print('Connection successful')
    except Error as e:
        print(f"the error '{e}' occurred")
 
    return conn
 
 
def show_all(path,tableName):
    conn=create_connection(path)
 
    c=conn.cursor()
 
    c.execute("SELECT rowid, * from {}".format(tableName))
 
    items=c.fetchall()
    for i in items:
        print(i)
    conn.commit()
 
    conn.close()
 
 
def add_one_statsdb(path,tableName,IP,victories,losses,rating):
    conn=create_connection(path)
 
    c=conn.cursor()
 
    c.execute("INSERT INTO {} VALUES (?,?,?,?)".format(tableName), (IP,victories,losses,rating))
 
    conn.commit()
 
    conn.close()
 
 
 
def delete_one(path,tableName,id):
    # when putting in a value, it MUST be a STRING, not an INTEGER. e.g. '6' instead of 6
    # значение id ДОЛЖНО быть СТРОКОЙ, а не ЧИСЛОМ, например '6' вместо 6
    conn=create_connection(path)
 
    c=conn.cursor()
 
    c.execute("delete from {} where rowid = (?) ".format(tableName), id)
 
    conn.commit()
 
    conn.close()
 
def add_many(path,tableName,list):
    conn=create_connection(path)
 
    c=conn.cursor()
 
    c.executemany("INSERT INTO {} VALUES (?,?)".format(tableName), (list))
 
    conn.commit()
 
    conn.close()
 
 
# def search_by_IP(path,tableName,IP):
#     conn=create_connection(path)
 
#     c=conn.cursor()
 
#     c.execute("select rowid from {} where IP = (?)".format(tableName), (IP,))
 
#     item=c.fetchone()
 
#     return item
 
#     conn.commit()
 
#     conn.close()
 
def update_victories(path, rowid):
    conn=create_connection(path)
 
    c=conn.cursor()
 
    c.execute("""UPDATE statistics SET victories = victories + 1 
    WHERE rowid = {}""".format(rowid))
    conn.commit()
 
    conn.close()
 
def update_losses(path, rowid):
    conn=create_connection(path)
 
    c=conn.cursor()
 
    c.execute("""UPDATE statistics SET losses = losses + 1 
    WHERE rowid = {}""".format(rowid))
    conn.commit()
 
    conn.close()
 
def update_rating(path, data, rowid):
    conn=create_connection(path)
 
    c=conn.cursor()
 
    c.execute("""UPDATE statistics SET rating = {} 
    WHERE rowid = {}""".format(data, rowid))
    conn.commit()
 
    conn.close()
 
def take_rowid(path,tableName,datatype, data):
    conn=create_connection(path)
 
    c=conn.cursor()
 
    c.execute("select rowid from {} where {} = (?)".format(tableName,datatype), (data,))
    # https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta
    # это чтоб понимать, зачем писать , после data
    items=c.fetchall()
    for i in items:
        return i[0]
 
    conn.commit()
 
    conn.close()
 
def take_rating(path,tableName,datatype, data):
    conn=create_connection(path)
 
    c=conn.cursor()
 
    c.execute("select rating from {} where {} = (?)".format(tableName,datatype), (data,))
 
    items=c.fetchall()
    for i in items:
        return i[0]
 
    conn.commit()
 
    conn.close()
 
def take_WL(path,id):
    conn=create_connection(path)
 
    c=conn.cursor()
 
    c.execute("SELECT victories, losses FROM statistics WHERE rowid = (?)",(id,))
    items=c.fetchall()
    for i in items:
        return i
 
    conn.commit()
 
    conn.close()
