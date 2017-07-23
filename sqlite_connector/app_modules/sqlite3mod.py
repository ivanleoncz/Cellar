
import sqlite3 as lite
import sys

class Lite:

    def get_version():
        
        conn = None
        
        try:
            conn = lite.connect('test.db')
            cur = conn.cursor()
            cur.execute('SELECT SQLITE_VERSION()')
            data = cur.fetchone()
            return "SQLite version: %s " % data
        
        except Exception as e:
            return "Error: %s " % e.args[0]
        
        finally:
            if conn:
                conn.close()

