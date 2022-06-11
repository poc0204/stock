import models.mysql_connect as mysql_connect
from bs4 import BeautifulSoup
import urllib.request as req
import config
import datetime
import asyncio
import time
import aiohttp

def stock_money_update():
    connection = mysql_connect.link_mysql()
    cursor = connection.cursor()  
    # 更新資金流向
    url="https://www.moneydj.com/Z/ZB/ZBA/ZBA.djhtm"

    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data=response.read()
    soup=BeautifulSoup(data)

    group_name=soup.select('table > tr > td.t4t1' )
    group_number=soup.select('table > tr > td.t3n1' )

    sql = "select * from stock_money"
    cursor.execute(sql)
    stock_money_data = cursor.fetchall()
    update_or_number = []
    update_or_name = []
    #print(stock_money_data[i][2])
    start = time.time()
    try:
        for i in range(30):
            if group_name[i].string =='電子':
                continue
            update_or_number.append(group_number[i].string)
            update_or_name.append(group_name[i].string)
        for i in range(len(stock_money_data)):
            if (float(stock_money_data[i][2]) == float(update_or_number[i][0:-1])) == False:
                for i in range(len(stock_money_data)):
                    sql = " UPDATE stock_money SET Transaction_proportion={},Transaction_proportion_yesterday={},Transaction_proportion_vs={} where group_name = '{}' ".format(float(update_or_number[i][0:-1]),float(stock_money_data[i][2]),float(update_or_number[i][0:-1])-float(stock_money_data[i][2]),update_or_name[i])
                    cursor.execute(sql) 
                    connection.commit()
                    data = {
                        'updata':'yes'
                    }
                return config.jsonify({'data':data}) ,200
        data = {
                'updata':'no'
        }
        return config.jsonify({'data':data}) ,200
    except:
        data = {
                'updata':'error'
        }
        return config.jsonify({'data':data}) ,200
    finally:
        end = time.time()
        print(f'花費時間:{end - start}')

def group_price():
    connection = mysql_connect.link_mysql()
    cursor = connection.cursor()
    date = datetime.date.today()
    async def tws():
        url="https://histock.tw/%E5%8F%B0%E8%82%A1%E5%A4%A7%E7%9B%A4"
        request=req.Request(url,headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
        })
        
        with req.urlopen(request) as response:
            data=response.read()
        soup=BeautifulSoup(data)

        tws_value=soup.select('div.info-right > div > ul.priceinfo > li > span > span' )
        data={
            'group_price':tws_value[0].string,
            'up_or_down':tws_value[1].string,
            'up_or_down_point':tws_value[2].string,
            'group_money':tws_value[3].string,
            'group_name':'加權'
        }
        sql = " UPDATE group_price set group_price='{}' , \
        up_or_down='{}',up_or_down_point='{}' ,group_money='{}'  ,\
        date_time='{}' where group_name = '{}'".format(data['group_price'],data['up_or_down'],data['up_or_down_point'],data['group_money'],date,'加權')
        cursor.execute(sql)
        connection.commit()

    url="https://histock.tw/twclass/A0"
    all_title=[
                '11','12','13','14','15','16',
                '19','20','21','22','23','32','33',
                '34','36','03','18','24','25','26',
                '27','28','29','30','31','37','38']
    tasks=[]    
    async def getHtml(url, client):  
            async with client.get(url) as resp:
                resp.get_encoding()
                await resp.text()
                soup=BeautifulSoup( await resp.text())
                group_value=soup.select('div.info-right > div > ul.priceinfo > li > span > span' ) 
                group_name=soup.select('div.info-left > div > h3' )
                group_date={
                    'group_price':group_value[0].string,
                    'up_or_down':group_value[1].string,
                    'up_or_down_point':group_value[2].string,
                    'group_money':group_value[3].string,
                    'group_name':group_name[0].string.lstrip()
                }
                sql = " UPDATE group_price set group_price='{}' , \
                up_or_down='{}',up_or_down_point='{}' ,group_money='{}'  ,\
                date_time='{}' where group_name = '{}'".format(group_date['group_price'],group_date['up_or_down'],group_date['up_or_down_point'],group_date['group_money'],date,group_date['group_name'][2:])
                cursor.execute(sql)
                connection.commit()

    async def main(url, turn):
        async with aiohttp.ClientSession() as client:
            for i in range(len(turn)):
                url = "https://histock.tw/twclass/A0"+all_title[i]
                tasks.append(asyncio.create_task(getHtml(url, client)))
            asyncio.create_task(tws())
            await asyncio.wait(tasks)


    start = time.time()
    try:

        loop = asyncio.new_event_loop()
        loop.run_until_complete(main(url, all_title))  # 完成事件循环，直到最后一个任务结束
        data = {
                    'updata':'yes'
                }
        return config.jsonify({'data':data}) ,200
   
    except:
        data = {
                'updata':'error'
        }
        return config.jsonify({'data':data}) ,200
    finally:
        end = time.time()
        print(f'花費時間:{end - start}')