# author    : Charles
# time      ：2020/7/8  18:14 
# file      ：getData.PY
# project   ：apiToy
# IDE       : PyCharm

from app.libs.yellowprint import YellowPrint
from flask import jsonify

yp_data = YellowPrint('yp_data', url_prefix='/data')


@yp_data.route('/all', methods=['GET'])
def get_data():
    data = {
      "code": 200,
      "time": "2020-05-28,14:29:31",
      "day_of_week": 1,
      "data": {
        "building": 50,
        "building_in": 15,
        "detectors": 5000,
        "area": 4999,
        "usage": dict(total=2000,
                      week=[41, 41, 41, 41, 41, 12, 21, 51, 51, 12, 41, 41, 41, 41, 41, 12, 21, 51, 51, 12, 41, 41, 41,
                            41, 41, 12, 21, 51, 51, 12, 41, 41, 41, 41, 41, 12, 21, 51, 51, 12, 123, 44, 88],
                      week_forcast=[41, 41, 41, 41, 41, 12, 21, 51, 51, 12, 41, 41, 41, 41, 41, 12, 21, 51, 51, 12, 41,
                                    41, 41, 41, 41, 12, 21, 51, 51, 12, 41, 41, 41, 41, 41, 12, 21, 51, 51, 12, 123, 44,
                                    88], month=[111, 111, 111, 111, 111, 111, 111]),
        "power": dict(peak=2000,
                      week=[41, 41, 41, 41, 41, 12, 21, 51, 51, 12, 41, 41, 41, 41, 41, 12, 21, 51, 51, 12, 41, 41, 41,
                            41, 41, 12, 21, 51, 51, 12, 41, 41, 41, 41, 41, 12, 21, 51, 51, 12, 123, 44, 88],
                      week_forcast=[41, 41, 41, 41, 41, 12, 21, 51, 51, 12, 41, 41, 41, 41, 41, 12, 21, 51, 51, 12, 41,
                                    41, 41, 41, 41, 12, 21, 51, 51, 12, 41, 41, 41, 41, 41, 12, 21, 51, 51, 12, 123, 44,
                                    88], advise=[]),
        "ratio_public": 2000,
        "ratio_company": 2000,
        "num_company": 134
      }
    }
    return jsonify(data)