import models.mysql_connect as mysql_connect
def gruop_name_db(gruop):
    connection = mysql_connect.link_mysql()
    cursor = connection.cursor()
    sql = "select * from stock_price where group_name ='{}'".format(gruop)
    cursor.execute(sql)
    gruop_name = cursor.fetchall()

    all_data =[]
    for i in range(len(gruop_name)):
        Trading_Volume = str(gruop_name[i][7])

        if (len(Trading_Volume[:-3]) > 3):
           Trading_Volume = format(int(Trading_Volume[:-3]),',')
        else:
            try:
                Trading_Volume = Trading_Volume[:-3]
            except:
                Trading_Volume = Trading_Volume
        
        if gruop_name[i][3] == 0:
    
            data = {
                'group_name':gruop_name[i][8],
                'stock_id':gruop_name[i][1],
                'stock_name':gruop_name[i][2],
                'open':'0.00',
                'low':'0.00',
                'hight':'0.00',
                'close':'0.00',
                'Trading_Volume':'0.00',
                'spread':'0.00',
                'spread_point':'0.00%',
                'td_stock_yestday':'0.00',
            }
            all_data.append(data)
        else:
            data = {
                'group_name':gruop_name[i][8],
                'stock_id':gruop_name[i][1],
                'stock_name':gruop_name[i][2],
                'open':'%.2f'%gruop_name[i][3],
                'low':'%.2f'%gruop_name[i][4],
                'hight':'%.2f'%gruop_name[i][5],
                'close':'%.2f'%gruop_name[i][6],
                'Trading_Volume':Trading_Volume,
                'spread':'%.2f'%gruop_name[i][9],
                'spread_point':'{:.2%}'.format(gruop_name[i][9]/(gruop_name[i][6])),
                'td_stock_yestday':'%.2f'%(gruop_name[i][6]+gruop_name[i][9])
            }
            all_data.append(data)

    return  all_data

def group_price(group):
    connection = mysql_connect.link_mysql()
    cursor = connection.cursor()
    sql = "select * from group_price where group_name ='{}'".format(group)
    cursor.execute(sql)
    gruop_data = cursor.fetchall()
    data={
        'group_price':gruop_data[0][2],
        'up_or_down_point':gruop_data[0][3],
        'up_or_down':gruop_data[0][4],
        'group_money':gruop_data[0][5],

    }
    return  data