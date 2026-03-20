# 测试端口连通性
import socket


def check_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception:
        return False


print("端口检测：")
print(f"smtp.163.com:465 → {'开放' if check_port('smtp.163.com', 465) else '关闭'}")
print(
    f"smtphz.qiye.163.com:465 → {
        '开放' if check_port('smtphz.qiye.163.com', 465) else '关闭'
    }"
)
