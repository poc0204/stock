
import config
import models.stock_money_db as stock_money_db
@config.app.route("/api/stock_money")
def api_stock_money():
    return config.jsonify({'data':stock_money_db.stock_money()})


@config.app.route("/api/all_stock")
def api_all_stock():
    return config.jsonify({'data':stock_money_db.all_stock()})


@config.app.route("/api/search_stock")
def api_search_stock():
    return config.jsonify({'data':stock_money_db.stock_money()})