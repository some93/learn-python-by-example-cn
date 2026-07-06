# 第 51 关：datetime（师兄带你学 Python）

## 🎯 这一关你会学到

- `date`、`time`、`datetime` 分别表示什么
- 如何在字符串和 `datetime` 之间转换
- 如何用 `timedelta` 做时间加减
- 时间戳为什么更适合跨系统传输
- naive datetime 和 aware datetime 的区别
- 如何做基础时区转换

## 🤔 先想一个问题

订单系统里经常会出现这些需求：下单时间、支付截止时间、7 天后自动确认收货、给海外用户显示当地时间。

如果只把时间当普通字符串处理，很快会出问题：字符串不能可靠加减，时区也说不清。`datetime` 模块解决的是：**用明确的数据类型表达日期、时间、时间间隔和时区**。

## 📖 看代码

```python
# datetime 日期时间处理

from datetime import date, datetime, time, timedelta, timezone


print("=== 创建 date / time / datetime ===")

# date 只表示日期，time 只表示一天中的时间。
course_day = date(2026, 7, 6)
start_time = time(15, 30, 45)

# datetime 同时包含日期和时间；这里故意用固定时间，方便对照输出。
lesson_time = datetime(2026, 7, 6, 15, 30, 45)

print(course_day)
print(start_time)
print(lesson_time)


print("\n=== 字符串和 datetime 互转 ===")

text = "2026-07-06 15:30:45"

# strptime 按格式解析字符串，格式必须和文本严格对应。
parsed = datetime.strptime(text, "%Y-%m-%d %H:%M:%S")
print(parsed)

# strftime 把 datetime 格式化成适合展示的字符串。
print(parsed.strftime("%Y年%m月%d日 %H:%M"))
print(parsed.strftime("%A"))


print("\n=== timedelta 时间加减 ===")

# timedelta 表示一段时间，可用于计算截止时间、过期时间。
deadline = lesson_time + timedelta(days=7, hours=2)
before = lesson_time - timedelta(minutes=45)
duration = deadline - lesson_time

print(deadline)
print(before)
print(duration)
print(duration.total_seconds())


print("\n=== 时间戳 timestamp ===")

beijing_tz = timezone(timedelta(hours=8))

# 带时区的 datetime 叫 aware datetime，转时间戳才不会依赖本机时区。
beijing_time = datetime(2026, 7, 6, 15, 30, 45, tzinfo=beijing_tz)
timestamp = beijing_time.timestamp()

print(timestamp)
print(datetime.fromtimestamp(timestamp, tz=timezone.utc))
print(datetime.fromtimestamp(timestamp, tz=beijing_tz))


print("\n=== 时区转换 ===")

tokyo_tz = timezone(timedelta(hours=9))
new_york_tz = timezone(timedelta(hours=-4))

# astimezone 不改变同一瞬间，只改变展示所在时区。
utc_time = beijing_time.astimezone(timezone.utc)
tokyo_time = beijing_time.astimezone(tokyo_tz)
new_york_time = beijing_time.astimezone(new_york_tz)

print(f"北京: {beijing_time.isoformat()}")
print(f"UTC: {utc_time.isoformat()}")
print(f"东京: {tokyo_time.isoformat()}")
print(f"纽约: {new_york_time.isoformat()}")


print("\n=== naive vs aware ===")

# 没有 tzinfo 的 datetime 是 naive datetime，不携带时区信息。
naive = datetime(2026, 7, 6, 15, 30, 45)
aware = naive.replace(tzinfo=beijing_tz)

print(naive.tzinfo)
print(aware.tzinfo)
print(aware.isoformat())
```

## 🔍 师兄给你拆开讲

`date` 只关心年月日，`time` 只关心时分秒，`datetime` 同时包含日期和时间。不要所有场景都用字符串存时间，字符串适合展示，计算时要先变成时间对象。

`strptime()` 是 parse time，把字符串解析成 `datetime`；`strftime()` 是 format time，把 `datetime` 格式化成字符串。格式里的 `%Y` 表示四位年份，`%m` 表示月份，`%d` 表示日期，`%H:%M:%S` 表示时分秒。

`timedelta` 表示一段时间。它不能表示“一个自然月”，但非常适合表达 7 天后、2 小时后、45 分钟前这类固定间隔。两个 `datetime` 相减，得到的也是 `timedelta`。

时间戳是从 `1970-01-01 00:00:00 UTC` 开始计算的秒数。它和展示格式无关，跨系统传输很方便。但把时间戳转回本地时间时，一定要明确时区。

没有 `tzinfo` 的对象叫 naive datetime，它只是一串日期时间数字，不知道自己属于哪个时区。带 `tzinfo` 的对象叫 aware datetime，适合做时间戳、跨时区转换这类操作。

## 🏃 跑一下试试

```bash
cd 51-datetime
python datetime_demo.py
```

输出：

```text
=== 创建 date / time / datetime ===
2026-07-06
15:30:45
2026-07-06 15:30:45

=== 字符串和 datetime 互转 ===
2026-07-06 15:30:45
2026年07月06日 15:30
Monday

=== timedelta 时间加减 ===
2026-07-13 17:30:45
2026-07-06 14:45:45
7 days, 2:00:00
612000.0

=== 时间戳 timestamp ===
1783323045.0
2026-07-06 07:30:45+00:00
2026-07-06 15:30:45+08:00

=== 时区转换 ===
北京: 2026-07-06T15:30:45+08:00
UTC: 2026-07-06T07:30:45+00:00
东京: 2026-07-06T16:30:45+09:00
纽约: 2026-07-06T03:30:45-04:00

=== naive vs aware ===
None
UTC+08:00
2026-07-06T15:30:45+08:00
```

## 💡 师兄的提醒

示例里的纽约时区用的是固定 `-04:00` 偏移，只适合教学。真实项目如果要处理城市时区和夏令时，优先看标准库 `zoneinfo` 或成熟第三方库，别自己维护时区规则。

项目里常见做法是：数据库存 UTC 或时间戳，接口传 ISO 8601 字符串，展示时再按用户所在时区转换。

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `date(...)` | 只表示日期 |
| `time(...)` | 只表示时间 |
| `datetime(...)` | 表示日期加时间 |
| `strptime()` | 字符串解析成时间对象 |
| `strftime()` | 时间对象格式化成字符串 |
| `timedelta(...)` | 表示时间间隔 |
| `timestamp()` | 转成 Unix 时间戳 |
| `fromtimestamp(..., tz=...)` | 按指定时区从时间戳还原 |
| `timezone(...)` | 创建固定偏移时区 |
| `astimezone()` | 转换展示时区 |
| naive / aware | 不带时区 / 带时区的 datetime |

## ➡️ 下一关

下一关：[collections](../52-collections/README.md)。
