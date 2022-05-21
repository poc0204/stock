import imp
import config
import models.stock_money_db as stock_money_db
@config.app.route("/api/stock_money")
def api_stock_money():
    return config.jsonify({'data':stock_money_db.stock_money()})