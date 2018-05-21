#!C:\Program Files (x86)\python\Python.exe
# Import modules for CGI handling
import cgi
import cgitb

# Import modules for Database
import pymysql

# Open database connection
db = pymysql.connect("172.16.199.70", "l630003054", "SDW2db", "l630003054")

# prepare a cursor() method
cursor = db.cursor()

sql = "SELECT event_name FROM event"  # Select all event's name

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
    <title>Search | ITTF Official Website</title>
    <link href="https://cdn.bootcss.com/bootstrap/4.1.0/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
    <div class="container">
    <header class="my-5">
    <h1 class="text-center">Make your Search</h1>
    </header>
    <form action="/cgi-bin/result.py" method="post" target="_blank">
    <div class="row">
    <div class="col-4"><h3 class="text-center">Event</h3></div>
    <div class="col-8">
    <div class="form-group">
    <select class="form-control" id="eventSelect" name="eventSelect">
    <option>Any</option>''')
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
    </form>
    </div>
    </body>
    </html>
    ''')
except:
    print("Error: unable to fetch data")

# disconnect from server
db.close()

