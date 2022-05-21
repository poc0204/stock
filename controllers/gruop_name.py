import config
import models.gruop_name_db as gruop_name_db
@config.app.route("/gruop_name/<gruop>",methods=['GET'])
def gruop_name(gruop):
    return config.render_template("gruop_name.html")

@config.app.route("/api/gruop_name/<gruop>",methods=['GET'])
def api_gruop_name(gruop):
    if gruop == '化學生技醫療':
        gruop = '生技醫療'
    if gruop == '化工':
        gruop = '化學'
    if gruop == '電腦及週邊設備':
        gruop = '電腦週邊'
    if gruop == '紡織纖維':
        gruop = '紡織'
    if gruop == '玻璃陶瓷':
        gruop = '玻璃'
    if gruop == '電子零組件':
        gruop = '電零組'
    if gruop == '航運業':
        gruop = '航運'
    if gruop == '金融保險':
        gruop = '金融'
    if gruop == '建材營造':
        gruop = '營建'
    gruop_name = gruop_name_db.gruop_name_db(gruop)
    return config.jsonify({'data':gruop_name}) ,200


