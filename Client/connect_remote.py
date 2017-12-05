#!/usr/bin/env python
from __future__import print_function
import sys
#sys.path.insert(0,’python{0}/’.format(sys.version_info[0]))
import mysql.connector
from mysql.connector.constants import ClientFlag
config = {
‘user’ :’root’,
‘password’:’root’
‘host’:’192.168.56.104’,
‘port’:3306,
‘database’:’shop’
}
cnx = mysql.connector.connect(**config)
cur=cnx.cursor()
cur.execute(“SELECT price FROM products”)
print(cur.fetchall())
cur.close()
cnx.close()

