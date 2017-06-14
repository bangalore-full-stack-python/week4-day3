#!usr/bin/env python3

import sqlite3

connection = sqlite3.connect('info.db')
cursor = connection.cursor()

cursor.execute(
    '''CREATE TABLE account(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        fname VARCHAR(64),
        lname VARCHAR(64),
        dob VARCHAR(64),
        phone_num VARCHAR(64),
        address VARCHAR(128)
    );'''
)
cursor.execute(
    '''INSERT INTO account(
        fname,
        lname,
        dob,
        phone_num,
        address
        ) VALUES(
            "Narendra",
            "Modi",
            "01-01-1955",
            "123-456-7890",
            "321, PM House, New Delhi, India 110001"
    );'''
)

connection.commit()
cursor.close()
connection.close()
