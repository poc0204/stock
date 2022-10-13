import config
import models.fitx_db as fitx_db

@config.app.route("/api/fixt_amplitude",methods=['GET'])
def fixt_api():
    fitx_amplitude = fitx_db.fixt_amplitude_data()
    return config.jsonify(fitx_amplitude) ,200
