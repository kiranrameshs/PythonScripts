Open the py file on IDLE or run it from command prompt.
What does it do?
	Tkinter UI to read/modify configurations, trigger and terminate automation
How does it do?
	Basic Tkinter UI to read default configurations from config.txt
	Any changes done on UI for configurations will be saved on runtime_config.txt
	Start Automation triggers Start_Automation.bat (Currently nothing)
	Stop Automation triggers Stop_Automation.bat (Currently kills python)
	After 15 seconds, every 10 seconds read log.txt and print logs in lower window
	If log.txt is not updated for 10 seconds, stop logging.