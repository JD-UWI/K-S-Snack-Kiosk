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
  
#Sort Item
def sort(l, n, s):
  ol = []
  r = 0
  def h(a, b, l, r, e):
    if 0 == len(b):   
      return l
    elif l == []:
      l = l + [b[0]]
      return h(0, b[1:], l, 0, e)
    elif b[0][e][r]>l[-1][e][r] and b[0][e][0]>=l[-1][e][0]:
      l = l + [b[0]]
      return h(0, b[1:], l, 0, e)
    elif b[0][e][r] < l[a][e][r]:
      l = l[:a] + [b[0]] + l[a:]
      return h(0, b[1:], l, 0, e)
    elif b[0][e][r] > l[a][e][r]:
      return h(a+1, b, l, 0, e)
    else:
      try:
       if b[0][e][r] == l[a][e][r]:
         return(h(0, b, l, r+1, e))
      except IndexError:
       if len(b[0][e]) > len(l[a][e]):
         l = l[:a+1] + [b[0]] + l[a+1:]
         return h(0, b[1:], l, 0, e)
       else:
         l = l[:a] + [b[0]] + l[a:]
         return h(0, b[1:], l, 0, e)
       return h(0, b, l, 0, e)
    return h(a, b, l, r, e)
  return(h(l, n, ol, r, s))

#Show Sort
@app.route("/sort", methods=['GET', 'POST'])
def sortS():
  g = getAll()
  w = []
  if request.method == 'POST':
    s = request.form.get("order")
    if s == None or s == '':
      w = sort(0, g, 0)
    else:
      w = sort(0, g, int(s))
  return render_template("L4SortItem.html", lst = w)

    
# (D) START
if __name__ == "__main__":
  app.run(HOST_NAME, HOST_PORT)
