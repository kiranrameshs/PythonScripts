import requests
from bs4 import BeautifulSoup
from jira.client import GreenHopper
from jira import JIRA
import time
import json
import sys
import re
import psycopg2
import traceback
from datetime import datetime, timedelta		
import datetime as dt
class jira_query:
	
	def main(self):
		try:
			jira_options = {
			'server': 'https://alm.xyz.com/jira'}
			self.gh = GreenHopper(basic_auth=("marathon", "xyz1234"),options=jira_options)
			self.jira = JIRA(basic_auth=("marathon", "xyz1234"), options= jira_options)
			self.board_list = {}
			self.sprint_list = {}
			self.dict_sid_start_end = {}
			self.boardid_sprintid = []
			#while True:
			list_key = self.find_projects()
			for project_key in list_key:
				self.find_sprint_info (project_key)
			list_boards = self.find_boards()
			self.delete_tables("marathon_DEMO")
			print("Delete tables Function complete")
			self.create_tables()
			print("Created tables Function complete")
			self.find_sprints_insert_to_db()
			print("Inserted data to tables Function complete")
			self.disconnect_from_db()
			print("Disconnected from db")
			time.sleep(20)
			print("Going to update DB")
			self.delete_testlink_tables()
			print("Delete tables Function complete")
			self.create_testlink_tables()
			self.connect_to_db()
			print("Connected to db")
			#Dublink
			self.calc_testlink_overall_results ('marathon','abcd@1234','b7970ae420d3362919955804bc3c8cb2f906665ed98ec02e894f40e9cb08c540','1350997','DUB')
	                # Edinburgh
			self.calc_testlink_overall_results 	('marathon','abcd@1234','b7970ae420d3362919955804bc3c8cb2f906665ed98ec02e894f40e9cb08c540','1380837','EDBH')
	                #Verizon DTG
			self.calc_testlink_overall_results ('marathon','abcd@1234','b7970ae420d3362919955804bc3c8cb2f906665ed98ec02e894f40e9cb08c540','1292224','VZDTG')
	                #5G QCOM
			self.calc_testlink_overall_results ('marathon','abcd@1234','b7970ae420d3362919955804bc3c8cb2f906665ed98ec02e894f40e9cb08c540','1342007','TENBPLUS')
	                #FE 3.1
			self.calc_testlink_overall_results ('marathon','abcd@1234','b7970ae420d3362919955804bc3c8cb2f906665ed98ec02e894f40e9cb08c540','1246352','CAEL')
			self.disconnect_from_db()
			print("Disconnected from db")
			self.delete_defect_density_tables()
			print("Delete tables Function complete")
			self.connect_to_db()
			print("Connected to db")
			self.create_defect_density_tables()
			print("Create tables Function complete")
			self.connect_to_db()
			print("Connected to db")
			self.defect_density()
			self.disconnect_from_db()
			print("Disconnected from db")
		except Exception as err:			
			print ("Error Occurred in init: "+str(err))
			print (traceback.format_exc())
	
	
	def connect_to_db(self):
		try:
			self.conn = psycopg2.connect(database = "sentestdb", user = "postgres", password = "root123", host = "127.0.0.1", port = "5432")
			print ("Connected to database successfully")
			self.cur = self.conn.cursor() 
		except Exception as err:			
			print ("Error Occurred in init: "+str(err))
			print (traceback.format_exc())

	def defect_density(self):
		proj_list = ['EDBH','TENBPLUS','VZDTG','VZDE','LMCOUSEIM','CAEL','DUB']
		for eachproj in proj_list:
			self.cur.execute("SELECT STARTDATE from marathon_DEMO WHERE PROJKEY = (%s) ORDER BY STARTDATE ASC;",(eachproj,))
			rows = self.cur.fetchall()
			print("rows is "+str(rows))
			sd = self.format_date_from_db(rows)
			total_defects_density = self.total_defects (str(eachproj),str(sd))
			open_defects_density  = self.open_defects (str(eachproj),str(sd))
			self.cur.execute("INSERT INTO DEFECTDENSITY_DEMO (PROJKEY,TOTAL_DEFECTS,OPEN_DEFECTS) VALUES (%s,%s,%s)",(eachproj,total_defects_density, open_defects_density));
			self.conn.commit()


	def format_date_from_db(self,rows):
		s= str(rows[0]).split("(")[2].split(")")[0].split(", ")
		print("S is "+str(s))
		date = ""
		for each in range(len(s)):
			if len(s[each])<2:
				date += ('0'+s[each])
				print("Date is "+str(date))
			else:
				date += (s[each])
				print("Date is "+str(date))
				print("No change in formatting")
		start_date_time_frmt = datetime(year=int(date[0:4]), month=int(date[4:6]), day=int(date[6:8]))
		start_date_frmt = str(start_date_time_frmt)[0:10]
		return (str(start_date_frmt))

			
	def disconnect_from_db(self):
		try:
			self.conn.commit()
			self.conn.close()
			print ("Disconnected from database successfully")
		except Exception as err:			
			print ("Error Occurred in init: "+str(err))
			print (traceback.format_exc())
			
	def create_tables(self):
		try:
			self.connect_to_db()
			self.cur.execute('''CREATE TABLE marathon_DEMO 
					  (PID TEXT PRIMARY KEY	 NOT NULL,
					  BOARDID	 TEXT	 NOT NULL,
					  BOARDNAME		   TEXT	NOT NULL,
					  PROJKEY			TEXT	 ,
					  SPRINTNAME		TEXT	 NOT NULL,
					  SPRINTID		 TEXT	   NOT NULL,
					  STARTDATE		DATE	  ,
					  ENDDATE		  DATE	  ,
					  LOC		  TEXT	  );''')
			print ("Table created successfully")
			self.disconnect_from_db()
		except Exception as err:			
			print ("Error Occurred in init: "+str(err))
			print (traceback.format_exc())

	def create_testlink_tables(self):
                try:
                        self.connect_to_db()
                        self.cur.execute('''CREATE TABLE TESTLINK_DEMO 
                                          (PROJ_CYCLE_ID TEXT PRIMARY KEY  NOT NULL,
                                          PROJECTNAME        TEXT    NOT NULL,
                                          CYCLE        TEXT    NOT NULL,
                                          TOTAL_PLANNED     TEXT NOT NULL,
                                          TOTAL_EXECUTED     TEXT NOT NULL,
                                          PASS_PERCENTAGE    TEXT     ,
                                          EXECUTION_PERCENTAGE  TEXT);''')
                        print ("Table created successfully")
                        self.disconnect_from_db()
                except Exception as err:
                        print ("Error Occurred in init: "+str(err))
                        print (traceback.format_exc())
			
	
	def create_defect_density_tables(self):
                try:
                        self.connect_to_db()
                        self.cur.execute('''CREATE TABLE DEFECTDENSITY_DEMO 
                                          (PROJKEY TEXT PRIMARY KEY  NOT NULL,
                                          TOTAL_DEFECTS        TEXT    NOT NULL,
                                          OPEN_DEFECTS        TEXT    NOT NULL);''')
                        print ("Table created successfully")
                        self.disconnect_from_db()
                except Exception as err:
                        print ("Error Occurred in init: "+str(err))
                        print (traceback.format_exc())
			
	

	def delete_tables(self):
		try:
			self.connect_to_db()
			self.cur.execute('''DROP TABLE marathon_DEMO ;''')
			print ("Table deleted successfully")
			self.disconnect_from_db()
		except Exception as err:			
			print ("Error Occurred in init: "+str(err))
			print (traceback.format_exc())

	def delete_testlink_tables(self):
		try:
			self.connect_to_db()
			self.cur.execute('''DROP TABLE TESTLINK_DEMO ;''')
			print ("Table deleted successfully")
			self.disconnect_from_db()
		except Exception as err:			
			print ("Error Occurred in init: "+str(err))
			print (traceback.format_exc())


	def delete_defect_density_tables(self):
		try:
			self.connect_to_db()
			self.cur.execute('''DROP TABLE DEFECTDENSITY_DEMO ;''')
			print ("Table deleted successfully")
			self.disconnect_from_db()
		except Exception as err:			
			print ("Error Occurred in init: "+str(err))
			print (traceback.format_exc())
			
	def find_projects (self):
		try:
			list_projects = self.jira.projects()
			return (list_projects)
		except Exception as err:			
			print ("Error Occurred in init: "+str(err))
			print (traceback.format_exc())		
	
	def find_boards (self):
		try:
			list_boards = self.gh.boards()
			for boards in list_boards:
				board_id = boards.id
				board_name = boards.name
				self.board_list.update({board_name:board_id})	 
			return (self.board_list)
		except Exception as err:			
			print ("Error Occurred in init: "+str(err))
			print (traceback.format_exc())	
		
	def find_sprints_insert_to_db(self):
		try:
			for k,v in self.board_list.items():
				iter = 0
				temp_list = []
				sprint_list= self.gh.sprints(v)
				for sprint in sprint_list:
					sprint_id = sprint.id
					if (iter == 0):
						temp_list.append(sprint.name) 
						sprint_name = sprint.name
					elif (sprint.name in temp_list):
						sprint_name = sprint.name+'_'+str(iter)
					else:
						temp_list.append(sprint.name)  
						sprint_name = sprint.name 
					PID = k+sprint_name
					if sprint_id not in self.dict_sid_start_end.keys():
						pass
					else:
						(project_key,start,end) = self.dict_sid_start_end[sprint_id]
						dict_proj_rep = {}
						start_date =self.format_date(start)
						end_date =self.format_date(end)
						print(str(start_date)+"  "+str(end_date))
						dict_proj_rep['TENBPLUS'] = 'LTE_eNB'
						dict_proj_rep['DUB'] = ''
						dict_proj_rep['EDBH'] = ''
						dict_proj_rep['CAEL'] = 'fe-2k'
						dict_proj_rep['LMCOUSEIM'] = 'LMCO_UeSim'
						dict_proj_rep['VZDTG'] = 'vz_intel_master'
						if str(project_key) in dict_proj_rep.keys() and dict_proj_rep[project_key] !="":
							print("Match found for proj "+str(project_key) )
							loc = self.calc_loc_overall_results(dict_proj_rep[project_key],start_date,end_date)
							print("loc is "+str(loc)+" for repo "+str(dict_proj_rep[project_key]))
						else:
							print("Project not present")
							loc = 0
						''' print ("project_key is ", project_key)
						print ("start is ", start)
						print ("end is ", end)
						print ("board name is ", k)
						print ("Primary Key is",PID)
						print ("Sprint Name is ", sprint_name)
						print ("Sprint id is ", sprint_id)'''
						self.cur.execute("INSERT INTO marathon_DEMO (PID,BOARDID,BOARDNAME,PROJKEY,SPRINTNAME,SPRINTID,STARTDATE,ENDDATE,LOC) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(PID,v, k, project_key, sprint_name,sprint_id,start_date,end_date,loc ));
						self.conn.commit()
					iter+=1
			return
		except Exception as err:			
			print ("Error Occurred in init: "+str(err))
			print (traceback.format_exc())
			
	def find_sprint_info (self,projectKey):
		s = requests.Session()
		s.auth = ("marathon", "xyz1234")
		s.headers.update({"Content-Type": "application/json"})
		j1 = "https://alm.xyz.com/jira/rest/greenhopper/1.0/integration/teamcalendars/sprint/list?jql=project="+str(projectKey)
		# print (j1)
		b = s.get(j1)
		d = json.loads(b.text)
		out = d['sprints']
		count = str(out).count("start")
		iter = 0
		while (iter < count):
			startDate = d['sprints'][iter]['start'][:8]
			endDate   = d['sprints'][iter]['end'][:8]
			id = d['sprints'][iter]['id']
			self.dict_sid_start_end.update ({id:(str(projectKey),startDate,endDate)})
			iter+=1
		return (self.dict_sid_start_end)

	def calc_testlink_overall_results (self,user_name,password,api_key,t_planid,proj_name):
		# Fill in your details here to be posted to the login form.
		payload = {
			'Login': user_name,
			'Password': password
			}	
		 # Use 'with' to ensure the session context is closed after use.
		with requests.Session() as s:
			count = 13
			total_fail =0
			iter =0 
			total_pass =0 
			total_executed=0
			total_planned =0 
			total_notapp =0
			project_id = '2959'
			tplan_id =  t_planid
			p = s.post('http://intestlink01.xyz.com/testlink-1.9.14/', data=payload)
			r = s.get('http://intestlink01.xyz.com/testlink-1.9.14/lib/results/resultsGeneral.php?apikey='+api_key+'&tproject_id='+project_id+'&tplan_id='+tplan_id+'&format=0')
			data = []
			soup = BeautifulSoup(r.content, 'html.parser')
			table=soup.find('table', {'class': 'simple_tableruler sortable'})
			abbs=table.find_all('td')
			values = [ele.text.strip() for ele in abbs]
			total_elements = len(values)
			total_cycle = total_elements/count
			# 13 value is caulated from number of coloumn in testlink
			print ("total number of cycle is ",total_elements/13 )
		
	 
		
		while (iter<total_cycle):
			Cycle_Pass_Per = 0
			Cycle_total_planned = 0
			Cycle_notapp = 0 
			Cycle__pass = 0
			Cycle_fail = 0
			test_cycle_name = (values[0+(count*iter)])
			print (test_cycle_name)
			id = str(test_cycle_name)+'_'+str(proj_name)
			Cycle_total_planned = int(values[1+(count*iter)])
			print (Cycle_total_planned)
			Cycle_notapp = int(values[10+(count*iter)])
			print (Cycle_notapp) 
			Cycle_pass =  int(values[4+(count*iter)]) 
			print (Cycle_pass)
			Cycle_fail =  int(values[6+(count*iter)]) 
			print (Cycle_fail)  
			Cycle_total_planned = Cycle_total_planned - Cycle_notapp
			print (Cycle_total_planned)	
			Cycle_executed =  Cycle_pass+Cycle_fail   
			print (Cycle_executed)
			try:
				Cycle_Pass_Per =  (Cycle_pass/Cycle_executed)*100
				print (Cycle_Pass_Per)
			except ZeroDivisionError:
				Cycle_Pass_Per = 0
				print (Cycle_Pass_Per)
			try:	
				Cycle_exe_per = (Cycle_executed/Cycle_total_planned)*100 
				print (Cycle_exe_per)		   
			except ZeroDivisionError:
				Cycle_exe_per = 0   
				print (Cycle_exe_per)
			#self.dict_exe_pass.update ({id:(str(proj_name),test_cycle_name,Cycle_Pass_Per,Cycle_exe_per,Cycle_executed,Cycle_total_planned)})				
			self.cur.execute("INSERT INTO TESTLINK_DEMO (PROJ_CYCLE_ID,PROJECTNAME,CYCLE,TOTAL_PLANNED,TOTAL_EXECUTED,PASS_PERCENTAGE,EXECUTION_PERCENTAGE) VALUES (%s,%s,%s,%s,%s,%s,%s)",(id,proj_name, test_cycle_name,Cycle_total_planned,Cycle_executed,Cycle_Pass_Per,Cycle_exe_per));
			self.conn.commit()
			total_planned = total_planned+ int(values[1+(count*iter)])
			total_notapp = total_notapp + int(values[10+(count*iter)])  
			total_pass = total_pass+ int(values[4+(count*iter)])
			total_fail = total_fail+ int(values[6+(count*iter)]) 
			iter += 1
			
		total_planned = total_planned - total_notapp	
		total_executed =  total_pass+total_fail 
		try:  
			Total_Pass_Per =  (total_pass/total_executed)*100
		except ZeroDivisionError:
			Total_Pass_Per = 0
		try:
			Test_exe_per = (total_executed/total_planned)*100  
		except ZeroDivisionError:
			Test_exe_per = 0
		print ("Test Case %Pass", Total_Pass_Per)
		print ("Test Case %Execution", Test_exe_per)
		test_cycle_name = "Overall"
		id = str(test_cycle_name)+'_'+str(proj_name)
		#self.dict_exe_pass.update ({id:(str(proj_name),test_cycle_name,Total_Pass_Per,Test_exe_per,total_executed,total_planned)})
		self.cur.execute("INSERT INTO TESTLINK_DEMO (PROJ_CYCLE_ID,PROJECTNAME,CYCLE,TOTAL_PLANNED,TOTAL_EXECUTED,PASS_PERCENTAGE,EXECUTION_PERCENTAGE) VALUES (%s,%s,%s,%s,%s,%s,%s)",(id,proj_name, test_cycle_name,total_planned,total_executed,Total_Pass_Per,Test_exe_per ));
		self.conn.commit()

	def calc_loc_overall_results(self,proj,start_date,end_date):
		payload = {
			'Login': "marathon",
			'Password': "xyz1234"
		}
		print("proj in loc calc is "+str(proj))
		total_lines = 0
		#start_date =self.format_date(start_date)
		#end_date =self.format_date(end_date)
		with requests.Session() as s:
			p = s.post('https://alm.xyz.com', data=payload)
			r = s.get('https://alm.xyz.com/crucible/search/'+str(proj)+'?ql=select%20revisions%20from%20dir%20%22%2F%22%20where%20date%20in%20%5B'+str(start_date)+'T00%3A00%3A00.000Z%2C%20'+str(end_date)+'T00%3A00%3A00.000Z)%20exclude%20merges%20return%20date%2C%20linesAdded&csv=true')
		lines = (r.text).replace("\r","").split("\n")
		for each in range(2,len(lines)-1):
			total_lines += int(lines[each].split(",")[1])
		return total_lines
		
	def format_date(self,strng_date):
		dd = strng_date[:2]
		mm = strng_date[2:4]
		yyyy = strng_date[4:]
		act_date = str(dd)+"-"+str(mm)+"-"+str(yyyy)
		req_date = str(yyyy)+"-"+str(mm)+"-"+str(dd)
		return req_date

	def total_defects (self,projectKey,startDate):
		total_defect =0 
		total_project_defect = 0
		startat = 0
		jira_options = {
                'server': 'https://alm.xyz.com/jira'}
		jira = JIRA(basic_auth=("marathon", "xyz1234"), options= jira_options)
		now = dt.date.today()
		endDate = str(now)
		while (startat<2000):
			project_temp = "project ="+str(projectKey)+" AND issuetype = Defect AND status in (Resolved, Closed, Submitted, WIP, Await, Postponed, Assigned, InBuild) AND resolution in (Unresolved, Fixed, \"Cannot Reproduce\", Incomplete, Done, \"Functions As Designed\", \"No Action Planned\", \"User Error\", \"Won't Do\", Resolved, \"Resolution Supplied\", \"Internal Only\", \"Enhancement Accepted\", \"Corrected Future Release\", \"Other Vendor Error\", \"Configuration Error\", \"Customer Request\", \"Design Intent\", \"Decided Not To Fix\", \"Resolve by characteristic\", \"Enhancement Request\", \"No action Planned Error\", Other, Declined, Unresloved) AND created >="+ startDate+ " AND created <="+endDate+" ORDER BY priority DESC, updated DESC"
			print (project_temp)
			issues_in_proj = jira.search_issues(project_temp,startAt=startat,maxResults=5000)
			total_defect = str(issues_in_proj).count("key")
			total_project_defect = total_project_defect+total_defect
			print (total_defect)
			print (total_project_defect)
			if (total_defect==1000):
				startat = 1001
			elif (total_defect<1000):
				break
		return total_defect 
	def open_defects (self,projectKey,startDate):
		total_defect =0 
		total_project_defect = 0
		startat = 0

		jira_options = {
            'server': 'https://alm.xyz.com/jira'}
		jira = JIRA(basic_auth=("marathon", "xyz1234"), options= jira_options)
		now = dt.date.today()
		endDate = str(now)
		while (startat<2000):
			project_temp = "project ="+str(projectKey)+" AND issuetype = Defect AND status in (Submitted, WIP, Await, Postponed, Assigned, InBuild) AND Severity in (Critical, High, Major) AND created >= "+ startDate+ " AND created <="+endDate+" ORDER BY priority DESC, updated DESC"
			print (project_temp)
			issues_in_proj = jira.search_issues(project_temp,startAt=startat,maxResults=5000)
			total_open_defect = str(issues_in_proj).count("key")
			total_project_defect_prj = total_project_defect+total_open_defect
			print (total_open_defect)
			print (total_project_defect_prj)
			if (total_open_defect==1000):
				startat = 1001
			elif (total_open_defect<1000):
				break
		return total_open_defect 



Obj_jira_query = jira_query()
Obj_jira_query.main()
