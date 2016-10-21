
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
