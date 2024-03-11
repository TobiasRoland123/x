from bottle import  delete
import x


######################################  
@delete("/users/<id>")
def _(id):

    try:

        db = x.db()
        q = db.execute("DELETE FROM users WHERE user_pk = ?",(id,))

        db.commit()
        return f"""
        <template mix-target="#user_{id}" mix-replace>
            user {id} has been deleted
         </template>
        """
        #return "user deleted"
    except Exception as ex:
        print(ex) 
        return "error"
    finally:
        if "db" in locals(): db.close()

    