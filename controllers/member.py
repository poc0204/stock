import config
import models.member_db as member_db
import json 
import os
import boto3
import base64

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
def member_stock():
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

@config.app.route("/member/<member_name>")
def member(member_name):  
    return config.render_template("member.html")

@config.app.route("/member_put_image", methods=["post"])
def member_put_image():
    token = config.session.get('token')
    data = member_db.member_check(token)
    e_mail= data['e-mail']
    image_data = config.request.files.get("image_data")
    data = member_db.member_put_image_db(image_data,e_mail)
    return config.jsonify({'data':data}) ,200

@config.app.route("/member_get_image")
def member_get_image():
    token = config.session.get('token')
    data = member_db.member_check(token)
    data = member_db.member_get_image_db(data['e-mail'])

    return config.jsonify({'data':data}) ,200

@config.app.route("/check_member_password",methods=["post"])
def check_member_password():
    token = config.session.get('token')
    member_email = member_db.member_check(token)
    data = json.loads(config.request.data)
    member_password_old = data['password_old']
    member_password_new= data['password_new']
    data = member_db.login(member_email['e-mail'],member_password_old)
    if data['success']==True:
        data = member_db.member_update_password(member_email['e-mail'],member_password_new)
        config.session.clear()
        return config.jsonify({'data':data}) ,200
    else :
        return config.jsonify({'data':data}) ,200