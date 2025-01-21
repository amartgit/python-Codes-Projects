#-------------------------------------------------------------------------------
# Name:        averageprac
# Purpose:
#
# Author:      amart
#
# Created:     26-06-2023
# Copyright:   (c) amart 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
last_number=int(input("enter the number of elements to be inserted:"))
x=[]
for i in range(0,last_number):
    element=int(input("enter element:"))
    x.append(element)
average=sum(x)/last_number
print("average of elements in list",round(average,2))