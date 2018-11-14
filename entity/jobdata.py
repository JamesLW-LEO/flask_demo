class JobData():
    def __init__(self):
        self.__position = None
        self.__area = None
        self.__minsalary = None

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        self.__area = area

    @property
    def minsalary(self):
        return self.__minsalary

    @minsalary.setter
    def minsalary(self, minsalary):
        self.__minsalary = minsalary
