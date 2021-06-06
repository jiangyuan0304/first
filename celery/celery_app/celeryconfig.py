# celeryconfig.py

from datetime import timedelta
from celery.schedules import crontab

# 参数配置文件celeryconfig.py
BROKER_URL = 'redis://192.168.203.128:6379/1'
CELERY_RESULT_BACKEND = 'redis://192.168.203.128:6379/2'
CELERY_TIMEZONE = "Asia/shanghai" #默认UTC
# CELERY_RESULT_SERIALIZER = 'msgpack'
CELERY_RESULT_SERIALIZER = 'msgpack'
CELERY_ACCEPT_CONTENT = ['msgpack', 'json', 'pickle']
#
# CELERY_ACCEPT_CONTENT = ['json'],
# CELERY_TASK_SERIALIZER = 'json',
# CELERY_RESULT_SERIALIZER = 'json',

# 导入指定的任务模块
CELERY_IMPORTS = (
    'celery_app',
    # 'celery_app.task2',
)

# 设置定时任务
CELERYBEAT_SCHEDULE = {
    # 每过10秒执行以下task1.add的定时任务
    'task1':{
        'task': 'celery_app.add',
        'schedule': timedelta(seconds=10),
        'args': (2, 8)
    },
    # 等到22点18分执行task2的multiply
    'task2': {
        'task': 'celery_app.multiply',
        'schedule': crontab(hour=22, minute=20),
        'args': (4, 5)
    }
}
