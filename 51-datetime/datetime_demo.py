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
