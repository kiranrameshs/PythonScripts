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
	def __init__(self):
		print("Calling Reports constructor")
		
	def send_email(self,DefectDensity,OpenDefect,KLOC):
		try: 
			print("In the send_email function")
			message = """<html>
			<head></head>
			<body>
			<table border=1>
			<tr bgcolor=#6495ED><th colspan=2>Details</th></tr>"""
			DefectDensity_STR = str(DefectDensity)
			OpenDefect_STR = str(OpenDefect) 
			KLOC_STR = str(KLOC)
			message +=     "<tr><td >RDD - Release Defect Density</th><td>" + DefectDensity_STR +"</td></tr>"
			message +=     "<tr><td >ORDD - Open Release Defect Density</th><td>" + OpenDefect_STR +"</td></tr>"       
			message +=     "<tr><td >KLOC - K Lines of Code</th><td>" + KLOC_STR +"</td></tr>"       
			msgbody = "<h3>Metrics Summary:</h3>"
			msg = MIMEMultipart()
			regards = "<br>Best Regards, <br> Insight Team"
			msg.attach(MIMEText('Hi All,<br><br>    Please find the attached metrics report <br><br>'+message+'<br><br>','html'))
			msg['Subject'] = 'Project Metrics Dashboard'
			msg['From'] = 'insight@xyz.com'
			To_list = "1@xyz.com,2@xyz.com,3@xyz.com,4@xyz.com,5@xyz.com"
			COMMASPACE = ', '
			msg['To'] = To_list
			s = smtplib.SMTP('mail.xyz.com')
			print("sending mail")
			s.send_message(msg)
			print("sent mail")
			s.quit()
		except Exception as err:
			print ("Error : "+str(err))
			print(traceback.format_exc())
			
		
