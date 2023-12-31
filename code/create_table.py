import sqlite3
import os
conn=sqlite3.connect("uni.db")

cur=conn.cursor()

# to create table using the sql file
with open('largeRelationsInsertFile.sql') as f:
    cur.executescript(f.read())
