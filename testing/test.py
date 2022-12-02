import mysql.connector

mydb = mysql.connector.connect(
    host="mysql.wpi.edu",
  user="ctang5",
  password="CT@ng5",
  database="mams_siso",
  )
sql = mydb.cursor()

command = f"INSERT INTO daily VALUES (return_id('Charles', 'Tang'), CURRENT_DATE(), CURRENT_TIME());"
sql.execute(command) 
mydb.commit()

command = f"SELECT * FROM daily"
sql.execute(command)
myresult = sql.fetchall()
print(myresult)
mydb.close()
