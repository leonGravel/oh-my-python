#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sqlalchemy import create_engine
import pandas as pd

# 获取数据库连接
engine = create_engine('mysql+pymysql://root:12345678@localhost:3306/ip_pools')

sql = "select * from ips"
# read_sql_query的两个参数: sql语句， 数据库连接
df = pd.read_sql_query(sql, engine)

# 输出ip表的查询结果
print(df)
