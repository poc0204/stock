import config
import models.stock_name_db as stock_name_db
@config.app.route("/stock_name/<stock>",methods=['GET'])
def stock_name(stock):

    return config.render_template("stock_name.html")

@config.app.route("/api/stock_name/<stock>",methods=['GET'])
def api_stock_name(stock):
    stock_name_data = stock_name_db.stock_name_db(stock)
    return config.jsonify({'data':stock_name_data}) ,200

@config.app.route("/api/stock_id/<stock>",methods=['GET'])
def stock_id(stock):
    stock_id = stock_name_db.stock_id_k(stock)
    return config.jsonify({'data':stock_id}) ,200