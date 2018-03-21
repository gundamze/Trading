__author__ = 'ryan'



import pyodbc


'''
_________________ wiki/documentation __________________________
https://code.google.com/p/pyodbc/w/list


_________________ How to write configs _________________________
https://www.connectionstrings.com/microsoft-access-accdb-odbc-driver/

'''
configs = 'Driver={Microsoft Access Driver (*.mdb, *.accdb)};' \
          'Dbq=D:\poly\courses\projects\China\database_access\China.accdb'


cnxn = pyodbc.connect(configs)
cursor = cnxn.cursor()

cursor.execute('SHOW TABLES;')


