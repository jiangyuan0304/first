# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# import signal
# import os
# import time
#
# def receive_signal(signum, stack):
#     """用于接收信号，对signum的值区分信号，实现不同的信号做对应的处理"""
#     print('接收的signum', signum)
#
# #注册处理信号的事件，此处对用户定义信号1、用户定义信号2，绑定事件
# signal.signal(signal.SIGABRT, receive_signal)
# signal.signal(signal.SIGABRT, receive_signal)
#
# print('我的PID: %s' % os.getpid())
#
# #开启循环监听信号
# while True:
#     print('Waiting...')
#     time.sleep(3)
#
# # signal_signal.py


# import signal, os, time
#
#
# # def onsignal_term(a, b):
# #     print
# #     '收到SIGTERM信号'
# #
# #
# # def onsignal_quit(a, b):
# #     print
# #     '收到SIGQUIT信号'
#
#
# def onsignal_alrm(a, b):
#     print('收到SIGALRM信号')
#     time.sleep(2)
#     os.kill(os.getegid(), signal.SIGTERM)
#
#
#
# # signal.signal(signal.SIGTERM, onsignal_term)
# # signal.signal(signal.SIGQUIT, onsignal_quit)
# signal.signal(signal.SIGALRM, onsignal_alrm)
# signal.alarm(10)
# while 1:
#     print('进程id：', os.getpid())
#     time.sleep(2)



import  signal

def alarm_received(n, stack):
    return

signal.signal(signal.SIGALRM, alarm_received)

signals_to_names = {
    getattr(signal, n): n for n in dir(signal)
    if n.startswith("SIG") and "_" not in n
}


for s, name in sorted(signals_to_names.items()):
    handler = signal.getsignal(s)
    if handler is signal.SIG_DFL:
        handler = 'SIG_DFL'
    elif handler is signal.SIG_IGN:
        handler = 'SIG_IGN'
    print("{}  {}:".format(name, s), handler)