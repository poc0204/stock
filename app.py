import config
import controllers.index , controllers.msql_error , controllers.update , controllers.stock_money , controllers.member
import controllers.gruop_name , controllers.stock_name 
import os
from flask_apscheduler import APScheduler
import urllib.request as req
import datetime
from dotenv import load_dotenv
load_dotenv()

config.app.config['SECRET_KEY'] = os.getenv('jwt_member')
config.app.config['JSON_AS_ASCII'] = False
#域名
host='0.0.0.0'
#port 號
port=3000


aps = APScheduler()


class Config(object):
    JOBS = [
        {
            'id': 'update_stock_money',                # 一個標識
            'func': '__main__:update_stock_money',     # 指定執行的函式 
            'trigger': 'cron',       # 指定 定時任務的型別
            'day_of_week': 'mon-fri',
            'hour': '9',
            'minute': '00',   
            'second':  '00'               # 執行的間隔時間
        },
        {
            'id': 'update_group_price',                # 一個標識
            'func': '__main__:update_group_price',     # 指定執行的函式 
            'trigger': 'cron',       # 指定 定時任務的型別
            'day_of_week': 'mon-fri',
            'hour': '9',
            'minute': '05',   
            'second':  '00'                 # 執行的間隔時間         # 執行的間隔時間
        },
        {
            'id': 'update_stock_price_fist',                # 一個標識
            'func': '__main__:update_stock_price_fist',     # 指定執行的函式 
            'trigger': 'cron',       # 指定 定時任務的型別
            'day_of_week': 'mon-fri',
            'hour': '9',
            'minute': '10',   
            'second':  '00'  
        },
        {
            'id': 'update_stock_price_second',                # 一個標識
            'func': '__main__:update_stock_price_second',     # 指定執行的函式 
            'trigger': 'cron',       # 指定 定時任務的型別
            'day_of_week': 'mon-fri',
            'hour': '10',
            'minute': '10',   
            'second':  '00'  
        },
    ]
    SCHEDULER_API_ENABLED = True


def update_stock_money():                          # 執行的定時任務的函式
    #data = update_all.stock_money()
    url="https://pocworks.store/updata/stock_money"
    request=req.Request(url)
    print(datetime.datetime.now(),'update_stock_money')

def update_group_price():   
    #data = update_all.group_price()
    url="https://pocworks.store/updata/group_price"
    request=req.Request(url)
    print(datetime.datetime.now(),'update_group_price')

def update_stock_price_fist():   
    #data = update_all.group_price()
    url="https://pocworks.store/updata/stock_price"
    request=req.Request(url)
    print(datetime.datetime.now(),'update_stock_price_fist')

def update_stock_price_second():   
    #data = update_all.group_price()
    url="https://pocworks.store/updata/stock_price"
    request=req.Request(url)
    print(datetime.datetime.now(),'update_stock_price_second')

if __name__ == '__main__':
    config.app.config.from_object(Config())

    scheduler = APScheduler()
    scheduler.init_app(config.app)
    scheduler.start()
    # 啟動flask
    config.app.run(host=host, port=port)
    