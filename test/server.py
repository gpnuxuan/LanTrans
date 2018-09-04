#coding:utf-8
"""
@author:xuan
@file: server.py
@time: 2018/08/29
"""
# _*_ coding:utf-8 _*_

from socket import *
import threading

def send():
    # 获取本机计算机名称
    hostname = gethostname()
    # 获取本机ip
    ip = gethostbyname(hostname)
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST,1)
    PORT = 10001
    network = '<broadcast>'
    while True:
        s.sendto('0x00:{}'.format(ip).encode('utf-8'), (network, PORT))

def tcplink(skt,addr):
    print(skt)
    print(addr,"已经连接上...")
    print('开始接收文件')
    with open('test.txt', 'wb') as f:
        while True:
            data = skt.recv(1024)
            if not data:
                break;
            f.write(data)
    f.close()
    skt.close()
    print('接收完成')

def server():
    hostname = gethostname()
    # 获取本机ip
    HOST = gethostbyname(hostname)
    PORT = 23333
    ADDR = (HOST,PORT)
    server = socket(AF_INET,SOCK_STREAM)
    server.bind(ADDR)
    server.listen(5)

    while True:
        print("等待连接...")
        skt,addr = server.accept()
        t1=threading.Thread(target=tcplink,args=(skt,addr))
        t1.start()
        t1.join()
    server.close()

if __name__=='__main__':
    while True:
       server=threading.Thread(target=server,args=())
       send=threading.Thread(target=send,args=())
       server.start()
       send.start()
       server.join()
       send.join()
