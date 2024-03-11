from bottle import get, template

######################################  
@get("/items/<id>")
def _(id):
    try:
        title = "Item " + id
        return template("item",
                     id=id, 
                     title=title)
    except Exception as ex:
        print("error")
        print(ex)
    finally:
        pass