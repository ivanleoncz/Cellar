
import sqlite3 as lite
import sys

class Lite:
 
    db = None
    conn = None

    def __init__(self,db):
        self.db = db

    def data_builder(self):
        conn = lite.connect(self.db, isolation_level=None)
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS program_languages_ranking_ieee_2017")
        cur.execute("CREATE TABLE program_languages_ranking_ieee_2017 \
                    (Pos INT, Name TEXT, Web CHARACTER(3), Mobile CHARACTER(3), Desktop CHARACTER(3), MicroCircuits CHARACTER(3))")
        cur.execute("INSERT INTO program_languages_ranking_ieee_2017 VALUES(1,'Python','Yes','No','Yes','No')")
        cur.execute("INSERT INTO program_languages_ranking_ieee_2017 VALUES(2,'C','No','Yes','Yes','Yes')")
        cur.execute("INSERT INTO program_languages_ranking_ieee_2017 VALUES(3,'Java','Yes','Yes','Yes','No')")
        cur.execute("INSERT INTO program_languages_ranking_ieee_2017 VALUES(4,'C++','No','Yes','Yes','Yes')")
        cur.execute("INSERT INTO program_languages_ranking_ieee_2017 VALUES(5,'C sharp','Yes','Yes','Yes','NO')")
        cur.execute("INSERT INTO program_languages_ranking_ieee_2017 VALUES(6,'R lang','No','No','Yes','No')")
        cur.execute("INSERT INTO program_languages_ranking_ieee_2017 VALUES(7,'JavaScript','Yes','Yes','No','No')")
        cur.execute("INSERT INTO program_languages_ranking_ieee_2017 VALUES(8,'PHP','Yes','No','No','No')")
        cur.execute("INSERT INTO program_languages_ranking_ieee_2017 VALUES(9,'Go','Yes','No','Yes','No')")
        cur.execute("INSERT INTO program_languages_ranking_ieee_2017 VALUES(10,'Swift','No','Yes','Yes','No')")
        conn.close()
        return None

    def data_querier(self):
        conn = lite.connect(self.db, isolation_level=None)
        cur = conn.cursor()
        cur.execute("SELECT * FROM program_languages_ranking_ieee_2017")
        results = cur.fetchall()
        conn.close()
        return results

    def get_version(self):
        try:
            conn = lite.connect(self.db, isolation_level=None)
            cur = conn.cursor()
            cur.execute('SELECT SQLITE_VERSION()')
            data = cur.fetchone()
            return data
        except Exception as e:
            return "Error: %s " % e
        finally:
            if conn:
                conn.close()

