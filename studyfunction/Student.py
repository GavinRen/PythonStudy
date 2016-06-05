# _*_ condig =utf-8 _*_
from types import MethodType
class Student(object):
    def __str__(self):
        return "student name:%s score:%s"%(self.__name,self.__score)
    name="Student"
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print_score(self):
        print('%s:%s'%(self.__name,self.__score))
    def set_name(self,name):
        self.__name=name
    def set_score(self,score):
        self.__score=score
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def study(self):
        print ("I am a student,I love studying")
    def get_grade(self):
        if  self.__score>=90:
            return 'A'
        elif self.__score>=60:
            return 'B'
        else:
            return 'C'
    def __len__(self):
        return len(self.__name)
class Pupil(Student):
    def study(self):
        print("I am a pupil,I love studying ,I love enjoying myself too")
class Undergraduate(Student):
    def study(self):
        print ("I am a undergraduate,I love studying ,but I need to find a job ")
if __name__ == '__main__':
    def getStudying(Student):
        Student.study()

    lisa=Student("lili",30)
    xiaoming=Student("xiaoming",90)
    print lisa.name
    print Student.name
    lisa.print_score()
    lisa.get_grade()
    xiaoming.print_score()
    xiaoming.get_grade()
    gavin =Pupil("gavin",100)
    print(isinstance(gavin,Student))
    chenkun = Undergraduate("chenkun",101)
    getStudying(gavin)
    getStudying(chenkun)
    print (dir(gavin))
    print (len(gavin))
    print gavin
