# -*- encoding: utf-8 -*-
"""
@File    : create_db.py
@Time    : 2021/4/28 1:24 下午
@Author  : yuecong
@Email   : yueconger@163.com
@Software: PyCharm
"""

from db.db_mysql import MysqlDB
from conf.config import config


def _create_table(mysqldb, sql):
    mysqldb.execute(sql)


def create_table():
    hello_world_table = '''
    CREATE TABLE IF NOT EXISTS `hello_world_table` (
      `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
      `title` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `publish_time` datetime DEFAULT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC
    '''

    if config.get('mysqldb').get('auto_create_tables'):
        mysqldb = MysqlDB(**config.get('mysqldb'))
        _create_table(mysqldb, hello_world_table)


if __name__ == '__main__':
    create_table()
