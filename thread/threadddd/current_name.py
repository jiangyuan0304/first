import threading
import time

def worker():
    name = threading.current_thread().getName()
    print("{} :starting".format(name))
    time.sleep(2)
    print("{} :exiting".format(name))

def service():
    name = threading.current_thread().getName()
    print("{} :starting".format(name))
    time.sleep(2)
    print("{} :exiting".format(name))



a = threading.Thread(target=worker, name="Boss")
b = threading.Thread(target=worker)
c = threading.Thread(target=service, name="Boss-service")
# 如果我们对name 参数进行设置的话，就不会使用python默认的thead name
# 默认会根据线程启动的先后来命名

a.start()
b.start()
c.start()