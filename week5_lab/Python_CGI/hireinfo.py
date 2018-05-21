#!C:\Program Files (x86)\python\Python.exe

import cgi, cgitb 

form = cgi.FieldStorage() 

# Fetch data edit boxes
userName = form.getvalue('username')

# current skills
if form.getvalue('cs'):
   skills = form.getvalue('cs')
else:
   skills = "No current skills"


# city expected
if form.getvalue('citye'):
    city = form.getvalue('citye')
else:
    city = "No expected city"

# Position
if form.getvalue('po'):
    position = form.getvalue('po')
else:
    position = "No position"

# Recent Job
if form.getvalue('rj'):
    recentJob = form.getvalue('rj')
else:
    recentJob = "No recent Job"

# Work Experience
if form.getvalue('exp'):
    workExp = form.getvalue('exp')
else:
    workExp = ""


print ("Content-type:text/html")
print ()
print ("<html>")
print ("<head>")
print ("<meta charset=\"utf-8\">")
print ("<title>Submit result</title>")
print ("</head>")
print ("<body>")
print ("<h2>Username: %s</h2>" % userName)
print ("<h2>Current Skills: %s</h2>" % skills)
print ("<h2>City Expected: %s</h2>" % city)
print ("<h2>Position: %s</h2>" % position)
print ("<h2>Recent Jobs: %s</h2>" % recentJob) 
print ("<h2>Work Experience: %s</h2>" % workExp)
print ("</body>")
print ("</html>")
