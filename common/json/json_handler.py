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
from jsonpath_ng import jsonpath, parse


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


# 根据jsonpath找数据函数
def get_data_by_jsonpath(json_data: dict, jsonpath_str: str) -> list:  # 使用 jsonpath-ng 进行查询
    jsonpath_expr = parse(jsonpath_str)
    matches = jsonpath_expr.find(json_data)
    result = [match.value for match in matches]
    return result


def json_assert():
    pass


if __name__ == '__main__':
    import json
    from jsonpath_ng import jsonpath, parse

    # 示例 JSON 数据
    data = {
        "store": {
            "book": [
                {"category": "reference", "author": "Nigel Rees", "title": "Sayings of the Century", "price": 8.95},
                {"category": "fiction", "author": "Evelyn Waugh", "title": "Sword of Honour", "price": 12.99},
                {"category": "fiction", "author": "Herman Melville", "title": "Moby Dick", "isbn": "0-553-21311-3",
                 "price": 8.99},
                {"category": "fiction", "author": "J. R. R. Tolkien", "title": "The Lord of the Rings",
                 "isbn": "0-395-19395-8", "price": 22.99}
            ],
            "bicycle": {"color": "red", "price": 19.95}
        }
    }
    input_json_path = "$.store.book[0]"
    expect_result = {"category": "reference", "author": "Nigel Rees", "title": "Sayings of the Century", "price": 8.95}
    # 根据input_json_path查询json数据
    jsonpath_expr = parse(input_json_path)
    matches = jsonpath_expr.find(data)
    print(matches)
    # 使用 jsonpath-ng 进行查询
    # print(expect_result)
    result = [match.value for match in matches]
    print(type(result[0]))
    print(result[0])

    assert result[0] == expect_result
