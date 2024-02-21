'''a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)'''


#P3

'''
a=int(input())
b=int(input())
c=int(input())
if (a<=b and a>=c) or (a>=b and a<=c):
    print(a)
elif (b<=a and b>=c) or (b>=a and b<=c):
    print(b)
else:
    print(c)
 '''



'''   
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    a=0
elif b>c:
    b=0
else:
    c=0
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)   
'''



'''
for i in range(1000):
    print(i,"Hello World")
'''



'''
a,b=map(int,input().split())
if a<b:
    print("a < b")
elif a>b:
    print("a > b")
else:
    print("a == b")
'''

'''
a,b,c=map(int,input().split())   
if a+b>c and b+c>a and a+c>b:
    print("Yes")
else:
    print("No")
'''

'''
n=int(input())
k=int(input())
while k>n:
    k=k-n
print(k)
'''




'''
a=int(input())
e=abs(a)
c=0
if a<0:
    c=1
ans=0
while(e>0):
    r=e%10
    ans=ans*10+r
    e=e//10
if c==1:
    print(-1*ans)
else:
    print(ans)
'''



'''
n=int(input())
if n==2:
    print('No')
elif n%2==0:
    print('Yes')
    '''
    
    
    
'''   
n=int(input())
for i in range(n):
    t=int(input())
    if t>98:
        print('Yes')
    else:
        print("No")
''' 



 
'''
n=int(input())
while n>0:
    t=int(input())
    if t>98:
        print('Yes')
    else:
        print("No")
    n-=1
'''


 
'''
n=int(input())
for i in range(n):
    p=int(input())
    print(100-p)
'''



'''
n=int(input())
for i in range(n):
    t1,t2,d1,d2=map(int,input().split())
    t1=t1-d1
    t2=t2-d2
    if t1<t2 :
        print("First")
    elif t2<t1:
        print("Second")
    else:
        print("Any")
'''



'''
n=int(input())
while n>0:
    t1,t2,d1,d2=map(int,input().split())
    t1=t1-d1
    t2=t2-d2
    if t1<t2 :
        print("First")
    elif t2<t1:
        print("Second")
    else:
        print("Any")
    n-=1
'''

'''
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if a>=b:
        k=a-b
        if k%4==0:
            print(k//4)
        else:
            print((k//4)+1)
    else :
        print(0)
'''



'''
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if a*b%4==0:
        print(a*b//4)
    else:
        print((a*b//4)+1)
'''

n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    c=a*b
    r=0
    while c>0:
        c-=4
        r+=1
    print(r)
        

        

    
            
            
            

        





































