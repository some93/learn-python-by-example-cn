# 第 60 关：使用 SQLite（师兄带你学 Python）

## 🎯 这一关你会学到

- SQLite 是什么，为什么适合小型项目和本地存储
- 如何用 `sqlite3` 创建表、插入、查询、更新、删除
- `executemany()` 如何批量插入
- 为什么必须使用参数化查询防 SQL 注入
- `commit()`、`with conn:` 和回滚的关系
- 如何用 `sqlite3.Row` 按列名访问查询结果

## 🤔 先想一个问题

你的程序要保存用户、订单、配置、任务记录。用文本文件当然也能存，但查询、更新、排序、去重很快会变麻烦。

SQLite 是一个嵌入式数据库，不需要单独安装数据库服务器。Python 标准库自带 `sqlite3`，一个文件就可以是一个数据库。这一章用内存数据库演示，方便反复运行。

## 📖 看代码

```python
# 使用 SQLite

import sqlite3


def print_rows(title, rows):
    print(title)
    for row in rows:
        print(dict(row))


# :memory: 表示创建内存数据库，程序结束后自动消失，适合教程演示。
with sqlite3.connect(":memory:") as conn:
    # row_factory 要在创建 cursor 前设置，这样查询结果才能按列名访问。
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    print("=== 创建表 ===")
    cursor.execute(
        """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
        """
    )
    print("users")

    print("\n=== 插入和批量插入 ===")
    cursor.execute(
        "INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
        ("Alice", 25, "alice@example.com"),
    )
    print(cursor.lastrowid)

    users = [
        ("Bob", 30, "bob@example.com"),
        ("Charlie", 28, "charlie@example.com"),
        ("Diana", 22, "diana@example.com"),
    ]
    cursor.executemany("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", users)

    # with conn: 正常结束会自动 commit。

    print("\n=== 查询数据 ===")
    cursor.execute("SELECT id, name, age FROM users ORDER BY id")
    print_rows("所有用户:", cursor.fetchall())

    print("\n=== 参数化查询 ===")
    min_age = 26
    cursor.execute("SELECT name, age FROM users WHERE age >= ? ORDER BY age", (min_age,))
    print_rows("年龄大于等于 26:", cursor.fetchall())

    print("\n=== 更新和删除 ===")
    cursor.execute("UPDATE users SET age = ? WHERE name = ?", (26, "Alice"))
    cursor.execute("DELETE FROM users WHERE name = ?", ("Diana",))
    cursor.execute("SELECT name, age FROM users ORDER BY id")
    print_rows("更新后:", cursor.fetchall())

    # 先提交前面的正常修改，后面的回滚示例才不会影响已完成的数据。
    conn.commit()

    print("\n=== 防 SQL 注入 ===")
    user_input = "Alice' OR 1=1 --"

    # 参数化查询会把输入当作普通值，不会拼进 SQL 结构里。
    cursor.execute("SELECT COUNT(*) AS count FROM users WHERE name = ?", (user_input,))
    print(cursor.fetchone()["count"])

    print("\n=== 事务回滚 ===")
    try:
        with conn:
            cursor.execute(
                "INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
                ("Eve", 35, "eve@example.com"),
            )
            # 故意制造唯一约束错误，触发整个 with conn 事务回滚。
            cursor.execute(
                "INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
                ("Evil Twin", 36, "eve@example.com"),
            )
    except sqlite3.IntegrityError as error:
        print(type(error).__name__)

    cursor.execute("SELECT name FROM users WHERE email = ?", ("eve@example.com",))
    print(cursor.fetchall())

    print("\n=== 按列名访问 Row ===")
    cursor.execute("SELECT * FROM users WHERE name = ?", ("Alice",))
    row = cursor.fetchone()
    print(row["name"])
    print(row["age"])
```

## 🔍 师兄给你拆开讲

`sqlite3.connect(":memory:")` 创建内存数据库。真实项目里可以传文件路径，例如 `sqlite3.connect("app.db")`，这个文件就是数据库。

SQL 里的 `?` 是占位符，参数通过第二个参数传入。永远不要用字符串拼接 SQL，尤其是用户输入。参数化查询会把输入当普通值处理，不会让它变成 SQL 语法的一部分。

`executemany()` 适合批量插入多行。`cursor.lastrowid` 可以拿到刚插入行的自增 ID。

`conn.commit()` 提交事务。`with conn:` 正常结束会自动提交，发生异常会自动回滚。示例里先手动 `commit()` 前面的正常修改，再故意插入重复邮箱触发回滚，这样回滚只影响 `with conn:` 里的 Eve。

`conn.row_factory = sqlite3.Row` 要在创建 cursor 前设置。这样 `fetchone()` 返回的行既像元组，也能用 `row["name"]` 按列名访问。

## 🏃 跑一下试试

```bash
cd 60-database-sqlite
python database-sqlite.py
```

输出：

```text
=== 创建表 ===
users

=== 插入和批量插入 ===
1

=== 查询数据 ===
所有用户:
{'id': 1, 'name': 'Alice', 'age': 25}
{'id': 2, 'name': 'Bob', 'age': 30}
{'id': 3, 'name': 'Charlie', 'age': 28}
{'id': 4, 'name': 'Diana', 'age': 22}

=== 参数化查询 ===
年龄大于等于 26:
{'name': 'Charlie', 'age': 28}
{'name': 'Bob', 'age': 30}

=== 更新和删除 ===
更新后:
{'name': 'Alice', 'age': 26}
{'name': 'Bob', 'age': 30}
{'name': 'Charlie', 'age': 28}

=== 防 SQL 注入 ===
0

=== 事务回滚 ===
IntegrityError
[]

=== 按列名访问 Row ===
Alice
26
```

## 💡 师兄的提醒

SQLite 很适合桌面应用、小网站、脚本工具、本地缓存、测试环境。高并发写入、大型分布式系统、复杂权限和运维需求，一般会考虑 PostgreSQL、MySQL 等数据库。

数据库代码里最重要的习惯：参数化查询、清楚事务边界、及时关闭连接或使用上下文管理器。

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `sqlite3.connect()` | 连接或创建 SQLite 数据库 |
| `:memory:` | 创建内存数据库 |
| `cursor.execute()` | 执行 SQL |
| `?` 占位符 | 参数化查询，防 SQL 注入 |
| `executemany()` | 批量执行 SQL |
| `fetchone()` / `fetchall()` | 获取查询结果 |
| `commit()` | 提交事务 |
| `with conn:` | 自动提交或回滚事务 |
| `sqlite3.Row` | 支持按列名访问结果 |
| `IntegrityError` | 约束冲突等完整性错误 |

## ➡️ 下一关

下一关：[WSGI 接口](../61-wsgi/README.md)。
