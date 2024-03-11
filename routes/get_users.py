
from bottle import get , template
import x


######################################  
@get("/users")
def _():
    try:
        db = x.db()
        sql = db.execute("SELECT * FROM users")    # runs SELECT function in database
        users = sql.fetchall() # gets all users from database
        return template("users", users=users)
    except Exception as ex:
        print(ex)
        return "error"
    finally:
        if "db" in locals(): db.close()
        print("oooooooooooooooooooooooooooooooo")
    
   