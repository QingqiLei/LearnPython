# -*- coding: utf-8 -*-

print("hello", "world")  # the coma will be replaced by a writespace
print(100 + 200)
# name = input()
# print("hello", name)
t = 0x10
print(t)
t = 1.2e-5
print(t)
print("I\'m "
      "OK.")
print(True and False)
print(5 > 3 and 3 > 1)
print(None)

print(10/3, 10//3)
print(ord("中"))
x = b'abc'
print(len(x))
# %d 整数  %f 浮点数  %s 字符串  %x 十六进制整数
print("hello, %s"%'world')
print('growth rate: %d %%' % 7)

print ("His name is %s"%("Aviad"))
print ("He is %d years old"%(25))
print ("His height is %f m"%(1.83))
print ("His height is %.2f m"%(1.83))
print ("Name:%10s Age:%8d Height:%8.2f"%("Aviad",25,1.83))
print ("Name:%-10s Age:%-8d Height:%-8.2f"%("Aviad",25,1.83))
print ("Name:%-10s Age:%08d Height:%08.2f"%("Aviad",25,1.83))
print(format(0.0015,'.2e'))
