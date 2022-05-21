import config
import controllers.index , controllers.msql_error , controllers.update , controllers.stock_money , controllers.member ,controllers.login
import controllers.signup , controllers.gruop_name
#域名
host='0.0.0.0'
#port 號
port=3000
if __name__ == '__main__':
    # 啟動flask
    config.app.run(host=host, port=port)
    