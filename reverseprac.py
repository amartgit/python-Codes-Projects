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
n=int(input("enter number:"))
rev=0
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("Reverse of the number:",rev)