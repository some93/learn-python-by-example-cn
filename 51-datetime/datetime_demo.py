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
