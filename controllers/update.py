import config
import models.update_all as update_all
@config.app.route("/updata/stock_money")
def updata_stocl_money():
    return update_all.stock_money_update()
@config.app.route("/updata/group_price")
def updata_group_pricey():
    return update_all.group_price()