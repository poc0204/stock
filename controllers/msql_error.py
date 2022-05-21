import config
import models.update_all as update_all
import models.mysql_connect as mysql_connect
@config.app.route("/mysql")
def mysql_error():
    return config.render_template("mysql_error.html")