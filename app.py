from flask import Flask, render_template, request, redirect, session
from entity.user import User
from entity.jobdata import JobData
from dao.userdao import UserDAO
from dao.jobdao import JobDAO
import os
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # 设置为24位的字符,每次运行服务器都是不同的，所以服务器启动一次上次的session就清除。
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)  # 设置session的保存时间。

userDAO = UserDAO()
jobDAO = JobDAO()


@app.route('/', methods=['GET', 'POST'])
def index():
    # if session.get("userName"):
    #     user = User()
    #     user.username = session.get("userName")
    #     render_template('mianInterface.html', user=user)
    # else:
    return render_template('index.html')


# 登录
@app.route('/login', methods=['GET', 'POST'])
def login():
    # 从表单中获取的数据
    userName = request.form['username']
    userPwd = request.form['userpwd']
    if userName != "" and userPwd != "":
        user = User()
        user.username = userName
        user.userpawd = userPwd
        result = userDAO.getUserByUserNameAndPwd(user)
        session["userName"] = userName
        session["userPwd"] = userPwd
    if result:
        return render_template('mianInterface.html', result=result)
    else:
        message = "用户名或密码不能为空！"
        return render_template('index.html', message=message)


# 跳转到注册
@app.route('/register', methods=['GET'])
def register():
    return render_template("register.html")


# 完成注册
@app.route('/registerFn', methods=['GET', 'POST'])
def registerFn():
    userName = request.form['user']
    userPwd = request.form['pass']
    userSex = request.form['sex']
    userAge = request.form['age']
    userEmail = request.form['email']
    userBirth = request.form['year']
    user = User()
    user.username = userName
    user.userpawd = userPwd
    user.usersex = userSex
    user.userage = userAge
    user.useremail = userEmail
    user.userbirth = userBirth
    result = userDAO.createUser(user)
    if result:
        return render_template('registerRE.html')
    if result:
        # print(result)
        message = "注册失败"
        print(message)
        return render_template('register.html')


# 获取工作信息
@app.route('/getjob', methods=['GET', 'POST'])
def getjob():
    position = request.form['pos']
    area = request.form['area']
    minsalary = request.form['minsalary']
    # print(position, area, minsalary)
    n = session["userName"]
    p = session["userPwd"]
    user = User()
    user.username = n
    user.userpawd = p
    jobdata = JobData()
    result = userDAO.getUserByUserNameAndPwd(user)
    # 直接搜索查询所有信息
    if position == "" and area == "北京" and float(minsalary) == 1.5:
        results = jobDAO.getAllJobInfo()
        # print(results)
        if results:
            return render_template('mianInterface.html', results=results, result=result)
    # 职位空 地点薪资不默认
    elif position == "" and area != "北京" and float(minsalary) != 1.5:
        jobdata.area = area
        jobdata.minsalary = float(minsalary)
        results = jobDAO.getJobByAreaAndMs(jobdata)
        if results:
            return render_template('mianInterface.html', results=results, result=result)
        else:
            message = "对不起，没有找到符合你条件的职位！"
            return render_template('mianInterface.html', result=result, message=message)
    # 职位空 地点默认 薪资不默认
    elif position == "" and area == "北京" and float(minsalary) != 1.5:
        jobdata.minsalary = minsalary
        results = jobDAO.getJobBySalary(jobdata)
        if results:
            return render_template('mianInterface.html', results=results, result=result)
        else:
            message = "对不起，没有找到符合你条件的职位！"
            return render_template('mianInterface.html', result=result, message=message)
    # 职位空 地点不默认 薪资默认
    elif position == "" and area != "北京" and float(minsalary) == 1.5:
        jobdata.area = area
        results = jobDAO.getJobByArea(jobdata)
        if results:
            return render_template('mianInterface.html', results=results, result=result)
        else:
            message = "对不起，没有找到符合你条件的职位！"
            return render_template('mianInterface.html', result=result, message=message)
        pass
    # 职位不空 地点默认 薪资默认
    elif position != "" and area == "北京" and float(minsalary) == 1.5:
        jobdata.position = position
        results = jobDAO.getJobByPos(jobdata)
        if results:
            return render_template('mianInterface.html', results=results, result=result)
        else:
            message = "对不起，没有找到符合你条件的职位！"
            return render_template('mianInterface.html', result=result, message=message)
        pass
    # 职位不空 地点默认 薪资不默认
    elif position != "" and area == "北京" and float(minsalary) != 1.5:
        jobdata.position = position
        jobdata.minsalary = float(minsalary)
        results = jobDAO.getJobByPosAndSalary(jobdata)
        if results:
            return render_template('mianInterface.html', results=results, result=result)
        else:
            message = "对不起，没有找到符合你条件的职位！"
            return render_template('mianInterface.html', result=result, message=message)
        pass
    # 职位不空 地点不默认 薪资默认
    elif position != "" and area != "北京" and float(minsalary) == 1.5:
        jobdata.position = position
        jobdata.area = area
        results = jobDAO.getJobByPosAndArea(jobdata)
        if results:
            return render_template('mianInterface.html', results=results, result=result)
        else:
            message = "对不起，没有找到符合你条件的职位！"
            return render_template('mianInterface.html', result=result, message=message)
        pass
    # 职位不空 地点不默认 薪资不默认
    elif position != "" and area != "北京" and float(minsalary) != 1.5:
        jobdata.position = position
        jobdata.area = area
        jobdata.minsalary = float(minsalary)
        results = jobDAO.getJobByInput(jobdata)
        if results:
            return render_template('mianInterface.html', results=results, result=result)
        else:
            message = "对不起，没有找到符合你条件的职位！"
            return render_template('mianInterface.html', result=result, message=message)
        pass
        pass


@app.route('/position', methods=['GET', 'POST'])
def pos():
    n = session["userName"]
    p = session["userPwd"]
    user = User()
    user.username = n
    user.userpawd = p
    result = userDAO.getUserByUserNameAndPwd(user)
    results1 = jobDAO.getPos()
    if results1:
        return render_template('mianInterface.html', results1=results1, result=result)


@app.route('/salary', methods=['GET', 'POST'])
def salary():
    n = session["userName"]
    p = session["userPwd"]
    user = User()
    user.username = n
    user.userpawd = p
    result = userDAO.getUserByUserNameAndPwd(user)
    results2 = jobDAO.getSalary()
    if results2:
        return render_template('mianInterface.html', results2=results2, result=result)


@app.route('/area',methods=['GET','POST'])
def area():
    print("777777777777777777")
    n = session["userName"]
    p = session["userPwd"]
    user = User()
    user.username = n
    user.userpawd = p
    result = userDAO.getUserByUserNameAndPwd(user)
    results3 = jobDAO.getArea()
    if results3:
        return render_template('mianInterface.html', results3=results3, result=result)


# 注销
@app.route('/logout')
def logout():
    return redirect('/')


if __name__ == '__main__':
    app.run()
