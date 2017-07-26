#!/usr/bin/env python

from app_modules import sqlite3mod


lite_obj = sqlite3mod.Lite("test.db")

db_builder = lite_obj.data_builder()

print(db_builder)
