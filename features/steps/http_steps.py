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
from common.http.http_handler import Request


# @when("管理员用户请求 POST /supplierData/addSupplierDetail Body '.../成功增加经销商.json'")
@when("管理员用户请求 POST {path} Body '{json_path}'")
def step_impl(context, path, json_path):
    pass


@when('请求 {method} {path} payload {payload_data}')
def step_impl(context, method, path, payload_data):
    # data = json.dumps(json.loads(
    #     payload_data))
    # print(type(data))
    # print(data)
    # 组装URL
    request = Request(method=method, path=path, payload=payload_data)
    request.set_header(context=context)
    # 存储返回信息到context
    context.response = request.send()


@then('状态码:{status_code}')
def step_impl(context, status_code):
    print(context.response.status_code)
    assert context.response.status_code == int(status_code)


@then('返回值JSON数据:"{json_file}"')
def step_impl(context, json_file):
    print(load_json_file(json_file))
    print(type(load_json_file(json_file)))
    print(context.response.json())
    print(type(context.response.json()))
    assert context.response.json() == load_json_file(json_file)


if __name__ == '__main__':
    import requests
    import json

    url = "http://127.0.0.1:5000/hospital/list"

    payload = json.dumps({
        "hospitalName": "",
        "hospitalCode": "",
        "province": "",
        "city": "",
        "pageNum": 1,
        "pageSize": 10
    })
    print(payload)
    print(type(payload))
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpblR5cGUiOiJsb2dpbiIsImxvZ2luSWQiOiLlhazlj7jotKblj7c6MSIsInJuU3RyIjoiNzYzZGllWU5URG85bG9FakNpa242MG5lN3hzUEdPdmYiLCJ1c2VySWQiOjF9.GeOkfpxwm1g-MMIkGNoNHGzUDE8wXEYzINs8mIvfoog',
        'Accept': '*/*',
        'Host': '127.0.0.1:5000',
        'Connection': 'keep-alive'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

    pass
