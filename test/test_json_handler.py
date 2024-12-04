#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Tuner
@contact:chenjianpeng97@outlook.com
@version: 1.0.0
@license: Apache Licence
@file: test_json_handler.py
@time: 2024/12/4 21:55
@doc: 
"""
import unittest
from common.json.json_handler import assert_json, get_data_by_jsonpath
from jsonpath_ng import jsonpath, parse


class TestjsonHandler(unittest.TestCase):
    def setUp(self):
        # 测试用json
        self.json_data = {
            "data": [
                {
                    "id": 1,
                    "address": "上海市黄浦区人民大道1号",
                    "hospitalCode": "H001",
                    "hospitalName": "上海市第一人民医院",
                    "price": 55.55
                },
                {
                    "id": 2,
                    "address": "南京市中山路1号",
                    "hospitalCode": "H002",
                    "hospitalName": "南京市中心医院",
                    "price": 66.66
                }
            ]
        }

    def test_get_data_by_jsonpath_success(self):
        # 测试get_data_by_jsonpath函数
        input_json = self.json_data
        input_jsonpath = "$.data[1].hospitalName"
        expected_output = "南京市中心医院"
        result = get_data_by_jsonpath(input_json, input_jsonpath)
        self.assertEqual(result, expected_output)

    def test_get_data_by_jsonpath_not_find_element(self):
        # 测试get_data_by_jsonpath函数
        input_json = self.json_data
        input_jsonpath = "$.data[2].hospitalName"
        expected_output = None
        result = get_data_by_jsonpath(input_json, input_jsonpath)
        self.assertEqual(result, expected_output)

    def test_json_assert_str_success(self):
        # 测试json_assert函数
        input_json = self.json_data
        assert_str = '$.data[1].hospitalName == "南京市中心医院"'
        assert_json(input_json, assert_str)

    def test_json_assert_str_fail(self):
        # 测试json_assert函数
        input_json = self.json_data
        assert_str = '$.data[1].hospitalName == "错误字符"'
        with self.assertRaises(AssertionError):
            assert_json(input_json, assert_str)

    def test_json_assert_int_success(self):
        # 测试json_assert函数
        input_json = self.json_data
        assert_str = '$.data[1].id == 2'
        assert_json(input_json, assert_str)

    def test_json_assert_int_fail(self):
        # 测试json_assert函数
        input_json = self.json_data
        assert_str = '$.data[1].id == 3'
        with self.assertRaises(AssertionError):
            assert_json(input_json, assert_str)

    def test_json_assert_float_success(self):
        # 测试json_assert函数
        input_json = self.json_data
        assert_str = '$.data[1].price == 66.66'
        assert_json(input_json, assert_str)

    def test_json_assert_float_fail(self):
        # 测试json_assert函数
        input_json = self.json_data
        assert_str = '$.data[1].price == 77.77'
        with self.assertRaises(AssertionError):
            assert_json(input_json, assert_str)


if __name__ == '__main__':
    pass
