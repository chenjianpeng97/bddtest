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


@given('标准payload {payload_data}')
def step_impl(context, payload_data: str):
    context.stander_payload = json.loads(payload_data)


@when('请求 {method} {path} payload {payload_data}')
def step_impl(context, method, path, payload_data: str):
    # 如果有stander_payload，payload覆盖或添加进去
    if hasattr(context, 'stander_payload'):
        payload_data = json.dumps(dict(context.stander_payload, **json.loads(payload_data)))
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
    # 期望返回
    print(f"期望返回{load_json_file(json_file)}")
    # 实际返回
    print(f"实际返回{context.response.json()}")
    assert context.response.json() == load_json_file(json_file)


if __name__ == '__main__':
    import requests
    import json

    data = json.loads('{"hospitalName": "","hospitalCode": "","province": "","city": "","pageNum": 1,"pageSize": 10}')
    payload = {"hospitalName": "", "hospitalCode": "", "province": "", "city": "", "pageNum": 1, "pageSize": 10}
    print(type(data))
    print(type(payload))
    print(data)
    print(payload)
    assert payload == data
    pass
