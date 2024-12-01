#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Tuner
@contact:chenjianpeng97@outlook.com
@version: 1.0.0
@license: Apache Licence
@file: settings.py
@time: 2024/11/28 10:23
"""
import os

# 目录常量
SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
# 测试数据目录，应和features目录在同一级
TESTDATA_DIR = os.path.normpath(os.path.join(SETTINGS_DIR, "../testdata"))
# 测试数据sqls目录
TESTDATA_SQLS_DIR = os.path.join(TESTDATA_DIR, "sqls")
# 测试数据jsons目录
TESTDATA_JSONS_DIR = os.path.join(TESTDATA_DIR, "jsons")
# 环境前缀
PREFIX_URL = "http://127.0.0.1:5000"
# 数据库配置
DB_CONFIG = {"sql_type": "sqlite", "config": {"db_path": os.path.join(SETTINGS_DIR, "../service/instance/test.db")}}


def get_db_config(config=DB_CONFIG) -> dict:
    """
    根据sql_type的配置，给SQLHandler提供数据库信息
    :return: {"sql_type":数据库配置,"db_config":配置参数}
    """
    # sqlite
    if config["sql_type"] == "sqlite":
        return {"sql_type": "sqlite", "db_config": config["config"]["db_path"]}
    # mysql


if __name__ == '__main__':
    print(TESTDATA_DIR)
    pass
