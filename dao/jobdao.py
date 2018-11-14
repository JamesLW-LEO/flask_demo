from .basedao import BaseDAO
from logger.syslogger import logger
from entity.jobdata import JobData


class JobDAO(BaseDAO):
    # 查询全部的信息
    def getAllJobInfo(self):
        try:
            super().getConnection()
            sqlSelect1 = "select * from t_jobdata order by jobMinsalary desc"
            result = super().fetchall(sqlSelect1)
            super().commit()
            return result
        except Exception as e:
            logger.error("执行SQL：" + sqlSelect1 + " 出现异常，params:" + str(e))
        finally:
            super().close()
        pass

    def getJobByAreaAndMs(self, jobdata):
        try:
            super().getConnection()
            sqlSelect2 = "select * from t_jobdata where jobArea = %s and jobMinsalary >= %s order by jobMinsalary desc"
            params = (jobdata.area, jobdata.minsalary)
            result = super().fetchall(sqlSelect2, params)
            super().commit()
            # print(sqlSelect2)
            return result
        except Exception as e:
            logger.error("执行SQL：" + sqlSelect2 + " 出现异常，params:" + str(e))
        finally:
            super().close()
        pass

    def getJobBySalary(self, jobdata):
        try:
            super().getConnection()
            sqlSelect3 = "select * from t_jobdata where jobMinsalary >= %s order by jobMinsalary desc"
            params = (jobdata.minsalary,)
            result = super().fetchall(sqlSelect3, params)
            super().commit()
            return result
        except Exception as e:
            logger.error("执行SQL：" + sqlSelect3 + " 出现异常，params:" + str(e))
        finally:
            super().close()
        pass

    def getJobByArea(self, jobdata):
        try:
            super().getConnection()
            sqlSelect4 = "select * from t_jobdata where jobArea = %s order by jobMinsalary desc"
            params = (jobdata.area,)
            result = super().fetchall(sqlSelect4, params)
            super().commit()
            return result
        except Exception as e:
            logger.error("执行SQL：" + sqlSelect4 + " 出现异常，params:" + str(e))
        finally:
            super().close()
        pass

    def getJobByPos(self, jobdata):
        try:
            super().getConnection()
            sqlSelect5 = "select * from t_jobdata where jobPosition like '%{0}%' order by jobMinsalary desc".format(jobdata.position)
            result = super().fetchall(sqlSelect5)
            super().commit()
            return result
        except Exception as e:
            logger.error("执行SQL：" + sqlSelect5 + " 出现异常，params:" + str(e))
        finally:
            super().close()
        pass

    def getJobByPosAndSalary(self, jobdata):
        try:
            super().getConnection()
            print(jobdata.position)
            print(jobdata.minsalary)
            sqlSelect6 = "select * from t_jobdata where jobPosition like '%{0}%'and jobMinsalary >= {1} order by jobMinsalary desc".format(
                jobdata.position, jobdata.minsalary)
            result = super().fetchall(sqlSelect6)
            super().commit()
            return result
        except Exception as e:
            logger.error("执行SQL：" + sqlSelect6 + " 出现异常，params:" + str(e))
        finally:
            super().close()
        pass

    def getJobByPosAndArea(self, jobdata):
        try:
            super().getConnection()
            # print(jobdata.position, str(jobdata.area))
            sqlSelect7 = "select * from t_jobdata where jobPosition like '%{0}%'and jobArea = '{1}' order by jobMinsalary desc".format(
                jobdata.position, jobdata.area)
            result = super().fetchall(sqlSelect7)
            super().commit()
            return result
        except Exception as e:
            logger.error("执行SQL：" + sqlSelect7 + " 出现异常，params:" + str(e))
        finally:
            super().close()
        pass

    def getJobByInput(self, jobdata):
        try:
            super().getConnection()
            # print(jobdata.position, str(jobdata.area))
            sqlSelect8 = "select * from t_jobdata where jobPosition like '%{0}%'and jobArea = '{1}' and jobMinsalary >= '{2}'".format(
                jobdata.position, jobdata.area, jobdata.minsalary)
            result = super().fetchall(sqlSelect8)
            super().commit()
            return result
        except Exception as e:
            logger.error("执行SQL：" + sqlSelect8 + " 出现异常，params:" + str(e))
        finally:
            super().close()
        pass

    def getPos(self):
        try:
            super().getConnection()
            sqlpos = "select jobPosition,jobArea,min(jobMinsalary),max(jobMaxsalary),count(jobArea) from t_jobdata where jobPosition ='python开发工程师' group by jobArea order by count(jobArea) desc;"
            result = super().fetchall(sqlpos)
            super().commit()
            # print(result)
            return result
        except Exception as e:
            logger.error("执行SQL：" + sqlpos + " 出现异常，params:" + str(e))
        finally:
            super().close()
        pass

    def getSalary(self):
        try:
            super().getConnection()
            sqlpos = "select jobPosition,jobCompany,jobArea,jobMinsalary from t_jobdata order by jobMinsalary desc limit 10;"
            result = super().fetchall(sqlpos)
            super().commit()
            return result
        except Exception as e:
            logger.error("执行SQL：" + sqlpos + " 出现异常，params:" + str(e))
        finally:
            super().close()
        pass

    def getArea(self):
        try:
            super().getConnection()
            sqlarea = "select * from t_jobdata where jobArea='海淀区' order by jobMinsalary desc limit 10;"
            result = super().fetchall(sqlarea)
            super().commit()
            print(result)
            return result
        except Exception as e:
            logger.error("执行SQL：" + sqlarea + " 出现异常，params:" + str(e))
        finally:
            super().close()
        pass
