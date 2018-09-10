import math as my_mat
print('enter a number', end='=')
a = input()
print('enter a number', end='=')
b = input ()
def foo(a,b):
    a=int(a)
    b=int(b)

    print('a+b=',a,b )
    print()
    print('a power 2', a=a**2)
    a/=6

    return a

print (foo (a))