#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Tuner
@contact:chenjianpeng97@outlook.com
@version: 1.0.0
@license: Apache Licence
@file: http_steps.py.py
@time: 2024/11/27 15:14
"""
import requests
import json
from behave import given, when, then
from common.json.json_handler import load_json_file
from common.settings import PREFIX_URL as PREFIX
from common.settings import set_header


# @when("管理员用户请求 POST /supplierData/addSupplierDetail Body '.../成功增加经销商.json'")
@when("管理员用户请求 POST {path} Body '{json_path}'")
def step_impl(context, path, json_path):
    pass


@when('请求 {method} {path} payload {payload_data}')
def step_impl(context, method, path, payload_data):
    # 组装URL
    url = PREFIX + path

    print(payload_data)
    print(type(payload_data))
    payload = json.dumps(
        payload_data)
    print(f'payload is {payload}')
    print(f'payload type is {type(payload)}')
    headers = set_header(context)
    context.response = requests.request("POST", url, headers=headers, data=payload)
    print(context.response.text)


if __name__ == '__main__':
    payload = '{"hospitalName": "","hospitalCode": "","province": "","city": "","pageNum": 1,"pageSize": 10}'
    print(json.dumps(
        load_json(payload)))
    pass
