
import traceback
from dbutils.pooled_db import PooledDB
import pymysql
import os
from dotenv import load_dotenv
load_dotenv()
import controllers.msql_error
import config
def link_mysql():
    try:
        POOL = PooledDB(
        creator=pymysql,  # 使用連結資料庫的模組
        maxconnections=6,  # 連線池允許的最大連線數，0和None表示不限制連線數
        mincached=2,  # 初始化時，連結池中至少建立的空閒的連結，0表示不建立
        maxcached=5,  # 連結池中最多閒置的連結，0和None不限制
        maxshared=3,  # 連結池中最多共享的連結數量，0和None表示全部共享。PS: 無用，因為pymysql和MySQLdb等模組的 threadsafety都為1，所有值無論設定為多少，_maxcached永遠為0，所以永遠是所有連結都共享。
        blocking=True,  # 連線池中如果沒有可用連線後，是否阻塞等待。True，等待；False，不等待然後報錯
        maxusage=None,  # 一個連結最多被重複使用的次數，None表示無限制
        setsession=[],  # 開始會話前執行的命令列表。如：["set datestyle to ...", "set time zone ..."]
        ping=0,
        # ping MySQL服務端，檢查是否服務可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
        host=os.environ.get('aws_rds_host'),
        port=3306,
        user=os.environ.get('aws_rds_user'),
        password=os.environ.get('aws_rds_password'),
        database=os.environ.get('database'),
        charset='utf8',
        )
        conn = POOL.connection()

    except Exception as e:
            traceback.print_exc(e)
            data ={
            'error':True
            }
            print("error")
            
            return data
            
    else:
	    return conn
 