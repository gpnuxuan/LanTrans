#coding:utf-8
"""
@author:xuan
@file: client.py
@time: 2018/08/29
"""
# _*_ utf-8 _*_

from socket import *
import datetime


def recv():
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

    PORT = 10001

    s.bind(('', PORT))
    print('Listening for broadcast at ', s.getsockname())

    while True:
        data, address = s.recvfrom(65535)
        recv_data=data.decode('utf-8')
        flag=recv_data.split(':')[0]
        ip=recv_data.split(':')[1]
        if flag=='0x00':
            break
    print(ip)
        #print('Server received from {}:{}'.format(address, data.decode('utf-8')))
    client(ip)


def client(ip):
    HOST = ip
    PORT = 23333
    ADDR = (HOST,PORT)
    print(ADDR)
    client = socket(AF_INET,SOCK_STREAM)
    client.connect(ADDR)
    start=datetime.datetime.now()
    send_data=''
    with open("数据.txt","r") as f:
        for data in f.readlines():
            send_data=send_data+data
        data=send_data*800
        client.send(data.encode())


    end=datetime.datetime.now()
    #f.close()
    client.close()
    print("发送完毕,用时：",end-start)

if __name__=='__main__':
    recv()