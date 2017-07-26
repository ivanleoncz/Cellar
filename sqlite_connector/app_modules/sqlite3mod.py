
import sqlite3 as lite
import sys

class Lite:
 
    db = None
    conn = None

    def __init__(self,db):
        self.db = db

    def data_builder(self):
        print("Building data...")
        conn = lite.connect(self.db, isolation_level=None)
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS program_languages_ranking_ieee_2017")
        cur.execute("CREATE TABLE program_languages_ranking_ieee_2017 \
                    (Pos INT, Name TEXT, Web BOOLEAN, Mobile BOOLEAN, Desktop BOOLEAN, MicroCircuits BOOLEAN)")
        cur.execute("INSERT INTO program_languages_ranking_ieee_2017 VALUES(1,'Python',1,0,1,0)")
        cur.execute("INSERT INTO program_languages_ranking_ieee_2017 VALUES(2,'C',0,1,1,1)")
        cur.execute("INSERT INTO program_languages_ranking_ieee_2017 VALUES(3,'Java',1,1,1,0)")
        cur.execute("INSERT INTO program_languages_ranking_ieee_2017 VALUES(4,'C++',0,1,1,1)")
        cur.execute("INSERT INTO program_languages_ranking_ieee_2017 VALUES(5,'C sharp',1,1,1,0)")
        cur.execute("INSERT INTO program_languages_ranking_ieee_2017 VALUES(6,'R lang',0,0,1,0)")
        cur.execute("INSERT INTO program_languages_ranking_ieee_2017 VALUES(7,'JavaScript',1,1,0,0)")
        cur.execute("INSERT INTO program_languages_ranking_ieee_2017 VALUES(8,'PHP',1,0,0,0)")
        cur.execute("INSERT INTO program_languages_ranking_ieee_2017 VALUES(9,'Go',1,0,1,0)")
        cur.execute("INSERT INTO program_languages_ranking_ieee_2017 VALUES(10,'Swift',0,1,1,0)")
        conn.close()
        return "Done."

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

