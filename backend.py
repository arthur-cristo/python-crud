import sqlite3 as sql

class TransactionObject():
    database = 'clientes.db'
    conn = None
    cur = None
    connected = False
    
    
    def connect(self):
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.connected = True
    
    
    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False


    def execute(self, sql, parms = None):
        if TransactionObject.connected:
            if parms == None:
                TransactionObject.cur.execute(sql)
            else:
                TransactionObject.cur.execute(sql,parms)
            return True
        else:
            return False
      
        
    def fetchall(self):
        return TransactionObject.cur.fetchall()
    
    
    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False
      
        
def initDB():
    trans = TransactionObject()
    trans.connect()
    trans.execute("CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY , name TEXT , last_name TEXT , email TEXT , cpf TEXT)")
    trans.persist
    trans.disconnect
    
    
def insert(name, last_name, email, cpf):
    trans = TransactionObject()
    trans.connect()
    trans.execute("INSERT INTO clients VALUES(NULL, ?,?,?,?)", (name, last_name, email, cpf))
    trans.persist()
    trans.disconnect()


def view():
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM clients")
    rows = trans.fetchall()
    trans.disconnect()
    return rows


def search(name="", last_name="", email="", cpf=""):
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM clients WHERE name=? or last_name =? or email=? or cpf=?", (name,last_name,email,cpf))
    rows = trans.fetchall()
    trans.disconnect()
    return rows


def delete(id):
    trans = TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM clients WHERE id = ?", (id,))
    trans.persist()
    trans.disconnect()


def update(id, name, last_name, email, cpf):
    trans = TransactionObject()
    trans.connect()
    trans.execute("UPDATE clients SET name=?, last_name=?, email=?, cpf=? WHERE id=?", (name,last_name,email,cpf,id))
    trans.persist()
    trans.disconnect()

initDB()
