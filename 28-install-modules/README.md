# 第 28 关：安装第三方模块（师兄带你学 Python）

## 🎯 这一关你会学到

- pip 包管理器
- pip install 安装模块
- venv 虚拟环境隔离依赖
- requirements.txt 管理依赖

## 🤔 先想一个问题

pip 像手机应用商店——搜一下、装一下就能用。venv 像给每个项目建独立手机——各自装各自的 app，互不干扰。

## 📖 看代码

```python
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
```

## 🔍 师兄给你逐行拆

Python 拥有全球最大的第三方模块库 PyPI（超过 40 万个包），用 pip 一行命令就能安装。

代码中的关键点已经在注释中标注，结合上面的完整代码逐段阅读即可。更多细节请运行代码观察输出。

## 🏃 跑一下试试

```bash
$ python install-modules.py
```

运行代码，观察输出，对照注释理解每一行。

## 💡 师兄的碎碎念

- **pip install / pip list / pip show**
- **python -m venv 创建虚拟环境**
- **pip freeze > requirements.txt 导出依赖**
- **pip install -r requirements.txt 安装依赖**

## 🎓 这一关的知识点清单

- **pip 包管理器**
- **pip install 安装模块**
- **venv 虚拟环境隔离依赖**
- **requirements.txt 管理依赖**

## ➡️ 下一关

本关搞定！接下来学 类和实例 👉 [下一关：类和实例 →](../29-classes-and-instances/)
