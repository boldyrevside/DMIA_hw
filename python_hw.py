
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

"""
Matplotlib
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math
import matplotlib
x = np.arange(0, 4*np.pi+0.1, 0.1)
y = np.sin(x)
z = np.sin(2*x)

x2 = np.linspace(0,5,300)
y2 = x2**2
z2 = 10*x2
v2 = 1/x2 
l2 = np.cos(x2)
s2 = np.sin(x2)

fig = plt.figure(num=None, figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k')
plt.subplot(2,2,1)
plt.gca()
plt.plot(x2, z2,color='red', linewidth=3.0, label = r'$10x$')

plt.plot(x2, y2, color='g', linewidth=3.0, label = r'$x^2$')
plt.plot(x2, v2, color='blue', linewidth=3.0,label = r'$\frac{1}{x}$')
plt.xlabel('X axe')
plt.ylabel('Y axe')
plt.legend()
plt.grid(True)

plt.subplot(2,2,2)
plt.plot(x2, l2, color='red', linewidth=3.0,label = r'$\sin(x)$')
plt.plot(x2, s2, color='g', linewidth=3.0,label = r'$\cos(x)$')
plt.xlabel('X axe')
plt.grid(True)
plt.legend()

plt.show()
fig.savefig('lol.pdf')

"""
SciPy
"""
import numpy as np
from numpy import linalg as LA


mat = np.random.randn(5,5)
print "matrix:"
print mat
i,k = LA.eig(mat)
print "eigenvalues:"
print i
print "eigenvectors:"
print k

def chekEig(a,b,c):
    i=0
    while i<len(c):
        if (c[i]*b[:,i]).all()!=(np.dot(a,b[:,i])).all():
            return False
        i=i+1
    return True
    
print "Are all eigenvalues and eigenvectors satisfy?"
print chekEig(mat,k,i)
