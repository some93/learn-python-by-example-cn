# 安装第三方模块
#
# 这一关的命令需要在终端里执行，例如：
# python -m pip install requests
#
# 为了保证示例代码离线也能运行，这里用内置 json 模块演示
# “导入模块 -> 调用模块功能 -> 得到结果” 的流程。

import json


print("=== 使用内置模块 json ===")

profile = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Web"],
}

json_text = json.dumps(profile, ensure_ascii=False, indent=2)
print(json_text)

parsed = json.loads(json_text)
print(parsed["name"])
print(parsed["skills"][0])
print(type(parsed).__name__)


print("\n=== requirements.txt 示例 ===")

requirements = [
    "requests==2.32.3",
    "rich==13.7.1",
]

print("\n".join(requirements))
