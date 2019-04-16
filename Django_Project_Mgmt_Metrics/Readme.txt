Install latest pip module by using command - 	python -m pip install --upgrade pip
Install rest framework by using the command 	pip install djangorestframework
Install Django by using command - 				pip install django
Install psycopg2 by using the command 			pip install psycopg2
Run the project from command prompt as python manage.py runserver
What does it do?
	Once linked to all projects on Jira, program calculates KLOC (Changes in Lines of Code) Open Release Defect Density and Release Defect Density for a given project, team, sprint, date range.
	Once linked to testcase data base, when same parameters are selected, calculates %pass, %fail, %inconc per test cycle
	Mail the entire report to recipients 
How does it do?
	Connects to Jira, updates all data onto db using sqlite3
	Once user selects a BU, project, team, sprint/ date range, it displays
	 KLOC (Total lines added/Modified) and open defect density, release defect density, %pass, %fail, %inconc per test cycle