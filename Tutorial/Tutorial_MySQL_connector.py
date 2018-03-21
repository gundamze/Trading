__author__ = 'ryan'

import mysql.connector

cnx = mysql.connector.connect(user='root', password='123456',
                              host='127.0.0.1')

#create a Cursor object.
cur = cnx.cursor()




cnx.database


cnx.close()
