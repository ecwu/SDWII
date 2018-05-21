#!C:\Program Files (x86)\python\Python.exe
# Import modules for CGI handling
import cgi
import cgitb

# Import modules for Database
import pymysql

# Import modules for Date Time handling
import datetime
import time

un_time = int(time.mktime(datetime.datetime.now().timetuple()))

# Open database connection
db = pymysql.connect("172.16.199.70", "l630003054", "SDW2db", "l630003054")

# prepare a cursor() method
cursor = db.cursor()

sql = "SELECT event_name FROM event WHERE unix_timestamp(registration_deadline) > %d" % un_time  # Select all event's name

try:
    # Execute the SQL command
    cursor.execute(sql)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()

    print("Content-type:text/html\r\n\r\n")
    print()
    print('''
    <!DOCTYPE html>
<html>
<head>
<title>Register | ITTF Official Website</title>
<link href="https://cdn.bootcss.com/bootstrap/4.1.0/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container">
<header class="my-5">
<h1 class="text-center">Register to an Event</h1>
</header>
<form action="/cgi-bin/register_submit.py" method="post">
<div class="row">
<div class="col-4"><h3 class="text-center">Player ID</h3></div>
<div class="col-8">
<div class="form-group">
<input type="text" class="form-control" id="registerEventPID" name="registerEventPID" placeholder="Enter Player ID">
</div>
</div>
</div>
<div class="row">
<div class="col-4"><h3 class="text-center">Event</h3></div>
<div class="col-8">
<div class="form-group">
<select class="form-control" id="registerEventSelect" name="registerEventSelect">
''')
    # create a drop down for every event
    for event in results:
        print("<option>%s</option>" % event)
    print('''
    </select>
</div>
</div>
</div>
<div class="row">
<div class="col">
<button type="submit" class="btn btn-primary btn-block">Submit</button>
</div>
</div>
</div>
</form>
</body>
</html>
    ''')
except:
    print("Error: unable to fetch data")

# disconnect from server
db.close()

