#!usr/bin/env python3

#import schema
import sqlite3

# def insert_account(fname, lname, dob, phone_num, address):
#     connection = sqlite3.connect('info.db')
#     cursor = connection.cursor()
#     cursor.execute(
#         '''INSERT INTO account(
#             fname,
#             lname,
#             dob,
#             phone_num,
#             address
#         )VALUES(%s, %s, %s, %s, %s);''',
#         (fname, lname, dob, phone_num, address)
#     )
#     connection.commit()
#     connection.close()

def read_fname_by_last_name(something):
    connection = sqlite3.connect('info.db')
    cursor = connection.cursor()
    cursor.execute('SELECT fname FROM account WHERE lname="{}"'.format(something))
    z = cursor.fetchall()[0][0]
    print(z)

def read_lname_by_first_name(something):
    connection = sqlite3.connect('info.db')
    cursor = connection.cursor()
    cursor.execute('SELECT lname FROM account WHERE fname="{}"'.format(something))
    z = cursor.fetchall()[0][0]
    print(z)

def read_dob_by_first_name(something):
    connection = sqlite3.connect('info.db')
    cursor = connection.cursor()
    cursor.execute('SELECT dob FROM account WHERE fname="{}"'.format(something))
    z = cursor.fetchall()[0][0]
    print(z)

def read_ph_num_by_first_name(something):
    connection = sqlite3.connect('info.db')
    cursor = connection.cursor()
    cursor.execute('SELECT phone_num FROM account WHERE fname="{}"'.format(something))
    z = cursor.fetchall()[0][0]
    print(z)

def read_address_by_first_name(something):
    connection = sqlite3.connect('info.db')
    cursor = connection.cursor()
    cursor.execute('SELECT address FROM account WHERE fname="{}"'.format(something))
    z = cursor.fetchall()[0][0]
    print(z)


if __name__ == '__main__':
    read_fname_by_last_name('Modi')
    read_lname_by_first_name('Narendra')
    read_dob_by_first_name('Narendra')
    read_ph_num_by_first_name('Narendra')
    read_address_by_first_name('Narendra')
