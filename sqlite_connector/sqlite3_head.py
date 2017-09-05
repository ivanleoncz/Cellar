#!/usr/bin/python3

import os
import sys

if os.path.isfile('test.sqlite3'):
    if os.path.getsize('test.sqlite3') > 100:
        with open('test.sqlite3','r', encoding = "ISO-8859-1") as f:
            header = f.read(100)
            if header.startswith('SQLite format 3'):
                print("SQLite3 database has been detected.")
