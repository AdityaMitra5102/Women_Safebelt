
from flask import * 
import pyodbc
server = 'tcp:safebelt.database.windows.net'
database = 'SECURITY'
username = 'womensafety01'
password = '{Anisha28}'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                      server+';DATABASE='+database+';UID='+username+';PWD=' + password)
cursor = cnxn.cursor()

def createTable():
    try:
        cursor.execute(
            "CREATE TABLE [SECURITY](UID VARCHAR(30) , NAME VARCHAR(40) ,EMAIL VARCHAR(30)) ")
        cursor.commit()
    except:
        pass

def getEMAIL_BY_UID(UID):
        try:
            command = 'SELECT EMAIL FROM [SECURITY] WHERE UID=?'
            cursor.execute(command, UID)
            retValue = cursor.fetchone()[0]
            cursor.commit()
            print(retValue)
            return retValue
        except:
            return "Error"
			
			
def getNAME_BY_UID(UID):
        try:
            command = 'SELECT NAME FROM [SECURITY] WHERE UID=?'
            cursor.execute(command, UID)
            retValue = cursor.fetchone()[0]
            cursor.commit()
            print(retValue)
            return retValue
        except:
            return "Error"


def addUser(UID, NAME, EMAIL):
    try:
        command = 'INSERT INTO [SECURITY] VALUES (?,?,?)'
        cursor.execute(command, UID, NAME, EMAIL)
        cursor.commit()
    except:
        createTable()
        try:
            command = 'INSERT INTO [SECURITY] VALUES (?,?,?)'
            cursor.execute(command, UID, NAME, EMAIL)
            cursor.commit()
        except:
            pass
