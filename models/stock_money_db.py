import models.mysql_connect as mysql_connect
import asyncio
import time

def stock_money():
    connection = mysql_connect.link_mysql()
    cursor = connection.cursor()

    # url="https://histock.tw/%E5%8F%B0%E8%82%A1%E5%A4%A7%E7%9B%A4"

    # request=req.Request(url,headers={
    #     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    # })

    # with req.urlopen(request) as response:
    #     data=response.read()
    # soup=BeautifulSoup(data)

    # tws_value=soup.select('div.info-right > div > ul.priceinfo > li > span > span' )  
    async def tws():
        sql = "select * from group_price where group_name = '加權' "
        cursor.execute(sql)
        tws_value = cursor.fetchall()
        tws_date={
            'tws':tws_value[0][2],
            'up_or_down':tws_value[0][4],
            'up_or_down_point':tws_value[0][3],
            'tws_money':tws_value[0][5],
        }
        return tws_date

    async def group():
        json_data = []

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
        return json_data
    async def main():
        tws_date = await asyncio.gather(tws(), group())
        return tws_date  
    #start = time.perf_counter()          
    tws_date = asyncio.run(main())
    #elapsed = time.perf_counter() - start
    #print("執行時間：%f 秒" % elapsed)
    return {"data":tws_date[1],'tws':tws_date[0]}


def all_stock():
    connection = mysql_connect.link_mysql()
    cursor = connection.cursor()
    sql = "select stock_id , stock_name from stock_price"
    cursor.execute(sql)
    all_stock = cursor.fetchall()
    json_data=[]
    for j in range(len(all_stock)):
            date={
                'stock_id':all_stock[j][0],
                'stock_name':all_stock[j][1],
            }
            json_data.append(date)
    return {"data":json_data}
