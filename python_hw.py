
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

"""
NumPy
"""


import numpy
from time import time

t0 = time()
#print numpy.linspace(1,20)
from timeit import Timer
t = Timer("linspace(1,20)", "from numpy import linspace")
print "linspace by Numpy executes in",t.timeit(),"usec"

    
def CycleLinSpace(a,b,n):
    a = float(a)
    b = float(b)
    n = float(n)
    otr=(b-a)/n
    l = []
    k=0
    while k < n+1:
        l.append(a+k*otr)
        k=k+1
    return l

#print CycleLinSpace(1,20,50)
from timeit import Timer
t = Timer("CycleLinSpace(1,20,50)", "from __main__ import CycleLinSpace")
print "linspace by Cycle executes in",t.timeit(),"usec"

def ListLinSpace(a,b,n):
    a = float(a)
    b = float(b)
    return [a + (b-a)/n*x for x in range(n+1)]

#print ListLinSpace(1,20,50)

from timeit import Timer
t = Timer("ListLinSpace(1,20,50)", "from __main__ import ListLinSpace")
print "linspace by List Comprehension executes in",t.timeit(),"usec"
