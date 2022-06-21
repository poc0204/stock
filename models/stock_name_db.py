import models.mysql_connect as mysql_connect
from FinMind.data import DataLoader
import os
import datetime
from dotenv import load_dotenv
load_dotenv()

def stock_id(stock):
    connection = mysql_connect.link_mysql()
    cursor = connection.cursor()
    sql = "select * from stock_price where stock_id ='{}'".format(stock)
    cursor.execute(sql)
    stock_name = cursor.fetchall()
    close = float(stock_name[0][6])
    spread = float(stock_name[0][9])
    Trading_Volume = str(stock_name[0][7])

    if (len(Trading_Volume[:-3]) > 3):
        Trading_Volume = format(int(Trading_Volume[:-3]),',')
    else:
        try:
            Trading_Volume = Trading_Volume[:-3]
        except:
            Trading_Volume = Trading_Volume
    data={
        'stock_id':stock_name[0][1],
        'stock_neam':stock_name[0][2],
        'close':'%.2f'%close,
        'spread':'%.2f'%spread,
        'spread_point':'{:.2%}'.format(spread/close),
        'Trading_Volume':Trading_Volume
    }

    stock_data =[]
    Trading_turnover_color=''
    end_date = datetime.date.today()
    start_date = datetime.date.today() - datetime.timedelta(days=365)
    stock_number =stock
    api = DataLoader()
    api.login_by_token(api_token=os.getenv('api_token_finmind_y'))
    df = api.taiwan_stock_daily(
                stock_id=stock_number,
                start_date=start_date,
                end_date=end_date
            )
    for i in range(len(df)-1):
        j = i+1
        if df['close'][i] > df['close'][j]:
            Trading_turnover_color = 'rgba(0, 150, 136, 0.8)' 
        else:
            Trading_turnover_color = 'rgba(255,82,82, 0.8)' 
        alldata ={
            'time':df['date'][j],
            'open':df['open'][j],
            'high':df['max'][j],
            'low':df['min'][j],
            'close':df['close'][j],
            'Trading_turnover':float(df['Trading_turnover'][i]),
            'color':Trading_turnover_color
        }
        
 
        stock_data.append(alldata)
    return {'stock_data':stock_data,"data":data}