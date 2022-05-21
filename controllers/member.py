import config
@config.app.route("/login")
def login():
    return config.render_template("login.html")

@config.app.route("/signup")
def signup():
    return config.render_template("signup.html")

@config.app.route("/member")
def member_stock():
    return config.render_template("member.html")