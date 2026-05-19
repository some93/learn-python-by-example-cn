# 第 59 关：UDP编程（师兄带你学 Python）

## 🎯 这一关你会学到

- 理解 UDP 和 TCP 的区别
- 用 `socket` 编写 UDP 服务器/客户端
- 了解 UDP 的适用场景

## 🤔 先想一个问题

TCP 像打电话（可靠但慢），UDP 像发短信（快但可能丢）。视频通话、在线游戏、DNS 查询……这些场景速度比可靠性更重要，所以用 **UDP**。

带着这个问题，我们来看代码。

## 📖 看代码

```python
# UDP 编程

import socket
import threading

# ===== UDP 服务器 =====
def udp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', 9998))
    print("[UDP服务器] 等待数据...")

    for _ in range(3):
        data, addr = s.recvfrom(1024)
        print(f"[UDP服务器] 收到来自 {addr}: {data.decode('utf-8')}")
        s.sendto(f"收到: {data.decode('utf-8')}".encode('utf-8'), addr)

    s.close()

# ===== UDP 客户端 =====
def udp_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for msg in ['Hello', 'World', 'UDP']:
        s.sendto(msg.encode('utf-8'), ('127.0.0.1', 9998))
        data, addr = s.recvfrom(1024)
        print(f"[UDP客户端] 响应: {data.decode('utf-8')}")

    s.close()

if __name__ == '__main__':
    import time

    server = threading.Thread(target=udp_server)
    server.start()
    time.sleep(0.5)

    client = threading.Thread(target=udp_client)
    client.start()

    server.join()
    client.join()
    print("UDP 通信完成！")

# TCP vs UDP：
# TCP：面向连接、可靠、有序、速度慢
# UDP：无连接、不可靠、无序、速度快
# UDP 适合：视频通话、游戏、DNS 查询等
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- UDP 不需要 connect，直接 sendto/recvfrom
- `SOCK_DGRAM` 表示 UDP（TCP 是 `SOCK_STREAM`）
- UDP 不保证数据到达，也不保证顺序
- UDP 没有 listen/accept 步骤，比 TCP 简单
- DNS 查询、视频流、游戏同步等场景常用 UDP

## 🏃 跑一下试试

```bash
cd 59-udp-programming
python udp-programming.py
```

## 💡 师兄的碎碎念

- UDP 不需要 connect，直接 sendto/recvfrom
- `SOCK_DGRAM` 表示 UDP（TCP 是 `SOCK_STREAM`）
- UDP 不保证数据到达，也不保证顺序
- UDP 没有 listen/accept 步骤，比 TCP 简单
- DNS 查询、视频流、游戏同步等场景常用 UDP

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `socket.socket(AF_INET, SOCK_DGRAM)` | 创建 UDP socket |
| `s.sendto(data, addr)` | 发送数据到指定地址 |
| `s.recvfrom(bufsize)` | 接收数据和来源地址 |
| `TCP vs UDP` | 可靠有序 vs 快速无连接 |

## ➡️ 下一关

下一关我们学习 [使用SQLite](../60-database-sqlite/README.md)，继续加油！
