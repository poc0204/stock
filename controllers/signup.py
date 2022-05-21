import config
import models.signup_db
@config.app.route("/signup_db",methods=['Post'])
def signup_db():
    print("signup")
    models.signup_db.signup_db_get()
    return 123
