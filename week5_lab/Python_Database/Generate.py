import pymysql

db = pymysql.connect("localhost","root","","test")  # open database connection

cursor = db.cursor()  # prepare a cursor object using cursor() method

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")  # delete existing employee table

sql = """CREATE TABLE IF NOT EXISTS EMPLOYEE(  # create a new employee table with 5 attribute
      FIRST_NAME CHAR(20) NOT NULL,
      LAST_NAME CHAR(20),
      AGE INT,
      SEX CHAR(1),
      INCOME FLOAT)"""

cursor.execute(sql)

sql = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES('%s','%s','%s','%s','%s')"  # Insert 4 employee info to the table
record = [('Mary', 'Smith', 19, 'F', 1800),
('Gary', 'Lee', 21, 'M', 2000),
('Becky', 'Bucked', 21, 'F', 2800),
('Flora', 'Aniston', 17, 'F', 2300)]

try:
    # Execute the SQL command
    for each in record:
        cursor.execute(sql % each)
        # Commit your changes in the database.
        db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

sql = "SELECT COUNT(*) FROM EMPLOYEE WHERE SEX = '%s'" % ('F')  # select all female 

cursor.execute(sql)

results = cursor.fetchall()

print('There are ' + str(results[0][0]) + ' Female employees')  # Output the result

sql = "SELECT * FROM EMPLOYEE WHERE AGE < '%d'" % (20)  # select all employee age under 20

cursor.execute(sql)

results = cursor.fetchall()

print("All employees whose age is under 20:")  # Output the result
for row in results:
	first_name = row[0]
	last_name = row[1]
	age = row[2]
	sex = row[3]
	income = row[4]
	print("fname = %s, lname = %s, age = %d, sex = %s, income = %d" % (first_name, last_name, age, sex, income))

sql = "UPDATE EMPLOYEE SET INCOME = 2000 WHERE INCOME < '%s'" % (2000)  # Update income for whose income is less than 2000

try:
    # Execute the SQL command
    cursor.execute(sql)

    # Commit your changes in the database
    db.commit()

except:
    # Rollback in case there is any error
    db.rollback()


sql = "SELECT * FROM EMPLOYEE WHERE INCOME >= '%d'" % (2000)  # select all employee whose income is greater or equal to 2000

cursor.execute(sql)

results = cursor.fetchall()

print("All employees whose income is greater or equal to 2000:")
for row in results:
	first_name = row[0]
	last_name = row[1]
	age = row[2]
	sex = row[3]
	income = row[4]
	print("fname = %s, lname = %s, age = %d, sex = %s, income = %d" % (first_name, last_name, age, sex, income))

sql = "DELETE FROM EMPLOYEE WHERE AGE < '%d'" % (18)  # delete all employee whose age is less than 18

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

sql = "SELECT * FROM EMPLOYEE" # select all employee

cursor.execute(sql)

results = cursor.fetchall()

print("All employees Information:")
for row in results:
	first_name = row[0]
	last_name = row[1]
	age = row[2]
	sex = row[3]
	income = row[4]
	print("fname = %s, lname = %s, age = %d, sex = %s, income = %d" % (first_name, last_name, age, sex, income))

# disconnect from server
db.close()