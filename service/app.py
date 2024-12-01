#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Tuner
@contact:chenjianpeng97@outlook.com
@version: 1.0.0
@license: Apache Licence
@file: app.py.py
@time: 2024/11/28 9:56
"""
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# 医院主数据模型
# 定义医院模型
class Hospital(db.Model):
    __tablename__ = 'hospital'

    id = db.Column(db.Integer, primary_key=True)
    hospital_code = db.Column(db.String(60))
    hospital_name = db.Column(db.String(60))
    province = db.Column(db.String(150))
    city = db.Column(db.String(150))
    address = db.Column(db.String(100))
    level = db.Column(db.String(30))
    grade = db.Column(db.String(30))
    hospital_type = db.Column(db.String(50))
    hospital_group_id = db.Column(db.Integer, db.ForeignKey('hospital_group.id'))
    del_flag = db.Column(db.Integer, default=0)


class HospitalGroup(db.Model):
    __tablename__ = 'hospital_group'

    id = db.Column(db.Integer, primary_key=True)
    hospital_group_name = db.Column(db.String(50))
    group_type = db.Column(db.String(50))
    del_flag = db.Column(db.Integer, default=0)


# 创建数据库
with app.app_context():
    db.create_all()


# 查询医院主数据列表接口
@app.route('/hospital/list', methods=['POST'])
def get_hospital_list():
    # 对请求的处理
    try:
        # 这里解析请求的 JSON 数据
        page_num = request.json.get('pageNum', 1)
        page_size = request.json.get('pageSize', 10)

        # 查询医院数据，分页获取
        hospitals_query = db.session.query(Hospital).join(HospitalGroup, Hospital.hospital_group_id == HospitalGroup.id,
                                                          isouter=True).all()

        # 对数据进行简单的分页处理
        start = (page_num - 1) * page_size
        end = start + page_size
        hospitals_data = hospitals_query[start:end]

        # 将查询结果转换为字典格式
        result = {
            "data": [
                {
                    "hospitalName": hospital.hospital_name,
                    "hospitalCode": hospital.hospital_code,
                    "province": hospital.province,
                    "city": hospital.city,
                    "grade": hospital.grade,
                    "level": hospital.level,
                    "hospitalType": hospital.hospital_type,
                    "hospitalGroupName": hospital_group.hospital_group_name if hospital.hospital_group_id else "",
                    # 这里是修改的部分
                    "address": hospital.address
                }
                for hospital in hospitals_data
                for hospital_group in [HospitalGroup.query.get(hospital.hospital_group_id)]  # 直接查询医院集团
            ]
        }

        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
