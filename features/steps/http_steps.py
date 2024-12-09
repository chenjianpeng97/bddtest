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
from common.json.json_handler import load_json_file, assert_json
from common.settings import PREFIX_URL as PREFIX
from common.http.http_handler import Request


@given('默认payload {payload_data}')
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
    print(f"实际返回{context.response.json()}")


@then('状态码:{status_code}')
def step_impl(context, status_code):
    print(f"期望状态码{status_code}")
    print(f"实际状态码{context.response.status_code}")
    assert context.response.status_code == int(status_code)


@then('返回值JSON数据:"{json_data}"')
def step_impl(context, json_data: str):
    # 根据json_data是否有.json后缀判断是否要读取json文件
    if json_data.endswith('.json'):
        except_json = load_json_file(json_data)
    else:
        # 当是不为.json的字符串时，直接解析为json
        except_json = json.loads(json_data)

    # 期望返回
    print(f"期望返回{except_json}")
    # 实际返回
    print(f"实际返回{context.response.json()}")
    assert context.response.json() == except_json


@then('返回JSON断言:"{json_assert}"')
def step_impl(context, json_assert: str):
    assert_json(json_data=context.response.json(), assert_str=json_assert)
    pass


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
