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
if form.getvalue('eventSelect'):
    selectedEvent = form.getvalue('eventSelect')
else:
    selectedEvent = None

# prepare a cursor() method
cursor = db.cursor()

if selectedEvent != "Any":
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
             """ % str(selectedEvent)  # Select all event's name
else:
    sql = """SELECT * FROM player ORDER BY ranking"""


try:
    # Execute the SQL command
    cursor.execute(sql)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    amount = len(results)
    cursor.execute("SELECT * FROM area")
    areas = dict(cursor.fetchall())
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
    <h1 class="text-center">%s result(s) found</h1>
    </header>
    <div class="row">
    <div class="col">
    <table class="table table-striped">
    <thead>
    <tr>
    <th scope="col">Name</th>
    <th scope="col">ID</th>
    <th scope="col">World Rank</th>
    <th scope="col">Ranking Points</th>
    <th scope="col">Country/Area</th>
    </tr>
    </thead>
    <tbody>''' % str(amount))
    for player in results:
        name = player[1]
        player_id = player[0]
        world_rank = player[2]
        ranking_point = player[3]
        area = areas[str(player[4])]
        print("""<tr><td>%s</td>
        <td>%d</td>
        <td>%d</td>
        <td>%d</td>
        <td>%s</td>
        </tr>""" % (name, int(player_id), int(world_rank), int(ranking_point), area))

    print('''
    </tbody>
    </table>
    </div>
    </div>
    </div>
    </body>
    </html>
        ''')
except:
    print("Error: unable to fetch data")

# disconnect from server
db.close()

