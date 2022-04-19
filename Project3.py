# MGIS.350.01 - Developing Business Applications
# Project 3
# Instructor - Dave Ballard
# Team Member
# - Liu, Kaiwen (kl8399@rit.edu)
# - Xue, Sally (qx4741@rit.edu)
# - Meng, Xing (xm5723@rit.edu)
# Apr 17, 2022

# Library
# tkinter library for graphics
from tkinter import *
from tkinter import messagebox
import traceback
# Libraries for using the database and file system
import sqlite3
import pathlib

# Global Variable
conn = None

invDough = 0.0
invSauce = 0.0
invCheese = 0.0
invPepperoni = 0.0
fdSales = 0.0
fdExpenses = 0.0

# Function
def fnOpenDatabase():
    global conn
    # This function will open the database and print out all of the
    # record to verify it is working
    # dbFile = 'database/HW_Database.sqlite3'
    dbFile = pathlib.Path('P3DB - Template.db')
    if dbFile.exists() == True:         
        conn = sqlite3.connect(dbFile)
        cur = conn.cursor()
        # Execute a test query
        cur.execute("SELECT * FROM finances;")
        records = cur.fetchall()
        print("*** DEBUGGING ***\n", records)
    else:
        messagebox.showerror("Error", "Database not found.")
        quit()

def getDough():
    print("Get Dough")
    try:
        global conn, invDough
        cur = conn.cursor()
        # Create a veriable for our query
        sql = "SELECT dough FROM inventory;"
         # Output the query for debugging
        print("**** debugging ***\nQuery:", sql)
        cur.execute(sql)
        records = cur.fetchall()
        print("*** DEBUGGING ***\n records for display", records)
        lblDough.config(text=records)

        for record in records:
            invDough = record[0]
            print('invDough ', invDough)

    except sqlite3.OperationalError as soe:
        messagebox.showerror("Error", "Database error. Please contact support.\n\n" + str(soe))
        traceback.print_exc()

    # Catch all the error, should be the last one you use
    except Exception as ex:
        messagebox.showerror("Error", "Something went wrong!\n\n" + str(ex))
        traceback.print_exc()

def getCheese():
    print("Get Cheese")
    try:
        global conn, invCheese
        cur = conn.cursor()

        # Create a veriable for our query
        sql = "SELECT cheese FROM inventory;"
         # Output the query for debugging
        print("**** debugging ***\nQuery:", sql)
        cur.execute(sql)
        records = cur.fetchall()
        print("*** DEBUGGING ***\n records for display", records)
        lblCheese.config(text=records)

        for record in records:
            invCheese = record[0]
            print('invCheese ', invCheese)

    except sqlite3.OperationalError as soe:
        messagebox.showerror("Error", "Database error. Please contact support.\n\n" + str(soe))
        traceback.print_exc()

    # Catch all the error, should be the last one you use
    except Exception as ex:
        messagebox.showerror("Error", "Something went wrong!\n\n" + str(ex))
        traceback.print_exc()

def getPepperoni():
    print("Get Pepperoni")
    try:
        global conn, invPepperoni
        cur = conn.cursor()

        # Create a veriable for our query
        sql = "SELECT pepperoni FROM inventory;"
         # Output the query for debugging
        print("**** debugging ***\nQuery:", sql)
        cur.execute(sql)
        records = cur.fetchall()
        print("*** DEBUGGING ***\n records for display", records)
        lblPepperoni.config(text=records)

        for record in records:
            invPepperoni = record[0]
            print('invPepperoni ', invPepperoni)

    except sqlite3.OperationalError as soe:
        messagebox.showerror("Error", "Database error. Please contact support.\n\n" + str(soe))
        traceback.print_exc()

    # Catch all the error, should be the last one you use
    except Exception as ex:
        messagebox.showerror("Error", "Something went wrong!\n\n" + str(ex))
        traceback.print_exc()

def updateDough():
    print("-----------------------Update Dough")
    try:
        global conn, invDough
        cur = conn.cursor()
        # Create a veriable for our query
        sql = "UPDATE inventory SET dough = '"+ str(invDough + 100)+ "' WHERE id = 1;"
        # Output the query for debugging
        print("**** debugging ***\nQuery:", sql)
        cur.execute(sql)
        conn.commit()
        print("End")
        getDough()
    
    except sqlite3.OperationalError as soe:
        messagebox.showerror("Error", "Database error. Please contact support.\n\n" + str(soe))
        traceback.print_exc()

    # Catch all the error, should be the last one you use
    except Exception as ex:
        messagebox.showerror("Error", "Something went wrong!\n\n" + str(ex))
        traceback.print_exc()

