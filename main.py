import myClient
import sqlMethods
import os
import time
import emailSender
from signal import signal, SIGINT
from sys import exit



from time import localtime, strftime
#import emailHandle

ourTime = strftime("%H:%M",localtime())
print(ourTime)

time2 = "18:03"
if time2 == ourTime:
    print("it works ")

myQuary = sqlMethods.mySQLMethods()

#myQuary.getField('email','start','00:00')
'''
myQuary.updateStatus('cmiles33nrs@gmail.com','false')
myQuary.updateStart('caleb','07:00')
myQuary.updateEnd('caleb','12:00')
myQuary.updateStart('cailan','07:00')
myQuary.updateEnd('cailan','12:00')
'''
myQuary.cursor.execute("SELECT first_name, email, payload, start, end  FROM contacts;")
#rows = myQuary.cursor.fetchall()
#print(rows)
for rows in myQuary.cursor.fetchall():
    print(rows)
    #print(rows)
#myQuary.updateStart('nathan','01:24')
sqlCode = "select email from contacts where start = '{}' and status = 'false';"
#sqlCode = "select email from contacts where status = 'false';"
sqlCode2 = "select email from contacts where end = '{}' ;"
myiterator = 0
myQuary.closeConnections()

thread1 = myClient.thread_with_exception("mythread")
thread1.start()
thread1.sendMessage("Program Started")

def handler(signal_received,frame):
  print("Kill received")
  thread1.raise_exception()
  myQuary.closeConnections()
  thread1.join()
  exit(0)

signal(SIGINT, handler)

while True:
    myQuary = sqlMethods.mySQLMethods()
    ourTime = strftime("%H:%M", localtime())
    stringEmails = ""
    myQuary.cursor.execute(sqlCode.format(ourTime))
    myValues = myQuary.cursor.fetchall()
    print(myValues)

    for emails in myValues:
        emailSender.payloadResponse(emails[0])
        myQuary.updateStatus(emails[0],'true')
        stringEmails += emails[0] + " "
        myiterator +=1

    time.sleep(10)

    myQuary.cursor.execute(sqlCode2.format(ourTime))
    resetEmails = myQuary.cursor.fetchall()
    
    for emails in resetEmails:
        myQuary.updateStatus(emails[0],'false')
        
    myQuary.closeConnections()
    time.sleep(10)
    print("Ran")
    print(ourTime)
    thread1.sendMessage("Running, no issues")
    thread1.sendMessage("Emails sent to: {}".format(stringEmails))



