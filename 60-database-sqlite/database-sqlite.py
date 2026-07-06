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
