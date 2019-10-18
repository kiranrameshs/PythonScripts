import sys
import os
import time
import configparser
import subprocess
import datetime

configfile = "config.ini"
config = configparser.ConfigParser()
config.readfp(open(configfile))
board_ip = config.get('BOARD', 'IP')
username = config.get('BOARD', 'Username')
password = config.get('BOARD', 'Password')
print("Board IP is "+str(board_ip))
print("Username is "+str(username))
print("Password is "+str(password))
start_time = datetime.datetime.now().replace(microsecond=0)
print ("Started execution at "+str(start_time))
while True:
	time.sleep(3)
	info = subprocess.STARTUPINFO()
	info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
	info.wShowWindow = subprocess.SW_HIDE
	output = subprocess.Popen(['ping', '-n', '1', '-w', '500', board_ip], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]
	if "Destination host unreachable" in output.decode('utf-8'):
		print(board_ip+" is Unreachable so exiting automation")
	elif "Request timed out" in output.decode('utf-8'):
		print(board_ip+" is Request timed out so exiting automation")
	else:
		break
stoptime = datetime.datetime.now().replace(microsecond=0)
print ("Board Pingable at "+str(stoptime))
total_time_for_board_up = stoptime - start_time
print("Time taken by board to reboot is"+str (total_time_for_board_up))
expect_l1_bringup_file = "bringup_l1.txt"
cmd_bringupl1 = 'expect '+expect_l1_bringup_file+" "+board_ip+' '+username+' '+password
print("cmd_bringupl1 is "+cmd_bringupl1)
os.system("start \"Bring up eNB\" cmd call /C "+cmd_bringupl1)
time.sleep(10)
print ("L1 bring up done, Going to bring up eNB ")

expect_enb_bringup_file = "bringup_enb.txt"
cmd_bringupenb = 'expect '+expect_enb_bringup_file+" "+board_ip+' '+username+' '+password
print("cmd_bringupenb is "+cmd_bringupenb)
os.system("start \"Bring up eNB\" cmd call /C "+cmd_bringupenb)
time.sleep(10)
print ("Bring up eNB done")
