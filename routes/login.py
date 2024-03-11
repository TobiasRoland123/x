from bottle import post, response, request
import x


@post("/login")
def _():
    try:
        # TODO: validate the email and password
        # validate password
        x.validate_user_email()
        x.validate_user_password()

        

        # TODO: Connect to the db and check that the email and password are correct
        # db.exceute(SELECT * FROM users WHERE user_email = ? AND user_password = ?, (email, password))
        user_email = request.forms.get("user_email")
        user_password = request.forms.get("user_password")

        print(f"#############{user_email}################")
        print(f"#############{user_password}################")
        db = x.db()
        q = db.execute("SELECT * FROM users WHERE user_email = ? AND user_password = ?", (user_email, user_password))
        user = q.fetchall()
        # print(f"########################{user}#############################")

        if not user:
            return """
            <template mix-target="#error" mix-replace>
                <div id="error">Invalid email or password</div>
            </template>
            """

        response.set_cookie("name", user[0]['user_name'], secret="my_secret", httponly=True)
        return """
        <template mix-redirect="/admin">
        </template>
        """
    except Exception as ex:
        print(ex)
        # print(type(ex))
        # print(ex.args[0])
        # print(ex.args[1]) # user_password xxxxx  user_email xxxxx

        if "user_password" in ex.args[1]:
            return """
            <template mix-target="#error" mix-replace>
                <div id="error">User password invalid</div>
            </template>
            """
        
        if "user_email" in ex.args[1]:
            return """
            <template mix-target="#error" mix-replace>
                <div id="error">User email invalid</div>
            </template>
            """
        
        return """
        <template mix-target="#error" mix-replace>
            <div id="error">System under maintainance</div>
        </template>
        """

    finally:
        pass





