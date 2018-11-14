class User():
    def __init__(self):
        self.__username = None
        self.__userpawd = None
        self.__usersex = None
        self.__userage = None
        self.__useremail = None
        self.__userbirth = None

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def userpawd(self):
        return self.__userpawd

    @userpawd.setter
    def userpawd(self, userpawd):
        self.__userpawd = userpawd

    @property
    def usersex(self):
        return self.__usersex

    @usersex.setter
    def usersex(self, usersex):
        self.__usersex = usersex

    @property
    def userage(self):
        return self.__userage

    @userage.setter
    def userage(self, userage):
        self.__userage = userage

    @property
    def useremail(self):
        return self.__useremail

    @useremail.setter
    def useremail(self, useremail):
        self.__useremail = useremail

    @property
    def userbirth(self):
        return self.__userbirth

    @userbirth.setter
    def userbirth(self, userbirth):
        self.__userbirth = userbirth

    pass
