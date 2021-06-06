
from celery_app import add 	# 在这里我只调用了task1

if __name__ == '__main__':
    print("Start Task ...")
    re = add.delay(111, 5)
    print(re.id)
    print(re.status)
    print(re.get())
    print("End Task ...")
