import config
import controllers.index , controllers.msql_error , controllers.update , controllers.stock_money , controllers.member
import controllers.gruop_name , controllers.stock_name 
import os
from dotenv import load_dotenv
load_dotenv()

config.app.config['SECRET_KEY'] = os.getenv('jwt_member')
config.app.config['JSON_AS_ASCII'] = False
#域名
host='0.0.0.0'
#port 號
port=3000
if __name__ == '__main__':
    # 啟動flask
    config.app.run(host=host, port=port)
    