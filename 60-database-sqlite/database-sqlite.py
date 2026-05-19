# 使用 SQLite

import sqlite3
import os

# SQLite 是内嵌数据库，不需要安装服务器
# Python 内置 sqlite3 模块

# 创建/连接数据库（使用内存数据库演示）
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# 创建表
cursor.execute('''CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT
)''')

# 插入数据（用 ? 占位符防止 SQL 注入！）
cursor.execute('INSERT INTO users (name, age, email) VALUES (?, ?, ?)',
               ('Alice', 25, 'alice@example.com'))
cursor.execute('INSERT INTO users (name, age, email) VALUES (?, ?, ?)',
               ('Bob', 30, 'bob@example.com'))
cursor.execute('INSERT INTO users (name, age, email) VALUES (?, ?, ?)',
               ('Charlie', 28, 'charlie@example.com'))

# 批量插入
users = [
    ('Dave', 22, 'dave@example.com'),
    ('Eve', 35, 'eve@example.com'),
]
cursor.executemany('INSERT INTO users (name, age, email) VALUES (?, ?, ?)', users)

conn.commit()    # 提交事务

# 查询数据
cursor.execute('SELECT * FROM users')
print("所有用户:")
for row in cursor.fetchall():
    print(f"  {row}")

# 条件查询
cursor.execute('SELECT name, age FROM users WHERE age > ?', (25,))
print("\n年龄大于25:")
for row in cursor.fetchall():
    print(f"  {row}")

# 更新数据
cursor.execute('UPDATE users SET age = ? WHERE name = ?', (26, 'Alice'))
conn.commit()

# 删除数据
cursor.execute('DELETE FROM users WHERE name = ?', ('Eve',))
conn.commit()

# 查看结果
cursor.execute('SELECT * FROM users')
print("\n更新后:")
for row in cursor.fetchall():
    print(f"  {row}")

# 使用 Row 工厂，可以按列名访问
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute('SELECT * FROM users WHERE name = ?', ('Alice',))
row = cursor.fetchone()
print(f"\nAlice: name={row['name']}, age={row['age']}")

# 关闭连接
conn.close()

# 注意事项：
# 1. 永远用 ? 占位符，不要拼接 SQL 字符串（防 SQL 注入）
# 2. 修改数据后要 commit()
# 3. 实际项目中用 with conn: 自动管理事务
