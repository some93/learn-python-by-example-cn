# 第 51 关：datetime（师兄带你学 Python）

## 🎯 这一关你会学到

- 获取当前日期时间
- 在 datetime 和字符串之间转换
- 进行时间加减运算
- 处理时区

## 🤔 先想一个问题

你在做一个全球化的应用，北京时间下午3点，东京是几点？纽约呢？时间处理看似简单，但涉及时区就头大了。Python 的 `datetime` 模块帮你搞定。

带着这个问题，我们来看代码。

## 📖 看代码

```python
# datetime

from datetime import datetime, timedelta, timezone

# 获取当前日期和时间
now = datetime.now()
print(now)
print(type(now))

# 创建指定日期时间
dt = datetime(2024, 6, 15, 14, 30, 0)
print(dt)

# 时间戳（timestamp）
ts = now.timestamp()
print(ts)    # 浮点数，从 1970-01-01 00:00:00 UTC 开始的秒数

# 时间戳转 datetime
print(datetime.fromtimestamp(ts))        # 本地时间
print(datetime.utcfromtimestamp(ts))     # UTC 时间

# 字符串转 datetime
dt = datetime.strptime('2024-06-15 14:30:00', '%Y-%m-%d %H:%M:%S')
print(dt)

# datetime 转字符串
print(now.strftime('%Y年%m月%d日 %H:%M:%S'))

# 时间加减
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))

# 时区处理
utc = timezone.utc
utc_now = datetime.now(utc)
print(f"UTC: {utc_now}")

# 东八区
bj_tz = timezone(timedelta(hours=8))
bj_now = utc_now.astimezone(bj_tz)
print(f"北京: {bj_now}")

# 东九区（东京）
tokyo_tz = timezone(timedelta(hours=9))
tokyo_now = utc_now.astimezone(tokyo_tz)
print(f"东京: {tokyo_now}")
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- `datetime.now()` 获取本地时间，`datetime.now(timezone.utc)` 获取 UTC 时间
- `strftime` 格式化为字符串，`strptime` 从字符串解析
- `timedelta` 做时间加减，支持天、小时、分钟、秒
- 时间戳是一个浮点数，跨平台跨语言通用
- 实际项目推荐用 `arrow` 或 `pendulum` 库，比标准库好用很多

## 🏃 跑一下试试

```bash
cd 51-datetime
python datetime_demo.py
```

## 💡 师兄的碎碎念

- `datetime.now()` 获取本地时间，`datetime.now(timezone.utc)` 获取 UTC 时间
- `strftime` 格式化为字符串，`strptime` 从字符串解析
- `timedelta` 做时间加减，支持天、小时、分钟、秒
- 时间戳是一个浮点数，跨平台跨语言通用
- 实际项目推荐用 `arrow` 或 `pendulum` 库，比标准库好用很多

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `datetime.now()` | 获取当前本地时间 |
| `datetime.strptime(s, fmt)` | 字符串转 datetime |
| `dt.strftime(fmt)` | datetime 转字符串 |
| `dt.timestamp()` | 转时间戳 |
| `timedelta(days=1)` | 时间间隔，用于加减 |
| `timezone(timedelta(hours=8))` | 创建时区 |

## ➡️ 下一关

下一关我们学习 [collections](../52-collections/README.md)，继续加油！
