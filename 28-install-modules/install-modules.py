# 安装第三方模块

# Python 使用 pip 安装第三方模块
# pip install requests
# pip install numpy

# 查看已安装的模块
# pip list
# pip show requests

# 常用第三方模块示例
# import requests       # HTTP 请求
# import numpy as np    # 数值计算
# import pandas as pd   # 数据分析

# 使用 venv 创建虚拟环境（推荐！）
# python -m venv myenv          # 创建
# source myenv/bin/activate     # 激活（Linux/Mac）
# myenv\Scripts\activate        # 激活（Windows）
# deactivate                    # 退出

# requirements.txt：记录项目依赖
# pip freeze > requirements.txt        # 导出
# pip install -r requirements.txt      # 安装

# 演示：使用内置模块
import json

data = {'name': 'Alice', 'age': 25, 'skills': ['Python', 'Go']}
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(json_str)

parsed = json.loads(json_str)
print(parsed['name'])
print(type(parsed))
