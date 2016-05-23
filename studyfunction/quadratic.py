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
if __name__=='__main__':
    a =3
    b =10
    c =5
    print '求解方程：(%s)*x^2+(%s)x+(%s)=0'%(a,b,c)
    quadratic(a,b,c)
