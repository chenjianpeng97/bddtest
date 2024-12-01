#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Tuner
@contact:chenjianpeng97@outlook.com
@version: 1.0.0
@license: Apache Licence
@file: json_handler.py
@time: 2024/11/27 17:19type
"""
import requests
from common.settings import PREFIX_URL

# 公共HTTP请求头
COMMON_HEADERS = {
    'User-Agent': 'Innovamed-Test/1.0.0',
    'Content-Type': 'application/json',
    'Authorization': None,
    'Accept': '*/*',
    'Host': PREFIX_URL[7:],
    'Connection': 'keep-alive'
}


class Request:
    # 组装请求
    def __init__(self, method, path, header=None, params=None, payload=None, auth=None):
        self.method = method
        # 组装URL
        self.url = PREFIX_URL + path
        self.header = header
        self.params = params
        self.payload = payload
        # TODO: 增加auth处理,BEARER TOKEN修改HEADER等
        self.auth = auth

    def __str__(self):
        return (f'actual request:\n'
                f'method={self.method}\n'
                f'url={self.url}\n'
                f'headers={self.header}\n'
                f'params={self.params}\n'
                f'payload={self.payload}\n'
                f'auth={self.auth}')

    # 发送请求
    def set_header(self, context=None) -> dict:
        # 输入context，如果context.auth_token存在，则添加到headers中
        header = COMMON_HEADERS.copy()
        if context and hasattr(context, "auth_token"):
            header["Authorization"] = f"Bearer {context.auth_token}"
        self.header = header
        return self.header

    def send(self):
        response = requests.request(self.method, self.url, headers=self.header, params=self.params, data=self.payload,
                                    auth=self.auth)
        # 打印真实的请求信息
        print(self)
        return response

    # 查看request发送的实际请求


if __name__ == '__main__':
    # 测试用例
    # 组装请求
    request = Request('GET', '/baidu.com')
    # 发送请求
    response = request.send()
    # 查看response
    print(response)
    pass
