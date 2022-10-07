def func():
    for i in range (3):
        yield i
res = func()

print(next(res))
print(next(res))

l=[1, 2, 3, 4]
def func1(a):
    for i in a:
        yield i**2
        yield i**3

print(list(func1(l)))


""""""

def func():
    for i in range (3):
        yield i
res = func()


l=[1, 2, 3, 4]
def func1(a):
    for i in a:
        yield i**2

print(list(func1(l)))
""""""
l=[1,2,3,4]

res = ((num**2)for num in l )
print(next(res))
print(next(res))
print(next(res))
print(next(res))



""""""
import math
PI = math.pi
print(PI)

def func(num):
    for i in range(num):
        yield round(PI,i)

print(list(func(6)))




#gen =(round(PI,i)for i in range(5)):
#print(list(gen(6)))

""""""
n1= 0
n2 = 1

for i in range(10):
    res=(n1)
    print(res, end=" ")
    next_ = n1 + n2
    n1 = n2
    n2 = next_

   # if i in  P :
    #    print("its a fibonacci number")
    #else:
     #   print("not fibonacci number")
print()
""""""

def func(num):
    n1=0
    n2=1

    for i in range(num):
        yield n1
        n1,n2 = n2,n1+n2
print(list(func(10)))

""""""
names = ["laura", "steve", "bill", "james", "greig", "scott", "alex", "ive"]

def func(a):
    for ele in a:
        if ele[0] in "aeiouAEIOU":
            yield ele


print(list(func(names)))


""""""

""""""
def fibo(num):
    a=o
    b=1
    for i in range (num):
        yield a
        c = a + b
        a = b
        b = c
    if num in l:
        yield "its a fibo number"
    else:
        yield  "its not a fibo number"

print(list(fibo(10)))
""""""
def func(*args):
    if len(args)>5:
        yield f"{len(args)} is less than 5"
    else:
        yield f"{len(args)} is more than 5"

#func(10,20,30,40,50)



