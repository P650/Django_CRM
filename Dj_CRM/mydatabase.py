#installed mysql
#from installer link
#https://dev.mysql.com/downloads/installer/
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user = "root",
    passwd = "root@12345",

)

#prepare cursor object

cursorObject = dataBase.cursor()

#create database    

cursorObject.execute("CREATE DATABASE pavankumardatabase")

print("all done!!")