import sqlite3 as sql

connection = sql.connect("dabaseMovies.db")

pointer = connection.cursor()
pointer.execute("CREATE TABLE IF NOT EXISTS MOVIES( NAME TEXT, ACTOR TEXT, ACTRESS TEXT,DIRECTOR_NAME TEXT, YEAR INTEGER )")
pointer.execute("INSERT INTO MOVIES VALUES('Ranna','Sudeep','Rachitha ram','Nanda kishore',2017)")
pointer.execute("INSERT INTO MOVIES VALUES('Kotigobba','Sudeep','Nithya menon','sury',2015)")
pointer.execute("INSERT INTO MOVIES VALUES('Yuvarathna','Puneeth rajkumar','Aarushi','Prem',2021)")
pointer.execute("INSERT INTO MOVIES VALUES('Kotigobba: 3','Sudeep','Sebastian','Nanda kishore',2021)")
pointer.execute("INSERT INTO MOVIES VALUES('Gajakesari','Yash','Amulya','Rakshitha',2017)")

# Printing all the elements of the database 
print("************************Everything in the database************************")
allMovies = pointer.execute("SELECT * FROM MOVIES").fetchall()
for i in allMovies:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
  print("============================================================================================")

# In this query, we are printing only the details from the db where Tom Holland is the lead actor
print("************************Actor Query************************")
actorQuery = pointer.execute("SELECT * FROM MOVIES WHERE ACTOR = 'Tom Holland'").fetchall()
for i in actorQuery:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
  print("============================================================================================")
