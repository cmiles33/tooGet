import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import lxml.html
from bs4 import BeautifulSoup
import re
import html2text
import sqlMethods

def emailSubsystem(emailSender,contents):
    #automaticResponse2(emailSender)
    print("Entering subworks")
    myQuary = sqlMethods.mySQLMethods()
    print(emailSender)
    emailSplit = re.split('; |, |\<|\>',emailSender)
    senderName = emailSplit[0]
    emailName = emailSplit[1]
    print(senderName)

    nameOfSender = myQuary.getField('first_name', 'email', emailName)
    if nameOfSender is None:
        print("Email Sender not in system, add to system?")

    else:
        print(nameOfSender[0])
        print("What stage are they at?")
        stage = myQuary.getField('stage','first_name',nameOfSender[0])
        if stage[0] == 0:
            print("We need more information")
        elif stage[0] == 1:
            print("They need there payload for the day")
        elif stage[0] == 2:
            print("The payload has been sent and we're awaiting response")
        elif stage[0] == 3:
            print("There done with there payload no response")
        elif stage is None:
            print("They need a stage, set them to zero")
            myQuary.updateStage(nameOfSender[0],'0')


def payloadResponse(reciever):
    sender_email = 'cmiles33nrs@gmail.com'

    password = ""

    message = MIMEMultipart("alternative")

    message["From"] = sender_email
    message["To"] = reciever
    page = open('pageSends/firstPage.html')
    myTest = BeautifulSoup(page, 'html.parser')

    myQuary = sqlMethods.mySQLMethods()

    myQuary.cursor.execute("select first_name, start, end, payload from contacts where email = '{}' ;".format(reciever))
    contact = myQuary.cursor.fetchall()
    contactTup = contact[0]

    firstName = contactTup[0]
    startTime = contactTup[1]
    endTime = contactTup[2]
    payloadNumber = contactTup[3]
    message["Subject"] = "Hey {} here is payload number {}!".format(firstName, payloadNumber)
    myTest.patronname.append(firstName)
    myTest.starttime.append(startTime)
    myTest.endtime.append(endTime)
    readOut = open('payload/{}/payload{}.txt'.format('cailan',payloadNumber),encoding='utf-8')
    counter = 0
    for lines in readOut:
        if counter == 0:
            myTest.payload0.append(lines)
        if counter == 1:
            myTest.payload1.append(lines)
        if counter == 2:
            myTest.payload2.append(lines)
        if counter == 3:
            myTest.payload3.append(lines)
        if counter == 4:
            myTest.payload4.append(lines)
        if counter == 5:
            myTest.payload5.append(lines)
        if counter == 6:
            myTest.payload6.append(lines)
        if counter == 7:
            myTest.payload7.append(lines)
        counter +=1
        print(lines)

    root = lxml.html.parse(page).getroot()
    #root.make_links_absolute()
    #content = lxml.html.tostring(root)
    content = myTest
    # Create the plain-text and HTML version of your message
    text = """\
    Testing
    How are you?"""
    html = """\
    {}
    """.format(content)

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, reciever, message.as_string()
        )
    payloadNumber += 1  # increase to next payload after its sent
    myQuary.setPayload(firstName,payloadNumber)  # update it in the data base

def automaticResponse2(reciever):
    sender_email = 'cmiles33nrs@gmail.com'
    receiver_email = reciever
    password = ""

    message = MIMEMultipart("alternative")
    message["Subject"] = "TESTING SYSTEM"
    message["From"] = sender_email
    message["To"] = reciever
    page = open('pageSends/autoRE.html')
    myTest = BeautifulSoup(page, 'html.parser')

    content = myTest
    # Create the plain-text and HTML version of your message
    text = """\
    Testing
    How are you?"""
    html = """\
    {}
    """.format(content)

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, reciever, message.as_string()
        )
    quit()


