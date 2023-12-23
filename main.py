from flask import Flask, request, jsonify
import json
import random

app = Flask(__name__)

with open('area.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

cities = [
    "北京路", "上海路", "广州路", "深圳路", "成都路", "重庆路", "天津路", "南京路", "杭州路",
    "武汉路", "西安路", "长沙路", "青岛路", "沈阳路", "哈尔滨路", "苏州路", "无锡路", "宁波路",
    "大连路", "福州路", "厦门路", "长春路", "石家庄路", "昆明路", "合肥路", "南昌路", "郑州路",
    "济南路", "南宁路", "南通路", "常州路", "东莞路", "佛山路", "珠海路", "惠州路", "中山路",
    "海口路", "桂林路", "贵阳路", "兰州路", "西宁路", "银川路"
]

def find_area(id_number):
    # 获取身份证前6位
    area_code = id_number[:6]

    # 查询对应的地区
    area = data.get(area_code)

    if area:
        # 随机选择一个城市名
        random_city = random.choice(cities)

        # 随机生成数字
        random_num_1 = random.randint(1, 999)
        random_num_2 = random.randint(1, 200)

        result = f"{area}\n{random_city} {random_num_1:03d}号 {random_num_2}户"
        return result
    else:
        return "未找到对应地区"

@app.route('/')
def get_area():
    cid = request.args.get('cid')
    result = find_area(cid)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, port=8001)
