import socket
import sys
import time
import mysql.connector
from mysql.connector.constants import ClientFlag

config = {
        'user':'root',
        'password':'root',
        'host':'127.0.0.1',
        'database':'shop'
}
cnx=mysql.connector.connect(**config)
mysql_cursor=cnx.cursor()

PORT=6789
serversocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST="192.168.56.101"
print 'socket created'
try:
        serversocket.bind((HOST, PORT))
except socket.error, msg:
        print 'BInd failed.error code:'
serversocket.listen(200)
while True:
	conn, addr = serversocket.accept()
	data = conn.recv(100000)
	print(data)
	data=data.split(",")
	query='SELECT price FROM products where name="{}" AND store="{}"'.format(data[0],data[1])
	print(query)
	mysql_cursor.execute(query)
	output=mysql_cursor.fetchall()
	output=str(output)
	print(output)
	conn.sendall(output)
conn.close()
mysql_cursor.close()
s.close()
