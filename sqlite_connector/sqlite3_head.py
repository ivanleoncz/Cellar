#!/usr/bin/python3
""" Verifies the existence of a SQLite3 database file. """

import os
import sys

db_filename = input("Database filename (end with .sqlite3), please:")

if os.path.isfile(db_filename):
    if os.path.getsize(db_filename) > 100:
        with open(db_filename,'r', encoding = "ISO-8859-1") as f:
            header = f.read(100)
            if header.startswith('SQLite format 3'):
                print("SQLite3 database has been detected.")
