# _*_ coding =utf-8 _*_
'a test module'
__author__ ='gavin'

import sys
def test():
    args=sys.argv
    if  len(args) ==1:
        print("Hello ,world!")
    elif len(args)==2:
        print ("Hello,%s!"% args[1])
    else:
        print ('too mang arguments')
if __name__=='__main__':
    test()
