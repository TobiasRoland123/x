import time
from bottle import post, request
import x
import uuid
from sqlite3 import IntegrityError
import bcrypt


@post ("/signup")
def _():
    try:
        #Valitede
        user_email = x.validate_user_email()
        user_id = uuid.uuid4().hex
        user_name = x.validate_user_name()
        user_updated_at = 0

        salt = bcrypt.gensalt()
        user_password = x.validate_user_password().encode()
        hashed_password  = bcrypt.hashpw(user_password, salt)
        
        user_created_at = int(time.time())
        db = x.db()
        q = db.execute('INSERT INTO users VALUES(?, ?, ?, ?, ?,?)', (user_id, user_name, user_updated_at, user_email, hashed_password, user_created_at))

        db.commit()
        

        return """
                <template mix-target="#message">
                <div id="message">
                    User Created
                </div>
                </template>
                """
    
    except Exception as ex:
        print(ex)
        
    

 
        if "users.user_email" in str(ex):
            return """
                <template mix-target="#message">
                <div id="message">
                    Email already taken
                </div>
                </template>
                """

        if "user_email" in str(ex):
            return """
            <template mix-target="#message">
            <div id="message">
                Email invalid
            </div>
            </template>
            """
        
        if "user_password" in str(ex):
            print("password error:",ex)
            return """
            <template mix-target="#message">
            <div id="message">
                password problem
            </div>
            </template>
            """
    finally:
        if "db" in locals(): db.close()