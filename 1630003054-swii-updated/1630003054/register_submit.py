#!C:\Program Files (x86)\python\Python.exe
# Import modules for CGI handling
import cgi
import cgitb

# Import modules for Database
import pymysql

# Open database connection
db = pymysql.connect("172.16.199.70", "l630003054", "SDW2db", "l630003054")

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
if form.getvalue('registerEventPID'):
    registerPID = form.getvalue('registerEventPID')
else:
    registerPID = None

if form.getvalue('registerEventSelect'):
    registerEvent = form.getvalue('registerEventSelect')
else:
    registerEvent = None

# prepare a cursor() method
cursor = db.cursor()

cursor.execute("SELECT * FROM event")
events = dict(cursor.fetchall)

try:
    cursor.execute("""
    SELECT * FROM player WHERE player_id = %d
    """ % int(registerPID))
    user = list(cursor.fetchall())
except:
    user = None


try:
    cursor.execute("""
    SELECT capacity FROM event WHERE event_name='%s'
    """ % str(registerEvent))
    capacity = cursor.fetchall()[0][0]
except:
    capacity = None

sql = """SELECT *
             FROM player
             WHERE player_id in
             (SELECT player_id
             FROM registration
             WHERE event_id =
             (SELECT event_id
             FROM event
             WHERE event_name='%s')) AND player_id = %d
             ORDER BY ranking
             """ % (str(registerEvent), int(registerPID))

try:
    cursor.execute(sql)
    user_registered = len(cursor.fetchall())
except:
    user_registered = 0

if user_registered > 0:
    is_register = 1
else:
    is_register = 0

sql = """SELECT *
             FROM player
             WHERE player_id in
             (SELECT player_id
             FROM registration
             WHERE event_id =
             (SELECT event_id
             FROM event
             WHERE event_name='%s'))
             ORDER BY ranking
             """ % str(registerEvent)

try:
    cursor.execute(sql)
    registered = len(cursor.fetchall())
except:
    registered = None

if capacity > registered:
    is_full = 0
else:
    is_full = 1


if len(user) == 0:
    print("Content-type:text/html\r\n\r\n")
    print()
    print('''
            <!DOCTYPE html>
            <html>
            <head>
            <title>Result | ITTF Official Website</title>
            <link href="https://cdn.bootcss.com/bootstrap/4.1.0/css/bootstrap.min.css" rel="stylesheet">
            </head>
            <body>
            <div class="container">
            <header class="my-5">
            </header>
            <div class="row">
            <div class="col">
            <div class="card">
            <div class="card-body">
            <h1 class="card-title text-center">ERROR: The player ID is invalid.</h1>
            </div>
            </div>
            </div>
            </div>
            </div>
            </body>
            </html>
            ''')
elif is_register == 1:
    print("Content-type:text/html\r\n\r\n")
    print()
    print('''
    <!DOCTYPE html>
    <html>
    <head>
    <title>Result | ITTF Official Website</title>
    <link href="https://cdn.bootcss.com/bootstrap/4.1.0/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
    <div class="container">
    <header class="my-5">
    </header>
    <div class="row">
    <div class="col">
    <div class="card">
    <div class="card-body">
    <h1 class="card-title text-center">ERROR: The player is previously registered to the event.</h1>
    </div>
    </div>
    </div>
    </div>
    </div>
    </body>
    </html>
    ''')
elif is_full:
    print("Content-type:text/html\r\n\r\n")
    print()
    print('''
    <!DOCTYPE html>
    <html>
    <head>
    <title>Result | ITTF Official Website</title>
    <link href="https://cdn.bootcss.com/bootstrap/4.1.0/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
    <div class="container">
    <header class="my-5">
    </header>
    <div class="row">
    <div class="col">
    <div class="card">
    <div class="card-body">
    <h1 class="card-title text-center">ERROR: The total number of registered players exceed the maximum capacity.</h1>
    </div>
    </div>
    </div>
    </div>
    </div>
    </body>
    </html>
    ''')
else:
    try:
        sql = '''INSERT INTO registration (event_id, player_id) VALUES(%d, registerPID)''' % int(events[registerEvent])

        try:
            # Execute the SQL command
            cursor.execute(sql)
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        # Execute the SQL command
        cursor.execute("""SELECT player_name FROM player WHERE player_id = %d""" % registerPID)

        # Fetch all the rows in a list of lists.
        player_name = cursor.fetchall()[0]
        print("Content-type:text/html\r\n\r\n")
        print()
        print('''
        <!DOCTYPE html>
        <html>
        <head>
        <title>Result | ITTF Official Website</title>
        <link href="https://cdn.bootcss.com/bootstrap/4.1.0/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
        <div class="container">
        <header class="my-5">
        </header>
        <div class="row">
        <div class="col">
        <div class="card">
        <div class="card-body">
        <h5 class="card-title">Register Result</h5>
        <p class="card-text">Your registration have been successfully submit. Please double check the information.</p>
        </div>
        <ul class="list-group list-group-flush">
        <li class="list-group-item">Name: %s</li>
        <li class="list-group-item">ID: %d</li>
        <li class="list-group-item">Registered Event: %s</li>
        </ul>
        </div>
        </div>
        </div>
        </div>
        </body>
        </html>
         ''' % (player_name ,registerEvent, registerEvent))

    except:
        print("Content-type:text/html\r\n\r\n")
        print()
        print("Error: unable to finish registration")

# disconnect from server
db.close()

