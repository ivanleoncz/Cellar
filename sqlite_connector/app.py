#!/usr/bin/env python

from app_modules import sqlite3mod


lite_obj = sqlite3mod.Lite

db_version = lite_obj.get_version()

print(db_version)
