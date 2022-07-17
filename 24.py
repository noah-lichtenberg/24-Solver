#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 20:08:58 2022

@author: noah01px2019
"""

import numpy as np
from itertools import permutations

def prefix_eval(tokens):
    try:
        stack = []
        for t in reversed(tokens):
            if   t == '+': stack[-2:] = [stack[-1] + stack[-2]]
            elif t == '-': stack[-2:] = [stack[-1] - stack[-2]]
            elif t == '*': stack[-2:] = [stack[-1] * stack[-2]]
            elif t == '/': stack[-2:] = [stack[-1] / stack[-2]]
            else: stack.append(t)
        assert len(stack) == 1, 'Malformed expression'
        return stack[0]
    except:
        pass

class Calculator:
    def __init__ (self):
        self.stack = []

    def push (self, p):
        if p in ['+', '-', '*', '/']:
            op1 = self.stack.pop ()
            op2 = self.stack.pop ()
            self.stack.append ('(%s %s %s)' % (op1, p, op2) )
        elif p == '!':
            op = self.stack.pop ()
            self.stack.append ('%s!' % (op) )
        elif p in ['sin', 'cos', 'tan']:
            op = self.stack.pop ()
            self.stack.append ('%s(%s)' % (p, op) )
        else:
            self.stack.append (p)

    def convert (self, l):
        l.reverse ()
        for e in l:
            self.push (e)
        return self.stack.pop ()

c = Calculator ()

operands1 = np.arange(111,445)
operands2 = []
for i in range(len(operands1)):
    num = str(operands1[i])
    if int(num[2]) >= int(num[1]) and int(num[1]) >= int(num[0]) and int(num[2]) <= 4:
        operands2.append(num)

for i in range(len(operands2)):
    string = operands2[i]
    temp = ""
    for j in range(0,3):
        if string[j] == "1":
            temp += "+"
        if string[j] == "2":
            temp += "-"
        if string[j] == "3":
            temp += "*"
        if string[j] == "4":
            temp += "/"
    operands2[i] = temp
    

perms = [''.join(p) for p in permutations("1234567")]
nums = []
for i in range(len(perms)):
    temp = perms[i]
    if temp[6] != "1" and temp[6] != "2" and temp[6] != "3":
        nums.append(temp)

nums2 = []
        
for i in range(len(operands2)):
    op = operands2[i]
    for j in range(len(nums)):
        temp = nums[j]
        temp = temp.replace("1",op[0])
        temp = temp.replace("2",op[1])
        temp = temp.replace("3",op[2])
        nums2.append(temp)

rows, cols = (len(nums2), 7)
arr=[]
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(0)
    arr.append(col)
    
print("1st number")
num1 = int(input())
print("2nd number")
num2 = int(input())
print("3rd number")
num3 = int(input())
print("4th number")
num4 = int(input())    

for i in range(len(nums2)):
    for j in range(7):
        temp = nums2[i]
        if temp[j] == "4":
            arr[i][j] = num1
        elif temp[j] == "5":
            arr[i][j] = num2
        elif temp[j] == "6":
            arr[i][j] = num3
        elif temp[j] == "7":
            arr[i][j] = num4
        else:
            arr[i][j] = temp[j]

for i in range(len(nums2)):
    if prefix_eval(arr[i]) == 24:
        print(c.convert(arr[i]))
        break
    if i == len(nums2)-1:
        print("No Solution")


        
