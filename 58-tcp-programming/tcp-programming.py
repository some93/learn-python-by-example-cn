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
