# -*- coding: utf-8 -*-
def f(x):
    return x * x
def fn(x,y):
    return x *10 + y
def char2num(s):
    return {'0': 0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
def tolower(s):
    return s.lower()
def is_odd(n):
    return n % 2 == 1
# 产生奇数列
def _odd_iter():
    n =1
    while True:
        n = n+2
        yield n
# 筛选函数
def _not_divisible(n):
    return lambda x : x %n >0
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n =next(it)
        yield n
        it = filter(_not_divisible(n),it)

if __name__ =='__main__':
    # map 函数 接收两个参数，一个是函数，一个是Iterable ,map 讲传入的函数依次作用到序列的每个元素，并作为新的Iterator 返回
    m =map(f,[1,2,3,4,5,6,7,8,9])
    list(m)
    # filter()把传入的函数一次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
    r = reduce(fn,map(char2num,'13579'))
    print r
    L1 =['adam','LISA','barT']
    L2=map(tolower,L1)
    print list(L2)
    L3 =list(filter(is_odd,[1,2,3,4,5,6,9,10,15]))
    print L3
    for n in primes():
        if n<100:
            print n
        else:
            break
