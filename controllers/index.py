import config
@config.app.route("/")
def index():
    return config.render_template("index.html")

