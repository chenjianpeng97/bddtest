#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Tuner
@contact:chenjianpeng97@outlook.com
@version: 1.0.0
@license: Apache Licence
@file: sql_handler.py
@time: 2024/11/28 10:23
"""
import pymysql
import sqlite3
from common.settings import get_db_config as dbconfig
from common.settings import TESTDATA_SQLS_DIR
import os


class SQLHandler:
    def __init__(self, sql_type=dbconfig()['sql_type'], config: dict = dbconfig()['db_config']):
        self.sql_type = sql_type
        self.conn = self._connect(config)
        self.cursor = None

    # 连接数据库私有方法
    def _connect(self, config: dict):
        if self.sql_type == 'mysql':
            # TODO：增加mysql连接方式
            pass
        elif self.sql_type == 'sqlite':
            return sqlite3.connect(config)

    def create_cursor(self):
        self.cursor = self.conn.cursor()

    def execute_sql(self, sql_statement: str):
        self.cursor.execute(sql_statement)

    def execute_sql_file(self, file_name: str):
        # 调用时只需要输入sql文件名
        file_path = os.path.join(TESTDATA_SQLS_DIR, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            sql_script = file.read()
            self.cursor.executescript(sql_script)

    # 提交更改
    def commit(self):
        self.conn.commit()

    # 读取数据
    def fetchall(self):
        return self.cursor.fetchall()

    # 读取一行数据
    def fetchone(self):
        return self.cursor.fetchone()

    # 关闭连接
    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    # 例程
    sqlite_path = '../../test/test.db'
    db = SQLHandler(sql_type='sqlite', config={'db_path': sqlite_path})
    db.create_cursor()
    db.execute_sql('SELECT * FROM hospital;')
    data = db.fetchall()
    print(data)
    pass
