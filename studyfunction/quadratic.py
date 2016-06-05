# -*- coding: utf-8 -*-
import math
def quadratic(a,b,c):
    deltag =b ** 2-4*a*c
    if  deltag < 0:
        print '根的判别式小于0，方程无解'
    elif deltag >0:
        x1 =(-b +math.sqrt(deltag))/(2*a)  # 第一个根
        x2 =(-b -math.sqrt(deltag))/(2*a) # 第二个根
        print '该方程有两个不同的根为：%f\t%f'%(x1,x2)
    else:
        x =-b/(2*a)
        print '该方程只有一个根为：%f'%x
# 函数的位置参数,默认参数为：2 默认参数必须是不可变对象
def power(x,n=2):
    s =1
    while n >0:
        s =s*x
        n=n-1
    return s
# 定义一个参数可变的函数，只需在参数前面加上即可表示参数的个数可变 函数内部其实接收到的是一个tuple
def calc(*number):
    sum =0
    for n in number:
        sum =sum +n **2
    return sum
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在啊还是农户内部自动组装为一个dict字典
def persion(name,age,**kw):
    if  'city' in kw :
        pass
    if 'job' in kw :
        pass
    print 'name:',name,'age:',age,'other:',kw
# 定义函数可以用必选参数、默认参数、可变参数、关键字参数。参数的顺序为：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a,b,c=0,*args,**kw):
    print 'a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw
def fac(n):
    if n ==1:
        return 1
    return n*fac(n-1)
if __name__=='__main__':
    a =3
    b =10
    c =5
    print '求解方程：(%s)*x^2+(%s)x+(%s)=0'%(a,b,c)
    quadratic(a,b,c)
    print power(10,3)
    print power(10)
    print calc(1,2,3,4,5,6,7,)
    persion('jack',24,city='Beijing',addr='Chaoyang',zipcode=123456)
    print f1(1,2,3,d=99,ext =None)
    print fac(6)

