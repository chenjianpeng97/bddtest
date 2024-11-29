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
class Hospital(db.Model):
    __tablename__ = 'hospital'
    id = db.Column(db.Integer, primary_key=True)
    hospital_code = db.Column(db.String(60), nullable=True)
    hospital_name = db.Column(db.String(60), nullable=True)
    province = db.Column(db.String(150), nullable=True)
    city = db.Column(db.String(150), nullable=True)
    address = db.Column(db.String(100), nullable=True)
    level = db.Column(db.String(30), nullable=True)
    grade = db.Column(db.String(30), nullable=True)
    hospital_type = db.Column(db.String(50), nullable=True)
    hospital_group_id = db.Column(db.Integer, nullable=True)
    del_flag = db.Column(db.Integer, default=0)

# 创建数据库
with app.app_context():
    db.create_all()

# 查询医院主数据列表接口
@app.route('/hospital/list', methods=['POST'])
def get_hospital_list():
    data = request.json
    hospital_name = data.get('hosptailName', '')
    hospital_code = data.get('hospitalCode', '')
    province = data.get('province', '')
    city = data.get('city', '')
    page_num = data.get('pageNum', 1)
    page_size = data.get('pageSize', 10)

    query = Hospital.query.filter(Hospital.del_flag == 0)

    if hospital_name:
        query = query.filter(Hospital.hospital_name.like(f'%{hospital_name}%'))
    if hospital_code:
        query = query.filter(Hospital.hospital_code.like(f'%{hospital_code}%'))
    if province:
        query = query.filter(Hospital.province.like(f'%{province}%'))
    if city:
        query = query.filter(Hospital.city.like(f'%{city}%'))

    # 分页查询
    hospitals = query.paginate(page=page_num, per_page=page_size)

    result = {
        "data": [
            {
                "hosptailName": hospital.hospital_name,
                "hospitalCode": hospital.hospital_code,
                "province": hospital.province,
                "city": hospital.city,
                "grade": hospital.grade,
                "level": hospital.level,
                "hospitalType": hospital.hospital_type,
                "hospitalGroupName": '',  # 这里可以根据需要填充集团医院名称
                "address": hospital.address
            }
            for hospital in hospitals.items
        ]
    }

    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)

