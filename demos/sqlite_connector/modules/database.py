#!/usr/bin/python3
""" Provides class for building and reading SQLite3 database. """

__author__ = "@ivanleoncz"

import sqlite3
import sys

class Lite:
    """ Protype for building SQLite3 database and reading its data. """

    dbfile = None
    db     = sqlite3.connect(dbfile, isolation_level=None)
    cur    = db.cursor()
    table  = "programming_languages_ranking_2017"


    def __init__(self,dbfile):
        """ Initializes class variable with database filename. """
        self.dbfile = dbfile


    def reader(self):
        """ Reads database table. """
        query = """ SELECT * FROM {0} """.format(self.table)
        self.cur.execute(query)
        data = cur.fetchall()
        self.db.commit()
        return data


    def builder(self):
        """ Builds database table. """

        pos  = "Pos"
        name = "Name"
        col1 = "Web"
        col2 = "Mobile"
        col3 = "Desktop"
        col4 = "Micro Circuits"

        dropif   = """ DROP TABLE IF EXISTS {0}""".format(self.table)
        create   = """ CREATE TABLE {0}
                     ({1} INT, {2} TEXT, {3} CHARACTER(3), {4} CHARACTER(3),
                       {5} CHARACTER(3), {6} CHARACTER(3))
                   """.format(self.table, pos, name, col1, col2, col3, col4)
        insert1  = """ INSERT INTO {0}
                       VALUES(1,'Python','Yes','No','Yes','No')
                   """.format(self.table)
        insert2  = """ INSERT INTO {0}
                       VALUES(2,'C','No','Yes','Yes','Yes')
                   """.format(self.table)
        insert3  = """ INSERT INTO {0}
                       VALUES(3,'Java','Yes','Yes','Yes','No')
                   """.format(self.table)
        insert4  = """ INSERT INTO {0}
                       VALUES(4,'C++','No','Yes','Yes','Yes')
                   """.format(self.table)
        insert5  = """ INSERT INTO {0}
                       VALUES(5,'C sharp','Yes','Yes','Yes','No')
                   """.format(self.table)
        insert6  = """ INSERT INTO {0}
                       VALUES(6,'R lang','No','No','Yes','No')
                   """.format(self.table)
        insert7  = """ INSERT INTO {0}
                       VALUES(7,'JavaScript','Yes','Yes','No','No')
                   """.format(self.table)
        insert8  = """ INSERT INTO {0}
                       VALUES(8,'PHP','Yes','No','No','No')
                   """.format(self.table)
        insert9  = """ INSERT INTO {0}
                       VALUES(9,'Go','Yes','No','Yes','No')
                   """.format(self.table)
        insert10 = """ INSERT INTO {0}
                       VALUES(10,'Swift','No','Yes','Yes','No')
                   """.format(self.table)
        self.cur.execute(dropif)
        self.cur.execute(create)
        self.cur.execute(insert1)
        self.cur.execute(insert2)
        self.cur.execute(insert3)
        self.cur.execute(insert4)
        self.cur.execute(insert4)
        self.cur.execute(insert5)
        self.cur.execute(insert6)
        self.cur.execute(insert7)
        self.cur.execute(insert8)
        self.cur.execute(insert9)
        self.cur.execute(insert10)
        self.db.commit()
