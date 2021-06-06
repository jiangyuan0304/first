# import os
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# # 会根据windows 和linux系统的不同显示不同的路径分隔符，是反斜杠还是斜杠
# # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(__file__)
# print(os.path.join("/allpython/django/", "yuan/", "wang"))


# print("www.baidu.com.con".split(".", 2)[1])
# # 分隔零次还是原来的字符 ，上面是分隔一次
# print("www.baidu.com.con".split(".", -1))
# # -1 和不加参数的效果是一样的都是最大化的分隔
# a, b, c = [1,2,3]
# print(b)


import sys
import time
import logging
import os.path

class logger_handler(object):
    '''封装后的logging'''
    def __init__(self, logger = None):
        '''
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定的文件中
        '''

        # 第一步，创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)  # Log等级总开关

        # 第二步，创建一个handler，用于写入日志文件
        self.rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        self.log_path = os.path.dirname(os.getcwd()) + 'jiang.txt'
        self.log_name = self.log_path + 'xx_' + self.rq + '.log'
        self.log_name_detail = self.log_path + 'xx_detail_' + self.rq + '.log'
        self.logfile = self.log_name
        self.logfile_detail = self.log_name_detail
        fh = logging.FileHandler(self.logfile, mode='w')
        fh_detail = logging.FileHandler(self.logfile_detail, mode='w')
        fh.setLevel(logging.INFO)  # 输出到file的log等级的开关
        fh_detail.setLevel(logging.INFO)  # 输出到file的log等级的开关
        # ch = logging.StreamHandler()
        # ch.setLevel(logging.INFO)  # 输出到console的log等级的开关

        # 第三步，定义handler的输出格式
        formatter_file = logging.Formatter(
            "[%(asctime)s] %(filename)s->%(funcName)s [line:%(lineno)d] - %(levelname)s: %(message)s")

        formatter_detail = logging.Formatter(
            "[%(asctime)s] %(pathname)s->%(filename)s->%(funcName)s [line:%(lineno)d] - %(levelname)s: %(message)s")

        formatter_console = logging.Formatter(
            "[%(asctime)s] %(pathname)s->%(filename)s->%(funcName)s [line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter_file)
        fh_detail.setFormatter(formatter_detail)
        # ch.setFormatter(formatter_console)

        # 第四步，将logger添加到handler里面
        self.logger.addHandler(fh)
        self.logger.addHandler(fh_detail)
        # self.logger.addHandler(ch)

        # 日志
        self.logger.debug('this is a logger debug message')
        self.logger.info('this is a logger info message')
        self.logger.warning('this is a logger warning message')
        self.logger.error('this is a logger error message')
        self.logger.critical('this is a logger critical message')
        # 2432jdsf
        try:
            open("sklearn.txt", "rb")
        except (SystemExit, KeyboardInterrupt):
            raise
        except Exception:
            self.logger.error("Faild to open sklearn.txt from logger.error", exc_info=True)

        self.logger.info("Finish")

        #  添加下面一句，在记录日志之后移除句柄
        # self.logger.removeHandler(ch)
        # self.logger.removeHandler(fh)
        # 关闭打开的文件
        # fh.close()
        # ch.close()

    def getlog(self):
        return self.logger

if __name__ == '__main__':
    logger_handler().getlog()
