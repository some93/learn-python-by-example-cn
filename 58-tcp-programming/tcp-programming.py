# TCP 编程

import socket
import threading
from queue import Queue


def recv_line(conn):
    """读取到换行符为止，演示 TCP 字节流需要自己定义消息边界。"""
    chunks = []
    while True:
        chunk = conn.recv(1024)
        if not chunk:
            break
        chunks.append(chunk)
        if b"\n" in chunk:
            break
    return b"".join(chunks).decode("utf-8").strip()


def tcp_server(port_queue, server_logs):
    # SOCK_STREAM 表示 TCP；with 会在退出时自动关闭 socket。
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 端口传 0 表示让系统分配空闲端口。
        server.bind(("127.0.0.1", 0))
        server.listen(1)

        port = server.getsockname()[1]
        port_queue.put(port)

        conn, _addr = server.accept()
        with conn:
            message = recv_line(conn)
            server_logs.put(f"服务器收到: {message}")

            # sendall 会尽力把全部字节发送出去，比 send 更适合教学示例。
            conn.sendall(f"ACK: {message}\n".encode("utf-8"))
            server_logs.put("服务器已回复")


def tcp_client(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        # connect 建立 TCP 连接，连接成功后才能 send/recv。
        client.connect(("127.0.0.1", port))

        # TCP 传输的是 bytes，字符串要先 encode。
        client.sendall("Hello, TCP Server!\n".encode("utf-8"))

        # recv 读到的也是 bytes，需要 decode 回字符串。
        return recv_line(client)


if __name__ == "__main__":
    port_queue = Queue()
    server_logs = Queue()

    server_thread = threading.Thread(target=tcp_server, args=(port_queue, server_logs))
    server_thread.start()

    # 等服务器把端口号放进队列，确保客户端不会抢跑。
    port = port_queue.get()

    print("=== TCP 客户端连接服务器 ===")
    response = tcp_client(port)
    print(f"客户端收到: {response}")

    server_thread.join()

    print("\n=== TCP 服务器处理结果 ===")
    while not server_logs.empty():
        print(server_logs.get())

    print("\n通信完成")
