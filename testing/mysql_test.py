import mysql.connector

def insert_daily_id(ID):
  mydb = mysql.connector.connect(
  host="mysql.wpi.edu",
  user="ctang5",
  password="CT@ng5",
  database="mams_siso",
  )
  sql = mydb.cursor()

  command = f"INSERT INTO daily VALUES ({ID}, CURRENT_DATE(), CURRENT_TIME());"
  sql.execute(command)
  mydb.commit()
  mydb.close()

def insert_daily_name(FName, LName):
  mydb = mysql.connector.connect(
  host="mysql.wpi.edu",
  user="ctang5",
  password="CT@ng5",
  database="mams_siso",
  )
  sql = mydb.cursor()
  command = f"INSERT INTO daily VALUES (return_id('{FName}', '{LName}'), CURRENT_DATE(), CURRENT_TIME());"
  sql.execute(command) 
  mydb.commit()
  mydb.close()


