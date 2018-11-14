import pymysql
from logger.syslogger import logger


# 封装数据库访问的基类
class BaseDAO():

    # 1. 封装连接数据库的参数作为属性
    def __init__(self, host='localhost', name='root', pwd='root', port='3306', schema='db_datacollectsys',
                 charset='utf8'):
        self.__host = host
        self.__name = name
        self.__pwd = pwd
        self.__port = port
        self.__schema = schema
        self.__charset = charset
        self.__conn = None
        self.__cursor = None
        pass

    # 2. 封装数据库连接的公有方法（通用的）
    def getConnection(self):
        try:
            self.__conn = pymysql.connect(self.__host, self.__name, self.__pwd, self.__schema, charset=self.__charset)
        except (pymysql.MySQLError, pymysql.DatabaseError, Exception):
            logger.error("数据库连接异常：" + self.__host)
            pass
        self.__cursor = self.__conn.cursor()
        pass

    # 3. 封装一个通用的对数据库进行操作的方法
    def execute(self, sql, params=None, isBatch=False):
        try:
            # self.getConnection()   # 每次连接的是独立的一个连接
            if self.__conn and self.__cursor:
                if params:
                    # print('not None')
                    # print(parms)
                    if isBatch:
                        return self.__cursor.executemany(sql, params)
                        pass
                    else:
                        return self.__cursor.execute(sql, params)
                else:
                    return self.__cursor.execute(sql)
                pass
        except Exception as e:
            logger.error("执行SQL：" + sql + " params：" + str(params)+str(e))
            self.__cursor.close()
            self.__conn.close()
            pass
        pass

    # 4. 封装数据库关闭的方法
    def close(self):
        if self.__cursor and self.__conn:
            self.__cursor.close()
            self.__conn.close()
        pass

    # 5. 封装数据库事务提交的方法
    def commit(self):
        # print("----------")
        self.__conn.commit()
        pass

    # 6. 封装事务回滚的方法
    def rollback(self):
        self.__conn.rollback()
        pass

    # 封装查询全部的方法
    def fetchall(self, sql, params=None):
        self.execute(sql, params)
        return self.__cursor.fetchall()
        pass

    # 封装查询一条记录的方法
    def fetchone(self, sql, params=None):
        self.execute(sql, params)
        return self.__cursor.fetchone()
        pass

    # 封装调用存储过程的方法
    def executeProc(self, sql, params=None):
        try:
            if self.__conn and self.__cursor:
                if params:
                    return self.__cursor.callproc(sql, params)
                else:
                    return self.__cursor.callproc(sql)
                pass
        except:
            logger.error("执行SQL：" + sql + " params：" + str(params))
            self.__cursor.close()
            self.__conn.close()
            pass
        pass

    # 封装执行存储过程的方法
    def fetchproc(self, sql, params=None):
        self.executeProc(sql, params)
        return self.__cursor.fetchall()
        pass
    pass
