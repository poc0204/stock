import models.mysql_connect as mysql_connect
import jwt 
from datetime import datetime
import os
import config
import pymysql
from dotenv import load_dotenv
load_dotenv()

def signup(member_name,member_email,member_password):
    connection = mysql_connect.link_mysql()
    cursor = connection.cursor()
    sql="select mail from member_data where mail = '{}' ".format(member_email)
    cursor.execute(sql)
    member_email_data = cursor.fetchall()
    if(member_email_data == ()):
        try:
            salt = os.getenv('jwt_member')

            payload={
            'password':member_password
            }
            
            password =  jwt.encode(payload,salt)
            print(password.decode("utf-8"))
            create_time =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sql="INSERT INTO member_data (name, mail, password, date_time) VALUES('{}','{}','{}','{}')".format(member_name,member_email,password,create_time)
            cursor.execute(sql)
            connection.commit()

            sql="INSERT INTO member_stock_1 (member) VALUES('{}')".format(member_email)
            cursor.execute(sql)
            connection.commit()
            data={
                'success':True,
                'massage':'註冊成功'
            }
            return data
        except pymysql.Error as e:
            print(e.args[0],e.args[1])
            data={
                'success':False,
                'massage':'註冊失敗'
            }
            return data
    else:
        data={
            'success': False,
            'massage':'帳號重複'
        }
        return data

def login(member_email,member_password):  
    connection = mysql_connect.link_mysql()
    cursor = connection.cursor()
    sql="select name , mail ,password from member_data where mail = '{}' ".format(member_email)
    cursor.execute(sql)
    member_data = cursor.fetchall()
    
    if(member_data == ()):
        data = {
            'success': False,
            'massage':'此信箱尚未註冊'  
        }
        return data
    else:    
        salt = os.getenv('jwt_member')
        mysql_password = jwt.decode(member_data[0][2],salt,algorithms='HS256')
        if(mysql_password['password'] == member_password):
            headers = {
                'typ':'jwt',
                'alg':'HS256'
            }
            payload = {
                'e-mail':member_email,
                'member':member_data[0][0]
            }
            token = jwt.encode(payload=payload,key=salt,algorithm='HS256',headers=headers)
            config.session['token'] = token
            data = {
                'success': True,
                'massage':'登入成功',  
                'member':member_email
            }
            return data
        else:
            data = {
                'success': False,
                'massage':'密碼錯誤'  
            }
            return data

def member_check(token):
    salt = os.getenv('jwt_member')
    try:
        member= jwt.decode(token,salt,algorithms='HS256')
        data = {
            'member':True,
            'member_name': member['member']
        }
        return data
    except:
        data = {
            'member':False
        }
        return data


def member_stock_data():
    connection = mysql_connect.link_mysql()
    cursor = connection.cursor()
    member_email = get_member_mail()
    sql="select * from member_stock_1 where member ='{}'".format(member_email)
    cursor.execute(sql)
    member_stock = cursor.fetchall()
    stock_data=[]
    j = 1
    for i in range(len(member_stock[0])-2):
        i = i+1
        j = j + 1
        if member_stock[0][j] != None:
            sql = "select * from stock_price where stock_id ='{}'".format(member_stock[0][j])
            cursor.execute(sql)
            member_stock_data = cursor.fetchall()
            Trading_Volume = str(member_stock_data[0][7])

            if (len(Trading_Volume[:-3]) > 3):
                Trading_Volume = format(int(Trading_Volume[:-3]),',')
            else:
                try:
                    Trading_Volume = Trading_Volume[:-3]
                except:
                    Trading_Volume = Trading_Volume
            data = {
                    'group_name':member_stock_data[0][8],
                    'stock_id':member_stock_data[0][1],
                    'stock_name':member_stock_data[0][2],
                    'open':'%.2f'%member_stock_data[0][3],
                    'low':'%.2f'%member_stock_data[0][4],
                    'hight':'%.2f'%member_stock_data[0][5],
                    'close':'%.2f'%member_stock_data[0][6],
                    'Trading_Volume':Trading_Volume,
                    'spread':'%.2f'%member_stock_data[0][9],
                    'spread_point':'{:.2%}'.format(member_stock_data[0][9]/(member_stock_data[0][6])),
                    'td_stock_yestday':'%.2f'%(member_stock_data[0][6]+member_stock_data[0][9])
                }
            stock_data.append(data)     
    return stock_data
    
def delete_stock(stock_id):
    connection = mysql_connect.link_mysql()
    cursor = connection.cursor()
    member_email = get_member_mail()
    for i in range(10):
        i = i+1
        sql = "update member_stock_1 set stock_{}=null where stock_{} ='{}' ".format(i,i,stock_id,member_email)
        cursor.execute(sql)
        connection.commit()

def add_stock_data(stock_id):
    connection = mysql_connect.link_mysql()
    cursor = connection.cursor()
    member_email = get_member_mail()
    sql="select * from member_stock_1 where member = '{}'".format(member_email)
    cursor.execute(sql)
    data = cursor.fetchall()
    j = 2
    for i in range(len(data[0])-2):
        i = i +1
        if data[0][j] == int(stock_id):
            stock_input = {
                'massage':True
            }
            return stock_input
        stock_input = {
                'massage':False
            }    
        j= j+1
    j = 2
    if stock_input['massage'] != True:
        for i in range(len(data[0])-2):
            i = i +1
            if data[0][j] == None:
                sql = "UPDATE member_stock_1 SET stock_{} ='{}' where member = '{}'".format(i,stock_id,member_email)
                cursor.execute(sql)
                connection.commit()
                stock_input = {
                    'massage':'success'
                }
                return stock_input
            j= j+1
        
def get_member_mail():
    token = config.session.get('token')
    salt = os.getenv('jwt_member')
    member_email = jwt.decode(token,salt,algorithms='HS256')
    return member_email['e-mail']








 