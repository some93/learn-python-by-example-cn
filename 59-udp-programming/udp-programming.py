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
