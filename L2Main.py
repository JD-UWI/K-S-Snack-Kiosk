# (A) INIT
# (A1) LOAD MODULES
from flask import Flask, render_template, request, make_response, escape
import sqlite3, json


# (A2) FLASK SETTINGS + INIT
HOST_NAME = "localhost"
HOST_PORT = 80
DB = "inventory.db"
app = Flask(__name__)
# app.debug = True

def select (sql, data=[]):
  conn = sqlite3.connect(DB)
  cursor = conn.cursor()
  cursor.execute(sql, data)
  results = cursor.fetchall()
  conn.close()
  return results

# (D) GET ALL ITEMS
def getAll ():
  return select("SELECT * FROM `items`")

# (B) HELPER - RUN SQL QUERY
def query (sql, data):
  conn = sqlite3.connect(DB)
  cursor = conn.cursor()
  cursor.execute(sql, data)
  conn.commit()
  conn.close()

# (G) SAVE ITEM Function
def save (Itemname,ID,qty,cost,suplier,supemail):
  # (G1) ADD NEW
  query(
      """INSERT INTO "items" 
      (`item_name`, `item_ID`, `item_qty`, `item_cost`, 'suplname', 'suplemail') 
      VALUES (?, ?, ?, ?, ?, ?)""",
      [Itemname,ID,qty,cost,suplier,supemail])

# Modify Item Function
def edit (Itemname,ID,qty,cost,suplier,supemail):
  query(
    """UPDATE "items"
    SET (`item_name`, `item_ID`, `item_qty`, `item_cost`, 'suplname', 'suplemail')
    VALUES (?, ?, ?, ?, ?, ?)""",
    [Itemname,ID,qty,cost,suplier,supemail])    

#Main Page
@app.route("/")
def main():
  items = getAll()
  return render_template("L4Main.html", items=items)

#Add New Item
@app.route("/newitem", methods=['GET', 'POST'])
def add():
  if request.method == 'POST':
    nm = request.form.get("item_name")
    iID = request.form.get("item_ID")
    qty = request.form.get("itemQty") 
    cost = request.form.get("item_cost")
    isn = request.form.get("suplname") 
    ise = request.form.get("suplemail")
    save(nm,iID,qty,cost,isn,ise)
  return render_template("L4Add.html")

@app.route("/adddelete")
def AD():
  items = getAll()
  return render_template("L4AddDelete.html", items=items)

#Modify  Item
@app.route("/modify", methods=['GET', 'POST'])
def modify():
  if request.method == 'POST':
    nm = request.form.get("item_name")
    iID = request.form.get("item_ID")
    qty = request.form.get("itemQty") 
    cost = request.form.get("item_cost")
    isn = request.form.get("suplname") 
    ise = request.form.get("suplemail")
    edit(nm,iID,qty,cost,isn,ise)
  return render_template("L4ModifyItem.html")

#Show Item
def showIT(a, c):
  b = getAll()
  r = 0
  d = 0
  i = []
  while d == 0:
    if a == b[r][c]:
      i = b[r]
      d +=1
    else:
      r += 1
    if r > len(b)-1:
      return ["Item doesn't exist in Database. Please ensure that Name/ID was entered correctly",-1]
      d -= 1
  return i

#Search Item
@app.route("/search", methods=['GET', 'POST'])
def search():
  w = []
  if request.method == 'POST':
   
   n = request.form.get("itemN")
   d = request.form.get("item#")
   if n == '' or n == None:
       w = showIT(d, 1)
   else: 
       w = showIT(n, 0)
  return render_template("L4SearchItem.html", info = w)
  




    
# (D) START
if __name__ == "__main__":
  app.run(HOST_NAME, HOST_PORT)
