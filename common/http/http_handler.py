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


class Request:
    # 组装请求
    def __init__(self, method, url, headers=None, params=None, payload=None, auth=None):
        self.method = method
        # 组装URL
        self.url = URL_PREFIX + url
        self.params = params
        self.payload = payload
        self.headers = headers
        # TODO: 增加auth处理,BEARER TOKEN修改HEADER等
        self.auth = auth

    # 发送请求
    def send(self):
        response = requests.request(self.method, self.url, headers=self.headers, params=self.params, data=self.payload,
                                    auth=self.auth)

    # 查看request发送的实际请求
    def __str__(self):
        return f'{self.method} {self.url} {self.headers} {self.params} {self.payload} {self.auth}'


if __name__ == '__main__':
    # 测试用例
    # 组装请求
    request = Request('GET', '/baidu.com')
    # 发送请求
    response = request.send()
    # 查看response
    print(response)
    pass
