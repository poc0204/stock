import config
import models.login_db
@config.app.route("/login_db",methods=['Post'])
def login_db():
    print("login")
    models.login_db.login_db_get()
    return 123
