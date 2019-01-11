import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os.path import basename
import email
import email.mime.application
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import csv

with open('emails.csv','rb') as f:
	reader=csv.reader(f)
	your_list=list(reader)

for i in range(len(your_list)):

	gmailUser = ''
	gmailPassword = ''
	recipient = your_list[i][2]
	message="""
	Hi """+your_list[i][0]+""" """+your_list[i][1]+"""!,

		Thanks For Attending ASIET Local Hack Day!
		We Would Love to Hear What You Thought Of The Event.
		Please Fill Out This Google Form To Let Us Know!
		https://goo.gl/forms/1IGWANh2jfBFLz9q2
		Please Note Your Certificates will be mailed to you in the upcoming days.
	
		-ASIET HackDay Team"""
	msg = MIMEMultipart()
	msg['From'] = gmailUser
	msg['To'] = recipient
	msg['Subject'] = "ASIET Local HackDay Feedback"
	msg.attach(MIMEText(message))
	filename=your_list[i][3]
	'''fo=open(filename,'rb')
	attach = email.mime.application.MIMEApplication(fo.read(),_subtype="pdf")
	fo.close()
	attach.add_header('Content-Disposition','attachment',filename=filename)
	'''
	# Attachment and HTML to body message.
	#msg.attach(attach)

	mailServer = smtplib.SMTP('smtp.gmail.com', 587)
	mailServer.ehlo()
	mailServer.starttls()
	mailServer.ehlo()
	mailServer.login(gmailUser, gmailPassword)
	mailServer.sendmail(gmailUser, recipient, msg.as_string())
	print "Email Has Been Sent To "+your_list[i][0]+" "+your_list[i][1]+", Email Number"+str(i)+" Email Id:"+recipient