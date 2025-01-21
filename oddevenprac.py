#-------------------------------------------------------------------------------
# Name:        oddeven
# Purpose:
#
# Author:      amart
#
# Created:     26-06-2023
# Copyright:   (c) amart 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
a=int(input("enter your value of from:"))
b=int(input("enter your value of to:"))
print("odd numbers :")
for i in range(a,b+1):
    if (i%2!=0):
        print(i)
print("Even numbers :")
for i in range(a,b+1):
    if (i%2==0):
        print(i)
