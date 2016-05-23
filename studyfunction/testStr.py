# -*- coding: utf-8 -*-
print "I love %s"%'hehe'
print "shi is %d years old" % 14
# list
classmates =["liming","bob","chengkun"]
print len(classmates)
classmates.append("tomxie")
print classmates[-2]
# tuble
teachers =("xia","feng","guo")
L = [
    ['Apple','google','Microsoft'],
    ['java','python','Rubby','PHP'],
    ['Adam','Bart','List']
]
print (L[0][0])
print (L[1][1])
print L[2][2]
age = 1
if  age >18:
    print('your age is %d'%age)
    print('adult')
else:
    print('your age is %d'%age)
    print('teenager')
if age >18 :
    print "adult"
elif age >6 :
    print "teenager"
else:
    print "kid"
height =1.75
weight =80.5
bmi = weight / (height ** 2)
if  bmi >32 :
    print ('严重肥胖')
elif bmi >28 :
    print "肥胖"
elif bmi >25 :
    print "过重"
elif bmi >18.5:
    print "正常"
else :
    print "过轻"
