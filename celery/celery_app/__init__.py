# __init__.py 包初始化文件

from celery import Celery

app = Celery('demo')

app.config_from_object('celery_app.celeryconfig') # 通过celery 实例加载配置文件
# def print_name():
#    print("jiangyuan is so clever")


@app.task
def add(x, y):
    print('Enter call function ...')
    return x + y

@app.task
def multiply(x, y):
    print('Enter call function ...')
    return x * y
