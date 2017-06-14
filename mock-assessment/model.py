#!usr/bin/env python3

#import schema
import sqlite3

def insert_account(fname, lname, dob, phone_num, address):
    connection = sqlite3.connect('info.db')
    cursor = connection.cursor()
    cursor.execute(
        '''INSERT INTO account(
            fname,
            lname,
            dob,
            phone_num,
            address
        )VALUES(%s, %s, %s, %s, %s);''',
        (fname, lname, dob, phone_num, address)
    )
    connection.commit()
    connection.close()

def select_account(params=()):
    connection = sqlite3.connect('info.db')
    cursor = connection.cursor()
    if params==():
        cursor.execute("select * from account")
    else:
        string = "select"
        for i in xrange(len(params)-1):
            string += "%s,"
        string += "%s"
        string += " from account"
        result = cursor.execute(string)
        connection.close()
        return result.fetchall()

#def get_dob(fname):
#    dob = cursor.execute('SELECT dob FROM account WHERE fname="{}"'.format(fname))
#    dob2 = dob.fetchall()

#    connection.commit()
#    cursor.close()
#    connection.close()

#if __name__ == '__main__':
#    x = get_dob('Narendra')
#    print(x)


