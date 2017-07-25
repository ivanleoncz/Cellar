
import sqlite3 as lite
import sys

class Lite:
 
    db = None
    conn = None

    def __init__(self,db):
        self.db = db
        conn = lite.connect(db)

    def get_version():
        try:
            conn = lite.connect('test.db')
            cur = conn.cursor()
            cur.execute('SELECT SQLITE_VERSION()')
            data = cur.fetchone()
            return "SQLite version: %s " % data
        except Exception as e:
            return "Error: %s " % e
        
        finally:
            if conn:
                conn.close()

