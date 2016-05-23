# -*- coding: utf-8 -*-
# for x in .. 循环把每个元素带入变量x
names = ['Michael','Bob','Tracy']
for name in names:
    print(name)
sum = 0
for x in range(101):
    sum =sum + x

print(sum)
L = ['Bart', 'Lisa','Adam']
for name in L :
    print ("hello %s" %name)
# python 内置字典dict和set
d = {'Michael':95,'Bob':75,'Tracy':85}
print d.get('Bob')
# set 是一组key 的集合，不存储value 不能有重复 无序
s = set([1,1,2,2,3,3])
s.add(4)
print s
# 对于不变对象来说，调用对象自身的任意方法都不会改变自身本身，而是穿件一个新的对象
a =['c','b','a']
a.sort()
print a
stra = 'abc'
b = stra.replace('a','A')
print stra
print max(1,10,23,100)
def my_abs(x):
    if  x> 0:
        return x
    else:
        return -x
print my_abs(-100)
print 'hello word',stra
