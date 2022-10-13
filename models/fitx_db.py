import models.mysql_connect as mysql_connect
import pandas as pd
import datetime
def fixt_amplitude_data():
    connection = mysql_connect.link_mysql()
    cursor = connection.cursor()
    sql="select amplitude from fitx limit 20"
    cursor.execute(sql)
    connection.commit()
    data = cursor.fetchall()
    connection.close()
    df = pd.DataFrame(data)
    maxs20=int(df.max()) # 最大波動 場外全壘打
    min20=int(df.min())# 最小波動 一壘
    mean20 = int(df.mean()) # 20平均振幅 三擂
    less_mean20 = 0
    less_mean20_time = 0
    more_mean20 = 0
    more_mean20_time = 0
    
    for i in range(len(data)):
        if data[i][0] >mean20 :
            more_mean20=more_mean20+data[i][0]
            more_mean20_time=more_mean20_time+1
        else:
            less_mean20=less_mean20+data[i][0]
            less_mean20_time=less_mean20_time+1
    third = int(more_mean20/more_mean20_time)
    two = int(less_mean20/less_mean20_time)
    fitx = {
        '一壘':min20,
        '二壘':two,
        '三壘':mean20,
        '全壘打':third,
        '場外全壘打':maxs20,
        'date':str(datetime.date.today())
        }  
    return fitx