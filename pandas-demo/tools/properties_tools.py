#!/usr/bin/python
# -*- coding: UTF-8 -*-
import yaml
import os
import properties
properties_path = os.path.dirname(properties.__file__)


# 根据配置文件名称加载配置文件
def load_properties(file_name):
    yaml_path = os.path.join(properties_path, file_name)
    f = open(yaml_path, 'r', encoding='utf-8')
    return yaml.load(f.read())