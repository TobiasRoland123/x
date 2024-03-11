from bottle import post, request
import x
import uuid
import datetime


@post("/users")
def _():
    try:

        user_name = request.forms.get("user_name")
        user_email = request.forms.get("user_email")
        user_password = request.forms.get("user_password")
        user_pk = uuid.uuid4().hex
        user_updated_at = datetime.datetime.now()
        db = x.db()
        q = db.execute("INSERT INTO users VALUES(?, ?, ?,?,?)",(user_pk, user_name, user_updated_at, user_email, user_password))
        db.commit()
        return f"""
        <template mix-target="#users" mix-top>
        {user_name}
        </template>
        """

        
    
    except Exception as ex:
        print("error")
        print(ex)
        return f"{ex}"
    finally:
        if db in locals(): db.close()