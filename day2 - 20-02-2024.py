
'''

def myfun(x):
    x[0]=10000
l=[10,11,12,13,14,15]
myfun(l)
print(l)
'''


'''
def profit(x):
    return x*50*0.3
def recursive(n):
    if n>0:
        x=int(input())
        print(profit(x))
        recursive(n-1)
    else :
        return
n=int(input())
recursive(n)
'''


'''
a,b=map(int,input().split())
print(int(a-b/2))
'''


'''
def m(x,y):
    print(int(x-y/2))
a,b=map(int,input().split())
m(a,b)

'''

'''
def o(x):
    if x==0:
        return 0
    else :
        if x%10==4:
            return 1+o(x//10)
        else :
            return o(x//10)

def r(n):
    if n>0:
        x=int(input())
        print(o(x))
        r(n-1)
    else :
        return
n=int(input())
r(n)
'''

'''
n=int(input())
k=1
for i in range(1,n+1):
    k=k*i
print(k)

''' 

'''
def rec(n):
    if n==0:
        return 1
    else:
        return n*rec(n-1)
n=int(input())
r=rec(n)
print(r)
'''

'''
n=int(input())
x=n
c=0
while n>0:
    n=n//10
    c+=1
x=3*(10**c)+x
x=x*10+3
print(x)

'''


















