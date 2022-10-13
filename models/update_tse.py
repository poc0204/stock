from FinMind.data import DataLoader
import requests, json
import math
import pandas as pd
import models.mysql_connect as mysql_connect
import datacompy
import pymysql

def tse_update():
    connection = mysql_connect.link_mysql()
    cursor = connection.cursor()

    # 取得所有股票名稱
    api = DataLoader()
    df = api.taiwan_stock_info()

    # 取得所有股票當日成交明細
    url ="https://www.twse.com.tw/zh/exchangeReport/STOCK_DAY_ALL" 
    stcok_data = requests.get(url)
    stcok_data_text = json.loads(stcok_data.text)

    # 計算資金流向
    stock_class = []
    # 個股交易明細
    tse_stock=[]
    # 個股名稱
    tse_stock_name=[]

    # 個股資料整理
    for i in range(len(df)):
        if df['type'][i] == 'twse' and  df['industry_category'][i] !='電子工業' and  df['industry_category'][i] !='化學生技醫療' and  df['industry_category'][i] !='Index' \
            and  df['industry_category'][i] !='ETF' and df['industry_category'][i] !='受益證券' and  df['industry_category'][i] !='創新板股票' and df['industry_category'][i] !='存託憑證' and df['industry_category'][i] !='大盤' : 
            for j in range(len(stcok_data_text['data'])):
                if stcok_data_text['data'][j][0] == df['stock_id'][i]:
                    TradeVolume = stcok_data_text['data'][j][2].replace(",","")
                    TradeValuev = stcok_data_text['data'][j][3].replace(",","")
                    open = stcok_data_text['data'][j][4].replace(",","")
                    hight = stcok_data_text['data'][j][5].replace(",","")
                    low = stcok_data_text['data'][j][6].replace(",","")
                    close = stcok_data_text['data'][j][7].replace(",","")
                    point = stcok_data_text['data'][j][8].replace("X","")
                    # 計算資金流向
                    stock_class.append([df['stock_id'][i],df['stock_name'][i],df['industry_category'][i],math.ceil(int(TradeVolume)/1000),TradeValuev,stcok_data_text['data'][j][4],stcok_data_text['data'][j][5],stcok_data_text['data'][j][6],stcok_data_text['data'][j][7],stcok_data_text['data'][j][8],stcok_data_text['date']])
                    # 個股交易明細
                    tse_stock.append([df['stock_id'][i],df['stock_name'][i],df['industry_category'][i],math.ceil(int(TradeVolume)/1000),TradeValuev,open,hight,low,close,point,stcok_data_text['date']])
                    # 個股名稱
                    tse_stock_name.append([df['stock_id'][i],df['stock_name'][i]])
            
    # 抓兩大類別個股計算金額
    for i in range(len(df)):
        if df['industry_category'][i] =='電子工業' or  df['industry_category'][i] =='化學生技醫療' :
            for j in range(len(stcok_data_text['data'])):
                if stcok_data_text['data'][j][0] == df['stock_id'][i]:
                    TradeVolume = stcok_data_text['data'][j][2].replace(",","")
                    TradeValuev = stcok_data_text['data'][j][3].replace(",","")
                    stock_class.append([df['stock_id'][i],df['stock_name'][i],df['industry_category'][i],math.ceil(int(TradeVolume)/1000),TradeValuev,stcok_data_text['data'][j][4],stcok_data_text['data'][j][5],stcok_data_text['data'][j][6],stcok_data_text['data'][j][7],stcok_data_text['data'][j][8],stcok_data_text['date']])  


    # 判斷是已經更新過
    sql="select date_time from stock_class_money where date_time = '{}'".format(stcok_data_text['date'])
    cursor.execute(sql)
    check_stock_class_money_db = cursor.fetchall()

    if len(check_stock_class_money_db) == 0 :
        #print("開始更新資金流向")
        # 當日大盤成交金額
        url ="https://www.twse.com.tw/zh/exchangeReport/MI_INDEX"
        tse = requests.get(url)
        tse_text = json.loads(tse.text)
        tse_TradeValuev = int(tse_text['data7'][16][1].replace(',',''))
        sql="insert into stock_class_money(class_money_id ,TradeValuev ,date_point ,date_time) \
            values({},{},{},'{}')".format(31,tse_TradeValuev,100,stcok_data_text['date'])
        cursor.execute(sql)
        connection.commit()

        # 計算當日資金流向占比
        sql="select * from stock_class_name"
        cursor.execute(sql)
        stock_class_name_db = cursor.fetchall()

        # 資料整合
        stock_TradeValuev = 0
        for j in range(len(stock_class_name_db)):
            if stock_class_name_db[j][1] == 31 or stock_class_name_db[j][1] == 32 :
                continue
            for i in range(len(stock_class)): 
                if stock_class[i][2] == stock_class_name_db[j][2]:
                    stock_TradeValuev = stock_TradeValuev + int(stock_class[i][4])
            stock_class_point = (stock_TradeValuev/tse_TradeValuev)*100*100
            sql="insert into stock_class_money(class_money_id ,TradeValuev ,date_point ,date_time) \
                values({},{},{},'{}')".format(stock_class_name_db[j][1],stock_TradeValuev,math.ceil(stock_class_point)/100,stcok_data_text['date'])
            cursor.execute(sql)
            connection.commit()
            stock_TradeValuev = 0
    #     print("更新完畢資金流向")
    # else:
    #     print("已更新過")
 
    # 個股資料整理把類股名稱改成代號
    tse_stock = pd.DataFrame(tse_stock, columns=['id','name','class_name','TradeVolume','TradeValuev','open','hight','low','colse','point','date_time'])
    tse_stock['class_name'] = tse_stock['class_name'].replace([ '水泥工業' , '其他' , '食品工業' , '電器電纜' , '塑膠工業' , '建材營造' , '汽車工業' , '紡織纖維' ,\
    '貿易百貨' , '電子零組件業' , '電機機械' , '生技醫療業' , '化學工業' , '玻璃陶瓷' , '造紙工業' , '鋼鐵工業' , '橡膠工業' , '航運業' , '電腦及週邊設備業' ,\
    '半導體業' , '其他電子業' , '通信網路業' , '光電業' , '電子通路業' , '資訊服務業' , '油電燃氣業' , '觀光事業' , '金融保險' , '電子工業' , '化學生技醫療'],\
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])

    # 判斷是否今日有新的個股
    sql="select tse_stock_id , stock_name from tse_stock_name"
    cursor.execute(sql)
    connection.commit()
    tse_stock_name_db = cursor.fetchall()
    tse_stock_name_db = pd.DataFrame(tse_stock_name_db, columns=['id','name'])
    tse_stock_name= pd.DataFrame(tse_stock_name, columns=['id','name'])
    compare = datacompy.Compare(tse_stock_name_db, tse_stock_name, join_columns='id')
    compare = compare.df2_unq_rows
    if len(compare) > 0:
        compare.reset_index(inplace=True)
        for i in range(len(compare)):
            sql="insert into tse_stock_name(tse_stock_id ,stock_name ) value('{}','{}')".format(compare.at[i ,'id'],compare.at[i ,'name'])
            cursor.execute(sql)
            connection.commit()
    #print("今日沒有新增各股")

    # 判斷有無新增個股明細
    sql="select date_time from tse_stock_price where date_time = '{}' ".format(stcok_data_text['date'])
    cursor.execute(sql)
    connection.commit()
    tse_stock_prict_db = cursor.fetchall()

    if len(tse_stock_prict_db) == 0 :
        sql="SET AUTOCOMMIT = 0"
        cursor.execute(sql)
        sql="START TRANSACTION;"
        cursor.execute(sql)
        print("開始更新tse_stock")
        for i in range(len(tse_stock)):
            try:
                sql="insert into tse_stock_price(stock_id ,class_stcck_id, open, high, low, close, Trading_Volume, spread, date_time)\
                    value('{}',{},{},{},{},{},{},'{}','{}')".format(tse_stock.at[i ,'id'],tse_stock.at[i ,'class_name'],\
                        tse_stock.at[i ,'open'],tse_stock.at[i ,'hight'],tse_stock.at[i ,'low'],tse_stock.at[i ,'colse'],tse_stock.at[i ,'TradeVolume'],tse_stock.at[i ,'point'],tse_stock.at[i ,'date_time'])
                cursor.execute(sql)
            except pymysql.Error as error :
                #print(tse_stock.at[i ,'point'])
                connection.rollback()
        connection.commit()
        #print("tse_stock更新結束")

    
    connection.close()
    #print("tse全部更新結束")