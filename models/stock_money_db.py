import models.mysql_connect as mysql_connect
from bs4 import BeautifulSoup
import urllib.request as req

def stock_money():
    json_data = []
    connection = mysql_connect.link_mysql()
    cursor = connection.cursor()
    sql = "select * from stock_money "
    cursor.execute(sql)
    stock_money = cursor.fetchall()
    for j in range(len(stock_money)):
        date={
            'name':stock_money[j][1],
            'today':stock_money[j][2],
            'yestday':stock_money[j][3],
            'vs':stock_money[j][4]
        }
    
        json_data.append(date)
        
    url="https://histock.tw/%E5%8F%B0%E8%82%A1%E5%A4%A7%E7%9B%A4"

    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data=response.read()
    soup=BeautifulSoup(data)

    tws_value=soup.select('div.info-right > div > ul.priceinfo > li > span > span' )  

    tws_date={
        'tws':tws_value[0].string,
        'up_or_down':tws_value[1].string,
        'up_or_down_point':tws_value[2].string,
        'tws_money':tws_value[3].string,
    }

    return {"data":json_data,'tws':tws_date}
