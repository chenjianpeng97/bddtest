#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Tuner
@contact:chenjianpeng97@outlook.com
@version: 1.0.0
@license: Apache Licence
@file: test_settings.py
@time: 2024/11/29 18:50
"""
from common.settings import get_db_config


# 对get_db_config进行测试
def test_get_db_config():
    db_config = get_db_config()
    assert db_config['host'] == 'localhost'


if __name__ == '__main__':
    pass
