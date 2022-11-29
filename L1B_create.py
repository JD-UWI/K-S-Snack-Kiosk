import sqlite3, os
from sqlite3 import Error

DB = "inventory.db"  #stores database into DB variable
SQLFILE = "L1A_inventory.sql"  #stores SQLfile into SQLFILE variable

#Delete pre-existing databases
if os.path.exists(DB):
  os.remove(DB)

#Import SQL
conn = sqlite3.connect(DB)
with open(SQLFILE) as f:
  conn.executescript(f.read())
conn.commit()
conn.close()
print("Database created successfully!")
