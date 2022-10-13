import config
import models.update_tse as tse
import models.update_fixt as fixt
import models.update_all as stock
import controllers.index , controllers.msql_error , controllers.update , controllers.stock_money , controllers.member
import controllers.gruop_name , controllers.stock_name , controllers.fitx
import os
from flask_apscheduler import APScheduler
import requests as req
import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime,timezone,timedelta
from dotenv import load_dotenv

load_dotenv()

config.app.config['SECRET_KEY'] = os.getenv('jwt_member')
config.app.config['JSON_AS_ASCII'] = False
socketio = config.SocketIO(config.app)
#域名
host='0.0.0.0'
#port 號
port=3000


aps = APScheduler()


class Config(object):
    JOBS = [
        # {
        #     'id': 'update_stock_money',                # 一個標識
        #     'func': '__main__:update_stock_money',     # 指定執行的函式 
        #     'trigger': 'cron',       # 指定 定時任務的型別
        #     'day_of_week': 'mon-fri',
        #     'hour': '17',
        #     'minute': '15',   
        #     'second':  '00'               # 執行的間隔時間
        # },
        # {
        #     'id': 'update_group_price',                # 一個標識
        #     'func': '__main__:update_group_price',     # 指定執行的函式 
        #     'trigger': 'cron',       # 指定 定時任務的型別
        #     'day_of_week': 'mon-fri',
        #     'hour': '17',
        #     'minute': '20',   
        #     'second':  '00'                 # 執行的間隔時間         # 執行的間隔時間
        # },
        # {
        #     'id': 'update_stock_price_fist',                # 一個標識
        #     'func': '__main__:update_stock_price_fist',     # 指定執行的函式 
        #     'trigger': 'cron',       # 指定 定時任務的型別
        #     'day_of_week': 'mon-fri',
        #     'hour': '17',
        #     'minute': '30',   
        #     'second':  '00'  
        # },
        # {
        #     'id': 'update_stock_price_second',                # 一個標識
        #     'func': '__main__:update_stock_price_second',     # 指定執行的函式 
        #     'trigger': 'cron',       # 指定 定時任務的型別
        #     'day_of_week': 'mon-fri',
        #     'hour': '10',
        #     'minute': '05',   
        #     'second':  '00'  
        # },
        # {   # 新增資金流向表
        #     'id': 'update_tse',                # 一個標識
        #     'func': '__main__:update_tse',     # 指定執行的函式 
        #     'trigger': 'cron',       # 指定 定時任務的型別
        #     'day_of_week': 'mon-fri',
        #     'hour': '17',
        #     'minute': '00',   
        #     'second':  '00'               # 執行的間隔時間
        # },
        # {   # 新增日振幅
        #     'id': 'update_fixt',                # 一個標識
        #     'func': '__main__:update_fixt',     # 指定執行的函式 
        #     'trigger': 'cron',       # 指定 定時任務的型別
        #     'day_of_week': 'mon-fri',
        #     'hour': '17',
        #     'minute': '05',   
        #     'second':  '00'               # 執行的間隔時間
        # },

        # {   # sokcetio
        #     'id': 'fitx_data',                # 一個標識
        #     'func': '__main__:fitx_data',     # 指定執行的函式 
        #     'trigger': 'cron',       # 指定 定時任務的型別
        #     'day_of_week': 'mon-fri',
        #     'hour': '08',
        #     'minute': '45',   
        #     'second':  '01'                       # 執行的間隔時間   
        # },
        {   # sokcetio_test
            'id': 'fitx_test',                # 一個標識
            'func': '__main__:fitx_test',     # 指定執行的函式 
            'trigger': 'interval', 
            'seconds': 2      
        },
    ]
    SCHEDULER_API_ENABLED = True
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'

# def update_stock_money():                          # 執行的定時任務的函式
#     #data = update_all.stock_money()
#     url="https://pocworks.store/updata/stock_money"
#     requests.get(url)
  
# def update_group_price():   
#     #data = update_all.group_price()
#     url="https://pocworks.store/updata/group_price"
#     requests.get(url)
   

# def update_stock_price_fist():   
#     #data = update_all.group_price()
#     url="https://pocworks.store/updata/stock_price"
#     requests.get(url)
    

# def update_stock_price_second():   
#     #data = update_all.group_price()
#     url="https://pocworks.store/updata/stock_price"
#     requests.get(url)

def update_tse():
    tse.tse_update()

def update_fixt():
    fixt.fitx_update()

@config.app.route("/fitx")
def fitxs():
    return config.render_template("fitx.html", async_mode=socketio.async_mode)

def fitx_test():
    url="https://pocworks.store/api/fitx"
    config.requests.get(url)

def fitx_data():
    dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
    dt2 = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
    now_time = dt2.strftime("%H:%M:%S")
    while now_time < '13:44:59':
        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt2 = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
        now_time = dt2.strftime("%H:%M:%S")
        url="https://pocworks.store/api/fitx"
        config.requests.get(url)

    

@config.app.route("/api/fitx")
def api_fitx():
    url=os.environ.get('api_fitx')
    payload = {"MarketType":"0",
            "SymbolType":"F",
            "KindID":"1",
            "CID":"TXF",
            "ExpireMonth":"",
            "RowSize":"全部",
            "PageNo":"",
            "SortColumn":"",
            "AscDesc":"A"}
    day_time = ''
    day_value = ''
    res =req.post(url, json = payload)
    data = res.json()
    df = pd.DataFrame(data['RtData']['QuoteList'])
    # df= df[["DispCName", "Status", "CBidPrice1", "CBidSize1", "CAskPrice1", "CAskSize1", "CLastPrice", "CDiff", "CAmpRate", "CTotalVolume", "COpenPrice", "CHighPrice", "CLowPrice", "CRefPrice", "CTime"]]
    # df.columns = ['商品', '狀態', '買進', '買量', '賣出', '賣量', '成交價', '漲跌', '振幅%', '成交量', '開盤', '最高', '最低', '參考價', '時間']
    hight = int(df.iat[1,11].replace('.00',""))
    low = int(df.iat[1,12].replace('.00',""))
    #day_time= df.iat[1,14]
    # if day_value != df.iat[1,9]:
    #     print(hight-low)
    #     print(df.loc[[1],['時間','買進','賣出','成交價','成交量']])
    #day_value =  df.iat[1,9]
    OpenPrice = int(df.iat[1,10].replace('.00',""))
    LastPrice = int(df.iat[1,7].replace('.00',""))
    hight_low = hight-low
    now_hight_low = str(OpenPrice-LastPrice).replace('-',"")
    socketio.emit('api_fitx', {'LastPrice':LastPrice,'hight_low':hight_low,'OpenPrice':OpenPrice,'now_hight_low':now_hight_low,'hight':hight,'low':low})
    return config.jsonify({"response": "ok"})


if __name__ == '__main__':
    config.app.config.from_object(Config())
    scheduler = APScheduler(BackgroundScheduler(timezone="Asia/Shanghai"))
    scheduler.init_app(config.app)
    scheduler.start()
    # 啟動flask
    #config.app.run(host=host, port=port)
    socketio.run(config.app, debug=True,host=host, port=port ,use_reloader=False)