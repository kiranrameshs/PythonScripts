#!/usr/bin/python

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import copy
import traceback
import itertools
import os
import sys
import re
from collections import Counter
from collections import OrderedDict
from collections import defaultdict

class Reports:
	
	def send_email(self):
		try: 
			print("In the send_email function")
			msgbody = "<h3> Summary:</h3>"  #Add mail content in html
			msg = MIMEMultipart()
			msg.attach(MIMEText(msgbody,'html'))
			filetoattch ="TestReport.html"  #Adding file to be attached to mail
			
			with open(filetoattch, "rb") as fil:
				msg.attach(MIMEApplication(
					fil.read(),
					Content_Disposition='attachment; filename="%s"' % basename(filetoattch),
					Name=basename(filetoattch)
				))

			msg['Subject'] = 'Report'       #Subject of the mail
			msg['From'] = 'donotreply@xyz.com'  #From mail ID       
			COMMASPACE = ', '
			msg['To'] = 'friend@xyz.com'    #Recipient mail ID

			s = smtplib.SMTP('mail.xyz.com')    #domain name
			print("sending mail")
			s.send_message(msg)
			print("sent mail")
			s.quit()
		except Exception as err:
			print ("Error : "+str(err))
			print(traceback.format_exc())
			
objTCContoler = Reports()
objTCContoler.send_email()
		
