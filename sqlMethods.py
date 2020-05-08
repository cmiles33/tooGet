import mysql.connector
import smtplib
from mysql.connector import errorcode


import emailSender

class mySQLMethods:

    def __init__(self):

        try:
            self.cnx = mysql.connector.connect(user='caleb', password='password',
                                          host='192.168.1.24', database='myFirstData')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        self.cursor = self.cnx.cursor()


    def add_description(self, name, description):
        try:
            myCommand = "UPDATE contacts SET description = '{}'" \
                        " WHERE first_name = '{}'".format(description, name)
            self.cursor.execute(myCommand)
        except mysql.connector.Error as err:
            print(err.msg)

    def getField(self,field1, field2, name):
        try:

            myCommand = "select {} from contacts where {} = '{}';".format(field1,field2,name)
            self.cursor.execute(myCommand)
            things = []
            for row in self.cursor:
                things.append(row[0])

            return things

        except mysql.connector.Error as err:
            print(err.msg)

    def updateStatus(self, email, status):
        try:
            myCommand = "UPDATE contacts SET status = '{}'" \
                        " WHERE email = '{}'".format(status, email)
            self.cursor.execute(myCommand)
            self.cnx.commit()
        except mysql.connector.Error as err:
            print(err.msg)

    def updateStart(self, name, time):
        try:
            myCommand = "UPDATE contacts SET start = '{}'" \
                        " WHERE first_name = '{}'".format(time, name)
            self.cursor.execute(myCommand)
            self.cnx.commit()
        except mysql.connector.Error as err:
            print(err.msg)

    def updateEnd(self, name, time):
        try:
            myCommand = "UPDATE contacts SET end = '{}'" \
                        " WHERE first_name = '{}'".format(time, name)
            self.cursor.execute(myCommand)
            self.cnx.commit()
        except mysql.connector.Error as err:
            print(err.msg)

    def setPayload(self, name,payload):
        try:
            myCommand = "UPDATE contacts SET payload = '{}'" \
                        " WHERE first_name = '{}'".format(payload, name)
            self.cursor.execute(myCommand)
            self.cnx.commit()
        except mysql.connector.Error as err:
            print(err.msg)


    def add_contact(self, first_name, last_name, phone_number='None', email='None'):
        try:
            command = '''
            INSERT
            INTO
            contacts(
                first_name,
                last_name,
                phone_number,
                email)

            VALUES
            ('{}', '{}', '{}', '{}');
            '''.format(first_name, last_name, phone_number, email)
            self.cursor.execute(command)
            self.cnx.commit()

        except mysql.connector.Error as err:
            print(err.msg)

    def closeConnections(self):
        self.cursor.close()
        self.cnx.close()

    def generalCommand(self,command):
        try:
            self.cursor.execute(command)
            print("Command Executed Sucessfully")
        except mysql.connector.Error as err:
            print(err.msg)









