import unittest
from common.sql.sql_handler import SQLHandler  # 假设你的类在 sql_handler.py 文件中


class TestSQLHandler(unittest.TestCase):
    def setUp(self):
        # 设置测试数据库路径
        self.sqlite_path = './test.db'
        self.db = SQLHandler(sql_type='sqlite', config={'db_path': self.sqlite_path})
        self.db.create_cursor()
        # 清空数据库
        self.db.execute_sql('DROP TABLE IF EXISTS hospital;')
        # 创建测试表和插入测试数据
        self.db.execute_sql('''
        CREATE TABLE IF NOT EXISTS hospital (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );
        ''')
        self.db.execute_sql('INSERT INTO hospital (name) VALUES ("Hospital A");')
        self.db.execute_sql('INSERT INTO hospital (name) VALUES ("Hospital B");')

    def test_fetch_all(self):
        # 执行查询
        self.db.execute_sql('SELECT * FROM hospital;')
        data = self.db.fetchall()
        # 断言查询结果
        self.assertEqual(len(data), 2)  # 应该返回2条记录
        self.assertEqual(data[0][1], "Hospital A")  # 第一条记录的名称
        self.assertEqual(data[1][1], "Hospital B")  # 第二条记录的名称

    def tearDown(self):
        # 清理数据库
        self.db.execute_sql('DROP TABLE IF EXISTS hospital;')
        self.db.close()


if __name__ == '__main__':
    unittest.main()
