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
    for response in responses:
        print(response)

    print("\n=== UDP 服务器处理结果 ===")
    while not server_logs.empty():
        print(server_logs.get())

    print("\nUDP 通信完成")
