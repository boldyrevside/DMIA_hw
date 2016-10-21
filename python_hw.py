
"""
Python
"""


def FizzBuzz():
    a=range(1,101)
    i=0
    while i<100:
        if a[i]%3==0 and a[i]%5==0:
           a[i]= "FizzBuzz"
        elif a[i]%3==0:
            a[i]="Fizz"
        else:
            if a[i]%5==0:
                a[i]="Buzz"
        i=i+1
    print a                   

FizzBuzz()                   

def fib(n):
    if n < 2:
        return n
    a=range(n)
    a[0]=1
    a[1]=1
    i=2
    while i<n:
        a[i]=a[i-1]+a[i-2]
        i=i+1
    return a[n-1]

fib(100)
