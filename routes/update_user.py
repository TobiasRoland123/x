from bottle import put, request
import x

@put("/users/<id>")
def _(id):
    try:
        new_user_name = request.forms.get("user_name")

        db = x.db()
        q = db.execute("UPDATE users SET user_name = {new_user_name} WHERE user_pk = ? ",(id))
        db.commit()
    except Exception as ex:
        print("error")
        print(ex)
        return f"{ex}"
    finally:
        if db in locals(): db.close()