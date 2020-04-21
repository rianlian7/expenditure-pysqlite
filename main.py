import sqlite3

import os
from db_utils import *


os.system('cls')
state = 1
settingState = 0
conn = dbConnect("mainDB")
dateAuto = 1

while state == 1:
    print("\n1. Input spending record\n2. Show all records\n3. Show year month records\n5. Exit\n0. Settings")
    action = input("What would you like to do: ")

    if action == "1":
        sql_inputData(conn, autoDate=dateAuto)
        print()
    if action == "2":
        sql_fetchRecord(conn)
        print()
    if action == "3":
        sql_fetchMonthRecord(conn)
        print()
    if action == "5":
        state = 0
    if action == "0":
        settingState = 1
        while settingState == 1:
            print("\n1. Set Auto Date: " + str(dateAuto) + "\n4. Exit")
            settingAction = input("What would you like to set? ")
            if settingAction == "1":
                if(dateAuto == 0): 
                    dateAuto = 1 
                else: 
                    dateAuto = 0
            if settingAction == "4":
                settingState = 0



