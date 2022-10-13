import requests
from bs4 import BeautifulSoup
import urllib.request as req
import models.mysql_connect as mysql_connect
def fitx_update():  
    url ="https://www.taifex.com.tw/cht/3/futDailyMarketReport" # 
    stcok_data = requests.get(url)

    soup = BeautifulSoup(stcok_data.text,"html.parser") #將網頁資料以html.parser
    txs = soup.find_all('td',class_="12bk")
    date = str(soup.select('div > table > tbody > tr:nth-child(2) > td > p') )
    date = date[-15:-5]
    if date != []:
        connection = mysql_connect.link_mysql()
        cursor = connection.cursor()
        sql="select * from fitx where date_time = '{}'".format(date)
        cursor.execute(sql)
        data = cursor.fetchall()
        if len(data) == 0 :
            print("開始更新fitx")
            sql="insert into fitx(date_time ,open ,hight ,low ,cloes ,amplitude)\
                values('{}',{},{},{},{},{})".format(date,int(txs[2].string),int(txs[3].string),int(txs[4].string),int(txs[5].string),int(txs[3].string)-int(txs[4].string))
            cursor.execute(sql)
            connection.commit()
            #tx.append({'日期':i.string[3:],'開盤價':int(txs[2].string),'最高價':int(txs[3].string),'最低價':int(txs[4].string),'收盤價':int(txs[5].string)})
        else:
            print("今日已更新")
    else:
        print('今日沒開盤')

    connection.close()
    print("fitx更新完畢")