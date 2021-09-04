"""
== : equal , != : does not equal ,< : less than ,> : larger than
>= : less or equal , <= larger or equal

And Operator 
True and True  =>  True
True and False  =>  False
False and True  =>  False
False and False  =>  False

or Operator 
True or True  =>  True
True or False  =>  True
False or True  =>  True
False or False  =>  False
"""


# if else
i=2
if i == 2:
    print("i equal 2")
else:
    print("i does not equal 2")


#if elif else
if i == 1:
    print("i equal 1")
elif i == 2:
    print("i equal 2")
else:
    print("i does not equal 1 or 2")


# Ternary  operator

a = 3
print(a) if a > i else print(i)


