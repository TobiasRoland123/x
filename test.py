import sqlite3


# connect to database 
db = sqlite3.connect("company.db")

# Runs SELECT command in database
sql = db.execute("SELECT * FROM users")

# get all users from database
users = sql.fetchall()


print(users)

