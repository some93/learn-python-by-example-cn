# 第 58 关：TCP编程（师兄带你学 Python）

## 🎯 这一关你会学到

- 理解 TCP 协议的特点
- 用 `socket` 编写 TCP 服务器
- 用 `socket` 编写 TCP 客户端
- 实现简单的客户端-服务器通信

## 🤔 先想一个问题

你打电话给朋友：先拨号（connect），对方接听（accept），然后你们对话（send/recv），最后挂断（close）。TCP 编程就像打电话，是面向连接的可靠通信。

带着这个问题，我们来看代码。

## 📖 看代码

```python
# TCP 编程

import socket
import threading

# ===== TCP 客户端 =====
def tcp_client():
    # 创建 TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务器
    s.connect(('127.0.0.1', 9999))
    print(f"[客户端] 已连接到服务器")

    # 发送数据
    s.send(b'Hello, Server!')

    # 接收响应
    data = s.recv(1024)
    print(f"[客户端] 收到: {data.decode('utf-8')}")

    # 关闭连接
    s.close()

# ===== TCP 服务器 =====
def handle_client(conn, addr):
    print(f"[服务器] 新连接: {addr}")
    data = conn.recv(1024)
    print(f"[服务器] 收到: {data.decode('utf-8')}")
    conn.send(f"你好！收到了你的消息: {data.decode('utf-8')}".encode('utf-8'))
    conn.close()

def tcp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 9999))
    s.listen(5)
    print("[服务器] 等待连接...")

    conn, addr = s.accept()
    handle_client(conn, addr)
    s.close()

# 演示：先启动服务器，再启动客户端
if __name__ == '__main__':
    import time

    server = threading.Thread(target=tcp_server)
    server.start()
    time.sleep(0.5)    # 等服务器启动

    client = threading.Thread(target=tcp_client)
    client.start()

    server.join()
    client.join()
    print("通信完成！")

# TCP 要点：
# 1. 面向连接：先 connect，再 send/recv
# 2. 可靠传输：数据不会丢失，顺序不会乱
# 3. 服务器：bind → listen → accept → recv/send
# 4. 客户端：connect → send/recv
```

## 🔍 师兄给你逐行拆

> 代码已经在注释中做了详细说明，这里挑重点讲。

### 核心要点

- TCP 是面向连接的：先 connect，数据传输可靠有序
- 服务器流程：socket → bind → listen → accept → recv/send → close
- 客户端流程：socket → connect → send/recv → close
- `AF_INET` 是 IPv4，`SOCK_STREAM` 是 TCP
- 实际项目不会直接用 socket，而是用 Web 框架（Flask/Django）

## 🏃 跑一下试试

```bash
cd 58-tcp-programming
python tcp-programming.py
```

## 💡 师兄的碎碎念

- TCP 是面向连接的：先 connect，数据传输可靠有序
- 服务器流程：socket → bind → listen → accept → recv/send → close
- 客户端流程：socket → connect → send/recv → close
- `AF_INET` 是 IPv4，`SOCK_STREAM` 是 TCP
- 实际项目不会直接用 socket，而是用 Web 框架（Flask/Django）

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `socket.socket(AF_INET, SOCK_STREAM)` | 创建 TCP socket |
| `s.bind((host, port))` | 绑定地址 |
| `s.listen(n)` | 开始监听，n 为等待队列长度 |
| `s.accept()` | 接受连接，返回 (conn, addr) |
| `s.connect((host, port))` | 连接服务器 |
| `conn.send/recv` | 发送/接收数据 |

## ➡️ 下一关

下一关我们学习 [UDP编程](../59-udp-programming/README.md)，继续加油！
