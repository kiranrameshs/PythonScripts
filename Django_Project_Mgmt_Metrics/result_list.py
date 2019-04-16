import psycopg2
from datetime import datetime, timedelta
import datetime as dt
import time
import subprocess
from subprocess import Popen, PIPE
import os
import sys
class result_list:
	def __init__(self):
		print("Result list")

	def get_table_data(self,bu,proj,board,tag1,tag2):
		print("Inputs received are ",str(bu),str(proj),str(board),str(tag1),str(tag2))
		conn = psycopg2.connect(database = "sentestdb", user = "postgres", password = "root123", host = "127.0.0.1", port = "5432")
		cur = conn.cursor()
		print ("Connected to database successfully")
		testlink_data = self.get_testlink_data(proj)
		print ("testlink_data",str(testlink_data))
		final_defect = self.get_rdd_ordd(proj)
		td = final_defect['td']
		od = final_defect['od']
		print("td is "+str(td)+"  od is "+str(od))
		dict_proj_rep = {}
		dict_proj_rep['TENBPLUS'] = 'lte_enb'
		dict_proj_rep['DUB'] = ''
		dict_proj_rep['EDBH'] = ''
		dict_proj_rep['CAEL'] = 'fe-2k'
		dict_proj_rep['LMCOUSEIM'] = 'lmco_uesim'
		dict_proj_rep['VZDTG'] = 'vz_intel_master'
		dict_proj_rep['VZDE'] = 'vz_intel_master'
		if str(proj) in dict_proj_rep.keys() and dict_proj_rep[proj] !="":
			print("Match found for proj "+str(proj) )
			path = dict_proj_rep[proj] 
		if board == "":
			print("board input not available, displaying for project level")
			cur.execute("SELECT STARTDATE from marathon_DEMO WHERE PROJKEY = (%s)  ORDER BY STARTDATE ASC;",(proj,))
			rows = cur.fetchall()
			start_date = self.format_date(rows)
			print(str(start_date))
			#cur.execute("SELECT ENDDATE from marathon_DEMO WHERE PROJKEY = (%s) ORDER BY ENDDATE DESC;",(proj,))
			#rows = cur.fetchall()
			conn.close()
			#end_date = self.format_date(rows)
			now = dt.date.today()
			end_date = str(now)
			print("end date is ",end_date)
			if str(tag1) and str (tag2) != "":
				kloc = self.get_tag (path,str(tag1),str(tag2))
				print (kloc)
			else:
				kloc = self.get_loc_total (start_date,end_date,proj,"")

		else:
			print("board input available, displaying for board level")
			cur.execute("SELECT STARTDATE from marathon_DEMO WHERE PROJKEY = (%s) AND BOARDNAME = (%s) ORDER BY STARTDATE ASC;",(proj,board,))
			rows = cur.fetchall()
			start_date = self.format_date(rows)
			print(str(start_date))
			#cur.execute("SELECT ENDDATE from marathon_DEMO WHERE PROJKEY = (%s) AND BOARDNAME = (%s) ORDER BY STARTDATE DESC;",(proj,board,))
			#rows = cur.fetchall()
			conn.close()
			#end_date = self.format_date(rows)
			now = dt.date.today()
			end_date = str(now)
			print("end date is ",end_date)
			if str(tag1) and str (tag2) != "":
				kloc = self.get_tag ("lmco_uesim",str(tag1),str(tag2))
				print (kloc)
			else:
				kloc = self.get_loc_total (start_date,end_date,proj,board)
		str_kloc  = round(float(kloc),3)
		try:
			rdd = float(td)/float(kloc)
		except ZeroDivisionError:
			rdd = 0
		try: 
			ordd = float(od)/float(kloc)
		
		except ZeroDivisionError:
			ordd = 0
		return {'bu':bu,'proj':proj,'board':board,'start_date':start_date,'end_date':end_date,'str_kloc':str_kloc,'rdd':round(float(rdd),2),'ordd':round(float(ordd),2),'td':td,'od':od,'testlink':testlink_data}
		
	def format_date(self,rows):
			s= str(rows[0]).split("(")[2].split(")")[0].split(", ")
			#print(str(s))
			#print(str(len(s)))
			date = ""
			for each in range(len(s)):
					if len(s[each])<2:
							date += ('0'+s[each])
					else:
							date += (s[each])
							print("No change in formatting")
			#print(str(date))
			start_date_time_frmt = datetime(year=int(date[0:4]), month=int(date[4:6]), day=int(date[6:8]))
			start_date_frmt = str(start_date_time_frmt)[0:10]
			return (str(start_date_frmt))

	def get_loc_total (self,sd,ed,proj,board):
			total_loc = 0
			conn = psycopg2.connect(database = "testdb", user = "postgres", password = "root123", host = "127.0.0.1", port = "5432")
			cur = conn.cursor()
			print ("Connected to database successfully")
			if board == "":
				cur.execute("SELECT LOC FROM marathon_DEMO WHERE STARTDATE BETWEEN (%s) AND (%s) AND PROJKEY = (%s);", (sd,ed,proj,))
			else:
				cur.execute("SELECT LOC FROM marathon_DEMO WHERE STARTDATE BETWEEN (%s) AND (%s) AND PROJKEY = (%s) AND BOARDNAME = (%s);", (sd,ed,proj,board,))
			rows = cur.fetchall()
			conn.close()
			for each in range(len(rows)):
					total_loc += int (str(rows[each]).replace("\'","").replace(",","").replace(")","").split("(")[1])
			print("total loc is "+str(total_loc))
			return (int(total_loc)/1000)
	
	def get_testlink_data(self,proj):
		conn = psycopg2.connect(database = "testdb", user = "postgres", password = "root123", host = "127.0.0.1", port = "5432")
		cur = conn.cursor()
		print ("Connected to database successfully under testlink data")
		cur.execute("SELECT CYCLE FROM TESTLINK_DEMO WHERE PROJECTNAME = (%s);", (proj,))
		rows = cur.fetchall()
		print("rows are "+str(rows))
		cycle_list = []
		final_testlink_report = {}
		for each in rows:
			eachcycle_str = str(each).split(",")[0]
			eachcycle = eachcycle_str.replace("\'","").replace("(","")
			#print("eachcycle is "+str(eachcycle))
			cycle_list.append(eachcycle)
		for eachcycle_id in cycle_list:
			cur.execute("SELECT PROJ_CYCLE_ID,CYCLE,TOTAL_PLANNED,TOTAL_EXECUTED,PASS_PERCENTAGE,EXECUTION_PERCENTAGE FROM TESTLINK_DEMO WHERE PROJECTNAME = (%s) AND CYCLE = (%s);", (proj,eachcycle_id,))
			rows = cur.fetchall()
			#print("each cycle list is "+str(rows))
			for eachline in rows:
				proj_cycle_id = str(eachline).split(",")[0].replace("\'","").replace("(","")
				cycle = str(eachline).split(",")[1].replace("\'","").replace("(","")
				total_planned = str(eachline).split(",")[2].replace("\'","").replace("(","")
				total_executed = str(eachline).split(",")[3].replace("\'","").replace("(","")
				pass_percentage = str(eachline).split(",")[4].replace("\'","").replace("(","")
				execution_percentage = str(eachline).split(",")[5].replace("\'","").replace("(","").replace(")","")
				print("proj_cycle_id   "+str(proj_cycle_id)+"cycle  "+str(cycle)+"total_planned"+str(total_planned)+"total_executed"+str(total_executed)+"pass_percentage  "+str(pass_percentage)+"execution_percentage  "+str(execution_percentage))
				final_testlink_report.update({proj_cycle_id:(cycle,total_planned,total_executed,round(float(pass_percentage),2),round(float(execution_percentage),2))})
		return final_testlink_report
		conn.close()

	def get_rdd_ordd(self,proj):
		final_dd = {}
		conn = psycopg2.connect(database = "sentestdb", user = "postgres", password = "root123", host = "127.0.0.1", port = "5432")
		cur = conn.cursor()
		print ("Connected to database successfully")
		cur.execute("SELECT TOTAL_DEFECTS,OPEN_DEFECTS FROM DEFECTDENSITY_DEMO WHERE PROJKEY = (%s);", (proj,))
		rows = cur.fetchall()
		conn.close()
		total_defects = str(rows).split(",")[0].replace("\'","").replace("[","").replace("(","")
		open_defects  = str(rows).split(",")[1].replace("\'","").replace("]","").replace(")","")
		print("total_defects is "+str(total_defects))
		print("open_defects is "+str(open_defects))
		final_dd.update({'td':int(total_defects),'od':int(open_defects)})
		print(str(final_dd))
		return final_dd

	def get_tag (self,path,tag_name1,tag_name2):
		print("Getting loc from tag values")
		command = "git diff --stat "+tag_name1+" "+tag_name2+" -- '*.c' '*.h'"
		wrk_dir = '/root/git/'+path
		p = Popen([command], cwd = wrk_dir ,stdout=PIPE, stderr=PIPE, stdin=PIPE, shell=True)
		output = p.stdout.read()
		loc = str (output).split (",")
		length = len(loc)
		if (length > 1):
			loc = loc [length-2].split (" ")
			loc = loc [1]
			kloc = int(loc)/1000
			return kloc
		else:
			return (0)

