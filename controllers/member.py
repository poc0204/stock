
import config
import models.member_db as member_db
import json , re

@config.app.route("/login")
def login():
    return config.render_template("login.html")

@config.app.route("/api/login",methods=['PATCH'])
def api_login():
    data = json.loads(config.request.data)
    member_email = data['email']
    member_password = data['password']
    data = member_db.login(member_email,member_password)
    return config.jsonify({'data':data}) ,200 

@config.app.route("/api/member")
def api_user():
    token = config.session.get('token')
    data = member_db.member_check(token)
    return config.jsonify({'data':data}) ,200 
        
@config.app.route("/signup")
def signup():
    return config.render_template("signup.html")

@config.app.route("/api/signup",methods=['POST'])
def api_signup():
    data = json.loads(config.request.data)
    member_email = data['email']
    member_password = data['password']
    member_name = data['name']
    data = member_db.signup(member_name,member_email,member_password)
    return config.jsonify({'data':data}) ,200

@config.app.route("/member_stock")
def member():
    token = config.session.get('token')
    data = member_db.member_check(token)
    if(data['member']==False):
        return config.render_template("login.html")
    else:
        return config.render_template("member_stock.html")

@config.app.route("/api/member_stock_data")
def api_member_stock_data():
    member_stock_data = member_db.member_stock_data()
    return config.jsonify({'data':member_stock_data}) ,200

@config.app.route("/api/add_stock/<stock_id>")
def api_add_stock_data(stock_id):
    token = config.session.get('token')
    data = member_db.member_check(token)
    if(data['member']==False):
        return config.render_template("login.html")
    else:
        member_db.add_stock_data(stock_id)
        return  config.redirect(config.request.referrer)

@config.app.route("/api/delete_stock/<stock_id>")
def delete_stock(stock_id):
    member_db.delete_stock(stock_id)
    return config.render_template("member_stock.html")
@config.app.route("/signout")
def signout():
    config.session.clear()
    return config.redirect("/")