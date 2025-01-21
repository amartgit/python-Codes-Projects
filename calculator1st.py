
a=int(input("enter your value of a:"))
opr=(input("enter operation..(+,-,*,/):"))
b=int(input("enter your value of b:"))
if opr==("+"):
    print(a+b)
elif opr==("-"):
    print(a-b)
elif opr==("*"):
    print(a*b)
elif opr==("/"):
    print(a/b)
    try:
        a_divide_b=1/0
    except:
        "divide by zero exception"
    else:
        print("value of 1/0 is",a)
else:
    print("error")