def updateCheese():
    print("-----------------------Update Cheese")
    try:
        global conn, invCheese
        cur = conn.cursor()
        # Create a veriable for our query
        sql = "UPDATE inventory SET cheese = '"+ str(invCheese + 100)+ "' WHERE id = 1;"
        # Output the query for debugging
        print("**** debugging ***\nQuery:", sql)
        cur.execute(sql)
        conn.commit()
        print("End")
        getCheese()
    
    except sqlite3.OperationalError as soe:
        messagebox.showerror("Error", "Database error. Please contact support.\n\n" + str(soe))
        traceback.print_exc()

    # Catch all the error, should be the last one you use
    except Exception as ex:
        messagebox.showerror("Error", "Something went wrong!\n\n" + str(ex))
        traceback.print_exc()

def updatePepperoni():
    print("-----------------------Update Pepperoni")
    try:
        global conn, invPepperoni
        cur = conn.cursor()
        # Create a veriable for our query
        sql = "UPDATE inventory SET pepperoni = '"+ str(invPepperoni + 100)+ "' WHERE id = 1;"
        # Output the query for debugging
        print("**** debugging ***\nQuery:", sql)
        cur.execute(sql)
        conn.commit()
        print("End")
        getPepperoni()
    
    except sqlite3.OperationalError as soe:
        messagebox.showerror("Error", "Database error. Please contact support.\n\n" + str(soe))
        traceback.print_exc()

    # Catch all the error, should be the last one you use
    except Exception as ex:
        messagebox.showerror("Error", "Something went wrong!\n\n" + str(ex))
        traceback.print_exc()

def getInventory():
    getDough()
    getCheese()
    getPepperoni()

# Function for adding dough to inventory
def UpdateInventory():
    global invDough, invSauce, invCheese, invPepperoni, fdExpenses
    if addDough.get() == 1:
        updateDough()

        # fdExpenses += 20
    # if addSauce.get() == 1:
        # invSauce += 100
        # fdExpenses += 10
    if addCheese.get() == 1:
          updateCheese()
    #     fdExpenses += 25
    if addPepperoni.get() == 1:
        updatePepperoni()
    #     fdExpenses += 40

# GUI
root = Tk()
root.title("Project 2")
root.geometry("960x600")

# Label
Label(root, text="INVENTORY").grid(row=0, column=0, columnspan=3, sticky=W)
Label(root, text=" ").grid(row=1, column=0, sticky=W) # Spacer to indent column
Label(root, text="Dough:").grid(row=1, column=1, sticky=W)
Label(root, text="Sauce:").grid(row=2, column=1, sticky=W)
Label(root, text="Cheese:").grid(row=3, column=1, sticky=W)
Label(root, text="Pepperoni:").grid(row=4, column=1, sticky=W)

lblDough = Label(root, text="-")
lblDough.grid(row=1, column=2, sticky=W)
lblSauce = Label(root, text="-")
lblSauce.grid(row=2, column=2, sticky=W)
lblCheese = Label(root, text="-")
lblCheese.grid(row=3, column=2, sticky=W)
lblPepperoni = Label(root, text="-")
lblPepperoni.grid(row=4, column=2, sticky=W)

Label(root, text=" ").grid(row=0, column=9, sticky=W) # Spacer between inventory & add to inventory
Label(root, text="ADD TO INVENTORY").grid(row=0, column=10, columnspan=2, sticky=W)
Label(root, text=" ").grid(row=1, column=10, sticky=W) # Spacer to indent column
addDough = IntVar()
addSauce = IntVar()
addCheese = IntVar()
addPepperoni = IntVar()
Checkbutton(root, text="Add Dough", variable=addDough).grid(row=1, column=11, sticky=W)
Checkbutton(root, text="Add Sauce", variable=addSauce).grid(row=2, column=11, sticky=W)
Checkbutton(root, text="Add Cheese", variable=addCheese).grid(row=3, column=11, sticky=W)
Checkbutton(root, text="Add Pepperoni", variable=addPepperoni).grid(row=4, column=11,sticky=W)
Button(root, text="Add To Inventory", command=UpdateInventory).grid(row=5, column=11,sticky=W)

