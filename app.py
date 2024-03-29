
from bottle import default_app, error, get , static_file, template, redirect, response




######################################
@get("/app.css")
def _():
    return static_file("app.css", ".")


######################################
@get("/mixhtml.js")
def _():
    return static_file("mixhtml.js", ".")


######################################
@get("/favicon.ico")
def _():
    return static_file("favicon.ico", ".")


#VIEW ROUTES    
######################################
import routes.get_users
import routes.get_items
import routes.delete_user

import routes.get_item_id
import routes.create_item
import routes.delete_item

import routes.create_user
import routes.update_user

import routes.login
import routes.admin


######################################
import api_html.signup


######################################
@get("/logout")
def _():
  response.add_header("Cache-Control", "no-cache, no-store, must-revalidate")
  response.add_header("Pragma", "no-cache")
  response.add_header("Expires", 0)    
  response.delete_cookie("name")
  response.status = 303
  response.set_header("Location", "/login")
  return    


######################################
@get("/") # 127.0.0.1
def _():
    return template("index.html")


######################################
@error(404)
def _(error):
    return "page not found :("


######################################

@get("/signup")
def _():
    return template("signup.html")


######################################

@get("/login")
def _():
    return template("login.html")










    
   






######################################  
@get("/users/<id>")
def _(id):
    title = "user " + id
    return template("user",
                     id=id, 
                     title=title)


######################################
app = default_app()