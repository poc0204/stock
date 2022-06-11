import config
import models.stock_name_db as stock_name_db
@config.app.route("/stock_name/<stock>",methods=['GET'])
def stock_name(stock):
    return config.render_template("stock_name.html")

@config.app.route("/api/stock_id/<stock_id>",methods=['GET'])
def stock_id(stock_id):
    stock_id = stock_name_db.stock_id(stock_id)
    return config.jsonify({'data':stock_id}) ,200