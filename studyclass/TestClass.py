# -*- coding: utf-8 -*-
class Strudent(object):
    # self 指向创建的实例本身 当有__init__ 方法的时候不能传入空的参数，必须传入与__init__方法匹配的参数，self不需要传
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print_score(self):
        print('%s:%s'%(self.__name,self.__score))
    def get__name(self):
        return self.__score()
    def get__score(self):
        return self.__score
