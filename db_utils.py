# db_utils.py
import sqlite3
import datetime
from sqlite3 import Error

recordList = []

def dbConnect(dbName):

    try:
        conn = sqlite3.connect(dbName + ".db")
        print("Connection established")
    except Error:
        print(Error)
    
    return conn

def sql_fetchRecord(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM spending')
    rows = cur.fetchall()
    print()
    for row in rows:
        print(row)

def sql_inputData(conn, autoDate):
    print("\nEnter your purchase info")
    if autoDate == 1:
        pur_date = datetime.datetime.today().date()
    if autoDate == 0:
        print("Purchase Date: ")
        pur_year = int(input("Year: "))
        pur_month = int(input("Month: "))
        pur_day = int(input("Day: "))
        pur_date = datetime.datetime(pur_year, pur_month, pur_day).date()
    pur_name = input("Name: ")
    pur_cost = int(input("Cost(RM): "))
    pur_category = input("Category: ")
    pur_req = input("Need/Want?: ")
    dictData = {
        "Purchase Date" : pur_date,
        "Name" : pur_name,
        "Cost" : pur_cost,
        "Category" : pur_category,
        "Need / Want" : pur_req
    }
    recordTup = (pur_name, pur_category, pur_cost, pur_date, pur_req)
    print("Data Inputed")
    print(recordTup)
    print()
    recordList.append(dictData)
    
    cur = conn.cursor()
    cur.execute('INSERT INTO spending(name, category, amount, pay_date, req) VALUES (?, ?, ?, ?, ?)', recordTup)
    conn.commit()



def sql_fetchMonthRecord(conn):
    yearOnly = 1

    cur = conn.cursor()
    yearRec = input("Enter year(YYYY): ")
    monthRec = input("(Year Only if Blank) Enter month(MM): ")
    if  monthRec == "" or monthRec == " ":
        yearOnlyRec = "'" + yearRec + "%'"
        cur.execute("SELECT * FROM spending WHERE pay_date LIKE " + yearOnlyRec)
    else:
        yearMonthRec = "'" + yearRec + "-" + monthRec + "%'"
        cur.execute("SELECT * FROM spending WHERE pay_date LIKE " + yearMonthRec)

    rows = cur.fetchall()
    for row in rows:
        print(row)