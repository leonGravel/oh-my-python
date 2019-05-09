#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
from tools import db_tools
# 获取数据库连接
engine = db_tools.get_conn('db_ip')

sql = "select * from ips"
# read_sql_query的两个参数: sql语句， 数据库连接
df = pd.read_sql_query(sql, engine)

# 输出ip表的查询结果
print(df)
