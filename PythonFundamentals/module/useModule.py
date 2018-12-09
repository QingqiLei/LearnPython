#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test module'
__author__ = "lei"
import sys
def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, World')
    elif len(args) ==2:
        print("Hello, %s!" % args[1])
    else :
        print('Too many arguemnts!')
if __name__ == '__main__': # if other python file import this file(useModule), here is false
    test()

# we assume that method or variable starts with _ is private,
# we don't call those directly
def _private_1(name):
    return 'Hello, %s'%name
def _private_2(name):
    return 'Hi, %s'%name
def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

print(greeting('mi'))
print(greeting('micc'))
print(sys.path)
sys.path.append('D:')
