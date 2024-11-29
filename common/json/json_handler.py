#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Tuner
@contact:chenjianpeng97@outlook.com
@version: 1.0.0
@license: Apache Licence
@file: json_handler.py
@time: 2024/11/27 16:53
"""
import json
from common.settings import TESTDATA_JSONS_DIR
import os


def load_json_file(file_name: str) -> dict:
    """
    读取json文件
    :param file_name:
    :return: json数据
    """
    file_path = os.path.join(TESTDATA_JSONS_DIR, file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

if __name__ == '__main__':

    # 测试jsonpath
    pass
