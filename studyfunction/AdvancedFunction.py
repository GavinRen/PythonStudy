# -*- coding: utf-8 -*-
from collections import Iterable
if __name__=='__main__':
    L =['Michael','Sarah','Trancy','Bob','Jack']
    # 切片 L[0:3]表示从索引0开始取，直到索引3为止，但不包括索引3
    print L[:-1]
    L1 = list(range(100))
    # [-10::2] 表示每隔2个取一个数
    print L1[-10::2]
    # 迭代
    d = {'a':1, 'b':2, 'c':3}
    for key in d:
        print key
    for value in d.values():
        print value
    for ch in 'ABC':
        print ch
    print isinstance(123,Iterable)
    for i in enumerate(['A','B','C']):
        print i
    L2 =[x * x for x in range(1,11) if x % 2 ==0 ]
    # 生成器
    g = (x * x for x in range(10))
    for x in g :
        print x
    print L2
   # 定义生成器的第二种方法 斐波那契数列
    def fib(max):
        n ,a, b =0,0,1
        while n <max:
            yield b
            a, b =b, a + b
            n = n + 1
    for x in fib(8):
        print x
    # 输出杨辉三角
    def triangles(n):
        L = [1]
        yield L
        L = [1,1]
        yield L
        while len(L)< n :
            L =[1]+[L[i]+L[i+1] for i in range(len(L)-1)] + [1]
            yield L
    def pascals_triangle(n):
        x = [[1]]
        for i in range(n - 1):
            x.append([sum(j) for j in zip([0] + x[-1], x[-1] + [0])])
        return x
    g = pascals_triangle(10)
    for n in g:
        print n
    lis=[1]+[1]
    print lis
    for x in pascals_triangle(8):
        print('{0:^64}'.format(x))


