# 第 59 关：UDP 编程（师兄带你学 Python）

## 🎯 这一关你会学到

- UDP 和 TCP 的核心区别
- 如何用 `SOCK_DGRAM` 创建 UDP socket
- `sendto()` / `recvfrom()` 如何收发数据报
- 为什么 UDP 不需要 `listen()` / `accept()`
- UDP 的数据报边界和超时处理
- UDP 适合哪些场景，不适合哪些场景

## 🤔 先想一个问题

如果 TCP 像打电话，UDP 更像寄明信片：不需要先建立连接，直接把数据发出去。速度快、开销小，但不保证一定到达，也不保证顺序。

DNS 查询、视频通话、在线游戏位置同步常用 UDP，因为它们更看重低延迟。偶尔丢一帧画面，比等到画面卡住更能接受。

## 📖 看代码

```python
# UDP 编程

import socket
import threading
from queue import Queue


def udp_server(port_queue, server_logs):
    # SOCK_DGRAM 表示 UDP，UDP 不需要 listen/accept。
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
        server.bind(("127.0.0.1", 0))
        server.settimeout(3)

        port = server.getsockname()[1]
        port_queue.put(port)

        for _ in range(3):
            # recvfrom 每次收到一个完整数据报，同时拿到发送方地址。
            data, address = server.recvfrom(1024)
            message = data.decode("utf-8")
            server_logs.put(f"服务器收到: {message}")

            reply = f"ACK: {message}".encode("utf-8")
            server.sendto(reply, address)


def udp_client(port):
    responses = []

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
        client.settimeout(3)
        server_address = ("127.0.0.1", port)

        for message in ["Hello", "World", "UDP"]:
            # UDP 无连接，直接把数据报发给目标地址。
            client.sendto(message.encode("utf-8"), server_address)

            data, _address = client.recvfrom(1024)
            responses.append(data.decode("utf-8"))

    return responses


if __name__ == "__main__":
    port_queue = Queue()
    server_logs = Queue()

    server_thread = threading.Thread(target=udp_server, args=(port_queue, server_logs))
    server_thread.start()

    # 等服务器绑定端口后，客户端再开始发送。
    port = port_queue.get()
    responses = udp_client(port)

    server_thread.join()

    print("=== UDP 客户端响应 ===")
    for response in responses:        # 依次输出：ACK: Hello / ACK: World / ACK: UDP
        print(response)

    print("\n=== UDP 服务器处理结果 ===")
    while not server_logs.empty():    # 依次输出：服务器收到: Hello / 服务器收到: World / 服务器收到: UDP
        print(server_logs.get())

    print("\nUDP 通信完成")  # UDP 通信完成
```

## 🔍 师兄给你拆开讲

`socket.SOCK_DGRAM` 表示 UDP。UDP 没有连接建立过程，所以服务端不需要 `listen()` 和 `accept()`，客户端也不需要 `connect()`，直接 `sendto(data, address)`。

`recvfrom()` 返回两个值：收到的数据和发送方地址。因为 UDP 无连接，服务端要靠这个地址知道该回复给谁。

和 TCP 字节流不同，UDP 保留数据报边界。客户端 `sendto()` 一次发出一个数据报，服务端 `recvfrom()` 一次收到一个数据报。这个边界是 UDP 的优势之一。

但 UDP 不可靠。数据可能丢失、重复、乱序。示例里用 `settimeout(3)` 避免收不到响应时永远卡住。真实项目如果需要可靠性，要自己加序号、重试、确认机制，或者直接选择 TCP。

端口传 `0` 表示系统自动分配空闲端口，避免教程示例和本机已有服务冲突。

## 🏃 跑一下试试

```bash
cd 59-udp-programming
python udp-programming.py
```

输出：

```text
=== UDP 客户端响应 ===
ACK: Hello
ACK: World
ACK: UDP

=== UDP 服务器处理结果 ===
服务器收到: Hello
服务器收到: World
服务器收到: UDP

UDP 通信完成
```

## 💡 师兄的提醒

简单说：需要可靠、有序、完整传输，优先 TCP；需要低延迟、能接受少量丢包，才考虑 UDP。

UDP 常见在 DNS、音视频、游戏同步、局域网广播发现等场景。普通 Web API、数据库连接、文件传输通常不会直接用 UDP。

## 🎓 这一关的知识点清单

| 知识点 | 说明 |
|--------|------|
| `SOCK_DGRAM` | UDP socket 类型 |
| `bind()` | 服务端绑定本地地址 |
| `sendto(data, addr)` | 发送 UDP 数据报 |
| `recvfrom(size)` | 接收数据报和发送方地址 |
| `settimeout()` | 设置收发超时，避免卡死 |
| 数据报边界 | UDP 一次发送对应一个数据报 |
| 无连接 | UDP 不需要 `connect/listen/accept` |
| 不可靠 | 不保证到达、顺序、唯一 |

## ➡️ 下一关

下一关：[使用 SQLite](../60-database-sqlite/README.md)。
