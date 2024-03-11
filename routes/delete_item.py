from bottle import delete, response, get
import x


############################
@delete("/items/<id>")
def _(id):
    try:
        db = x.db()
        q = db.execute("DELETE FROM items WHERE item_id = ?", (id,))
        db.commit()
        response.status = 303
        return f"""
        <template mix-target="#item_{id}" mix-replace>
        <div class="bg-red-500" mix-ttl="2000">
        item deleted
        </div>
        </template >
        """
        
    except Exception as ex:
        print(ex)

    finally:
         if "db" in locals(): db.close()