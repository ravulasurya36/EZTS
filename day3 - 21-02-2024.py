'''
n=int(input())
l=list(map(int,input().split()))[:n]
for i in range(n):
    if l[i] in l[i+1:]:
        print(l[i])
        break
'''


'''
n=int(input())
l=list(map(int,input().split()))[:n]
for i in l:
    c=l.count(i)
    if c>1:
        print(i)
        break
'''

#p22
'''approach 1
n=int(input())
l=list(map(int,input().split ()))
unique=[ ] 
for i in range(n):
    if l.count(l[i])==1:
        if l[i] in unique:
            continue
        else:
            unique.append(l[i])
for i in unique:
    print (i,end=" ")
'''
'''approach 2
n=int(input())
l=list(map(int,input().split()))[:n]
for i in l:
    if l.count(i)==1:
        print(i,end=" ")
'''

'''
t=int(input())
for i in range(t):
    n=int(input())
    f=0
    s=0
    for i in range (1,n+1):
        if n%i==0:
            if i%2==0:
                f+=1
            else:
                s+=1
    if f==s:
        print(1)
    else:
        print(0)
'''
'''

def m(n,x,f,s):
    if x<1:
        if f==s:
            print(1)
        else:
            print(0)
    else:
        if n%x==0:
            if x%2==0:
                f+=1
            else:
                s+=1
            m(n,x-1,f,s)
        else:
            m(n,x-1,f,s)
def t(n):
    if n>0:
        s=int(input())
        
        m(s,s,0,0)
        t(n-1)
    else :
        return
n=int(input())
t(n)
'''

'''

t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    f=list(map(int,input().split()))
    c=list(map(int,input().split()))
    r=0
    for j in range(len(f)):
        if f[j]>=x:
            r=r+c[j]
    print(r)
'''

'''

t=int(input())
while t>0:
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    t-=1
    c=0
    for i in range(n):
        if a[i]<=b[i]*2 and a[i]*2>=b[i]:
            c+=1
            
    print(c)

'''
t=int(input())
s=0
for j in range(2,t+1,2):
    for i in range(1 ,j):
        if j%i==0:
            s+=i
    if s==j:
        print(s)
    s=0

        
            

    
    

        

            

        
            
    
    


















