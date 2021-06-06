# from abs_path import logger_handler
#
# logger_handler().logger.info("jiangyuan")

# import logging
#
# logger = logging.getLogger()
# logger.setLevel(level=logging.DEBUG)
#
#
# file_log = logging.FileHandler("./log.txt", mode="a")
# file_log.setFormatter(logging.Formatter('%(message)s'))
# # Formatter 还是logging的方法
# # logging格式看看
#
# logger.addHandler(file_log)

#
# if __name__ == "__main__":
#     logger.info("jiangyuan is so clever")


# g = lambda x : print(x.strip())
# #  lambda 后面是参数，, 冒号后面定义相当与方法里面的执行步骤 ，g 呢就是方法名
# g("  jiang is so   ")

with open("./log.txt", 'r') as f :
    for i in f.readlines():
        print(i.rstrip("\n"))

