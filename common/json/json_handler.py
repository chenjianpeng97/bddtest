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
from typing import Union


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
def get_data_by_jsonpath(json_data: dict, jsonpath_str: str) -> Union[
    int, str, float, None, dict]:  # 使用 jsonpath-ng 进行查询
    """

    :param json_data:  json_data:dic数据
    :param jsonpath_str: 包含jsonpath的字符串
    :return: 未找到返回None，找到返回对应数据int str dict float类型
    """
    jsonpath_expression = parse(jsonpath_str)
    results = jsonpath_expression.find(json_data)
    # 当匹配不到结果时
    if not results:
        return None
    result_list = [match.value for match in results]
    return result_list[0]


def assert_json(json_data: dict, assert_str: str) -> None:
    """

    :param json_data: json(dict)数据
    :param assert_str: gherkin用例中字符串约定'{jsonpath_expression} {operator} {expect_value} {logic_operator} {jsonpath_expression} {operator} {expect_value}'
    :return:
    """

    # 解析assert_str,输入格式'jsonpath_expression '
    jsonpath_str, operator, expect_value = assert_str.split()
    # 如果expect_value是整数，则将其转换为int类型
    if expect_value.isdigit():
        expect_value = int(expect_value)
    # 如果expect_value是浮点数，则将其转换为float类型
    elif expect_value.replace('.', '', 1).isdigit():
        expect_value = float(expect_value)
    # 如果是字符串,脱去""或''
    elif expect_value.startswith(("'", '"')) and expect_value.endswith(("'", '"')):
        expect_value = expect_value[1:-1]
    actual_value = get_data_by_jsonpath(json_data, jsonpath_str)
    # 定义操作符与相应的比较函数的映射
    operator_map = {
        '==': lambda a, b: a == b,
        '!=': lambda a, b: a != b,
        '>': lambda a, b: a > b,
        '<': lambda a, b: a < b,
        '>=': lambda a, b: a >= b,
        '<=': lambda a, b: a <= b,
    }
    # 打印实际值和期望值
    print(f"Actual value: {actual_value}, Expected value: {expect_value}")
    # assert actual_value == expect_value
    # 查找操作符并执行相应的比较
    if operator in operator_map:
        assert operator_map[operator](actual_value,
                                      expect_value), (f"Actual value: {actual_value}, "
                                                      f"Expected value: {expect_value}, "
                                                      f"assert operator: {operator}")
    else:
        # 未找到定义的操作符
        raise ValueError(f"Unsupported operator: {operator}")


if __name__ == '__main__':
    pass
