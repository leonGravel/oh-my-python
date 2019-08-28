#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sqlalchemy import create_engine
from tools import properties_tools


# 获取数据库连接
def get_conn(db_type):
    _property = properties_tools.load_properties("properties-dev.yaml")
    _db = _property['datasource'][db_type]
    _host = _db['host']
    _port = _db['port']
    _db_name = _db['db_name']
    _username = _db['username']
    _password = _db['password']
    _conn = 'mysql+pymysql://%s:%s@%s:%s/%s' % (_username, _password, _host,_port, _db_name)
    return create_engine(_conn)