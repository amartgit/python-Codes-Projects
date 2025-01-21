#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      amart
#
# Created:     26-06-2023
# Copyright:   (c) amart 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
print("Hello World")
a=0
while a<5:
        print(a)
        a=a+1
        if a>=4:
            break

list=[10,20,30,40,50,60,70]
for b in list:
    if b== 30:
        continue
    print(b)

for b in list:
    if b== 60:
        pass
    print(b)
import calculator1st