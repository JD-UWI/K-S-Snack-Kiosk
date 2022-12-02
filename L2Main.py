
#LOAD MODULES
from flask import Flask, render_template, request, make_response, escape
import sqlite3, json
import smtplib

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()


#FLASK SETTINGS + INIT
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

#GET ALL ITEMS
def getAll ():
  return select("SELECT * FROM `items`")

#HELPER - RUN SQL QUERY
def query (sql, data):
  conn = sqlite3.connect(DB)
  cursor = conn.cursor()
  cursor.execute(sql, data)
  conn.commit()
  conn.close()

# SAVE ITEM Function
def save (Itemid, Itemname,qty,cost,suplier,supemail):
  # (G1) ADD NEW
  query(
      """INSERT INTO "items" 
      ('item_ID', `item_name`, `item_qty`, `item_cost`, 'suplname', 'suplemail') 
      VALUES (?, ?, ?, ?, ?, ?)""",
      [Itemid, Itemname,qty,cost,suplier,supemail])

# Modify Item Function
def edit(Itemid, Itemname,qty,cost,suplier,supemail):
  query(
    """UPDATE "items"
    SET ('item_ID', `item_name`, `item_qty`, `item_cost`, 'suplname', 'suplemail')
    VALUES (?, ?, ?, ?, ?, ?)""",
    [Itemid, Itemname,qty,cost,suplier,supemail])    

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
    save(iID, nm,qty,cost,isn,ise)
  return render_template("L4Add.html")

@app.route("/delete<string:ID>")
def delete (ID):
  query("DELETE FROM `items` WHERE `item_ID`=?", [ID])
  return render_template("L4AddDelete.html", items=getAll())

@app.route("/adddelete")
def AD():
  items = getAll()
  return render_template("L4AddDelete.html", items=items)

#Modify  Item
@app.route("/editable-items")
def editableItems():
  items =getAll()
  return render_template("L4ModifyItems.html", items=items)  

@app.route("/editable-items/modify", methods=['GET', 'POST'])
def modify():
  if request.method == 'POST':
    nm = request.form.get("item_name")
    iID = request.form.get("item_ID")
    qty = request.form.get("itemQty") 
    cost = request.form.get("item_cost")
    isn = request.form.get("suplname") 
    ise = request.form.get("suplemail")
    #edit(iID, nm,qty,cost,isn,ise)
  return render_template("L4ModifyItem.html")

@app.route("/edit<string:ID>")
def editItem(ID):
  query("SELECT * FROM `items` WHERE `ID`=?", [ID])
  return render_template("L4ModifyItems.html", items=getAll())  





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

#GET ALL ITEMS
def getAllNotif ():
  return select("SELECT * FROM `notifications`")

#Notifications
@app.route("/notify", methods=['GET', 'POST'])
def notify():
  notifs = getAllNotif()
  if request.method == 'POST':
    # query(
    # "SELECT item_qty FROM `items`")
    # return()

    # threshold = request.form.get("number")
    # if threshold >=  itemQty:
    #   return alert("")
    # else:
    #   pass

    # return 
    # if (threshold) > 10:
    qty = request.form.get("itemQty")
    # if threshold <= qty:
    # flash("Item has fallen below minimum stock level")   
     
    # return redirect(request.url)
  return render_template("L4Notification.html", notifs=notifs)
  

@app.route("/orderitems", methods=['GET', 'POST'])
def order():
  return render_template("L4Email.html", items=getAll())

@app.route("/email<string:suplemail>")
def email (suplemail):
  
  server.login('oraynemc10@gmail.com','fteakcjaerfvvohv')
  server.sendmail('oraynemc10@gmail.com',suplemail,'New items please')  #Place email here
  print('mailsnet')
  return render_template("L4Email.html", items=getAll())

    
# (D) START
if __name__ == "__main__":
  app.run(HOST_NAME, HOST_PORT)
