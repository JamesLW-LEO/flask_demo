from .basedao import BaseDAO
from logger.syslogger import logger
from entity.user import User


# 封装用户操作的类
class UserDAO(BaseDAO):
    # 根据用户名和密码进行查询
    def getUserByUserNameAndPwd(self, user):
        try:
            super().getConnection()
            sqlSelect = "select * from t_user where username=%s and userpwd=%s"
            params = (user.username, user.userpawd)
            result = super().fetchone(sqlSelect, params)
            super().commit()
            # print(result)
            return result
        except Exception as e:
            logger.error("执行SQL：" + sqlSelect + " 出现异常，params:" + params + " " + str(e))
        finally:
            super().close()
        pass

    # 查询全部的信息
    def getAllInfo(self):
        try:
            super().getConnection()
            sqlSelect = "select * from t_user "
            result = super().fetchall(sqlSelect)
            super().commit()
            return result
        except Exception as e:
            logger.error("执行SQL：" + sqlSelect + " 出现异常，params:" + str(e))
        finally:
            super().close()
        pass

    pass

    # 注册成功后写入数据库
    def createUser(self, user):
        try:
            super().getConnection()
            sqlInsert = "insert into t_user(username,userpwd,usersex,userage,useremail,userbirth) VALUES (%s,%s,%s,%s,%s,%s)"
            params = (user.username, user.userpawd, user.usersex, user.userage, user.useremail, user.userbirth)
            result = super().execute(sqlInsert, params)
            super().commit()
            return result
            pass
        except Exception as e:
            super().rollback()
            logger.error("执行SQL：" + sqlInsert + " 出现异常，params:" + params + str(e))
            pass
        finally:
            super().close()
            pass