Label(root, text=" ").grid(row=1, column=19, sticky=W) # Spacer between add to inventory & order form
Label(root, text="ORDER FORM").grid(row=0, column=20, columnspan=3, sticky=W)
Label(root, text=" ").grid(row=1, column=20, sticky=W) # Spacer to indent column
Label(root, text="Quantity:").grid(row=1, column=21, sticky=W)
entQuantity = Entry(root, width=5)
entQuantity.grid(row=1, column=22, sticky=W)

pizzaType = IntVar()
Radiobutton(root, text="Cheeze Pizza", variable=pizzaType, value=0).grid(row=2, column=21, columnspan=2, sticky=W)
Radiobutton(root, text="Cheese & Pepperoni", variable=pizzaType, value=1).grid(row=3,column=21, columnspan=2, sticky=W)
# Button(root, text="Add To Order", command=fnAddToOrder).grid(row=4, column=21,columnspan=2, sticky=W)
Button(root, text="Add To Order").grid(row=4, column=21,columnspan=2, sticky=W)

Label(root, text=" ").grid(row=9, column=0) # Row spacer
Label(root, text="REVIEW ORDER").grid(row=10, column=20, columnspan=3, sticky=W)
frmItems = Frame(root)
frmItems.grid(row=11, column=21, columnspan=3, rowspan=5, sticky=W)
scrItems = Scrollbar(frmItems)
scrItems.grid(row=0, column=1, sticky=N+S+W)
lstItems = Listbox(frmItems, height=5, width=40, yscrollcommand=scrItems.set)
lstItems.grid(row=0, column=0)
scrItems.config(command=lstItems.yview)

# Button(root, text="Place Order", command=fnPlaceOrder).grid(row=19, column=21, sticky=W)
# Button(root, text="Remove Selected", command=fnRemoveItem).grid(row=19, column=22,sticky=W)
# Button(root, text="Cancel Order", command=fnCancelOrder).grid(row=19, column=23, sticky=W)

Button(root, text="Place Order").grid(row=19, column=21, sticky=W)
Button(root, text="Remove Selected").grid(row=19, column=22,sticky=W)
Button(root, text="Cancel Order").grid(row=19, column=23, sticky=W)

Label(root, text=" ").grid(row=0, column=29, sticky=W) # Spacer between add to order form & financial data
Label(root, text="FINANCIAL DATA").grid(row=0, column=30, columnspan=3, sticky=W)
Label(root, text=" ").grid(row=1, column=30, sticky=W) # Spacer to indent column
Label(root, text="Sales:").grid(row=1, column=31, sticky=W)
Label(root, text="Expenses:").grid(row=2, column=31, sticky=W)
Label(root, text="Profits:").grid(row=3, column=31, sticky=W)

lblSales = Label(root, text="-")
lblSales.grid(row=1, column=32, sticky=W)
lblExpenses = Label(root, text="-")
lblExpenses.grid(row=2, column=32, sticky=W)
lblProfits = Label(root, text="-")
lblProfits.grid(row=3, column=32, sticky=W)

# PAST ORDERS
Label(root, text=" ").grid(row=20, column=0) # Row spacer
Label(root, text="PAST ORDERS").grid(row=21, column=0, columnspan=3, sticky=W)
frmPastItems = Frame(root)
frmPastItems.grid(row=22, column=0, columnspan=25, rowspan=5, sticky=W)
scrPastItems = Scrollbar(frmPastItems)
scrPastItems.grid(row=0, column=1, sticky=N+S+W)
lstPastItems = Listbox(frmPastItems, height=5, width=25, yscrollcommand=scrPastItems.set)
lstPastItems.grid(row=0, column=0)
scrPastItems.config(command=lstPastItems.yview)

# PAST ORDERS DEAILS
Label(root, text=" ").grid(row=20, column=20) # Row spacer
Label(root, text="PAST ORDERS DEAILS").grid(row=21, column=20, columnspan=3, sticky=W)
frmPastItems = Frame(root)
frmPastItems.grid(row=22, column=20, columnspan=30, rowspan=5, sticky=W)
scrPastItems = Scrollbar(frmPastItems)
scrPastItems.grid(row=0, column=1, sticky=N+S+W)
lstPastItems = Listbox(frmPastItems, height=5, width=45, yscrollcommand=scrPastItems.set)
lstPastItems.grid(row=0, column=0)
scrPastItems.config(command=lstPastItems.yview)

Button(root, text="Show Order Details").grid(row=28, column=0, columnspan=3, sticky=W)

# Connect and open the database
fnOpenDatabase()

getInventory()

# Open the windows
root.mainloop()