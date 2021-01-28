from re import *

for i in range(int(input())):
    a, b = input().split()
    reg = r'^<([a-z][\w+-._]+)@([a-z]+)\.([a-z]{1,3})>$'
    if match(reg, b):
        print(a, b)
        
