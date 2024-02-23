'''
s=input()
o=""
e=""
for i in range(len(s)):
    if i%2==0:
        e+=s[i]
    else:
        o+=s[i]
print(o)
print(e)
print(o+e)
'''

'''
s=input()
print(s[1::2])
print(s[::2])
'''

'''
s=input()
ch=input()
c=0
for i in range(len(s)):
    if ch[0]==s[i]:
        c+=1
print(c)
'''

'''
s=input()
ch=input()
print(s.count(ch))
'''

'''
s=input()
ch=input()
c=0
for i in range(0,len(s),2):
    if ch[0]==s[i]:
        c+=1
print(c)
'''

'''
s=input()
ch=input()
s=s[::2]
print(s.count(ch))
'''

'''
s=input()
v='aeiou'
c=0
for i in s:
    if i in v:
        c+=1
if c==len(s):
    print('Yes')
else:
    print('No')
'''

'''
s=input()
v='aeiou'
c=0
for i in s:
    if i not in v:
        c+=1
if c==0:
    print('Yes')
else:
    print('No')
'''

'''
s=input()
v='aeiou'
c=0
for i in s:
    if i not in v:
        c+=1
        break
else:
    print('No')
'''

'''
s=input()
v='0123456789'
c=0
for i in s:
    if i in v:
        c+=1
if c==len(s):
    print('Yes')
else:
    print('No')
'''

'''
s=input()
v='0123456789'
c=0
for i in s:
    if i not in v:
        c+=1
if c==0:
    print('Yes')
else:
    print('No')
'''

'''
s=input()
v='0123456789'
c=0
for i in s:
    if i not in v:
        c+=1
        break
else:
    print('No')
'''

'''
s=input()
print(s.isdigit())
'''

'''
s=input()
v='aeiou'
c='qwrtypsdfghjklzxcvbnm'
vc=0
cc=0
for i in s:
    if i in v:
        vc+=1
    elif i in c:
        cc+=1
print(vc)
print(cc)
'''

'''
s=input()
v='aeiou'
vc=0
cc=0
for i in s:
    if i.isalpha():
        if i in v:
            vc+=1
        else:
            cc+=1
print(vc)
print(cc)
'''

'''
s=input()
c=1
s1=s[0]
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        c+=1
    else:
        s1+=str(c)
        s1+=s[i]
        c=1
s1+=str(c)
print(s1)
'''

'''
t = int(input())
v = "aeiou"
for i in range(t):
    s = list(input().split())
    vc = 0
    cc = 0
    wc=len(s)
    for j in s:
        for k in j:
            if k.isalpha():
                if k in v:
                    vc+=1
                else:
                    cc+=1
    print(wc,vc,cc)
'''


'''
t=int(input())
while t>0:
    s=input()
    l=list(s.split())
    v='aeiou'
    w=len(l)
    vc=0
    cc=0
    for i in s:
        if i.isalpha():
            if i in v:
                vc+=1
            else:
                cc+=1
    print(w,vc,cc)
    t-=1
'''

'''
t=int(input())
while t>0:
    l=list(input().split())
    s=''
    for i in l[1]:
        if i not in l[0]:
            s+=i
    print(s)
'''

'''
t=int(input())
while t>0:
    a,b=input().split()
    b=int(b)
    r=''
    for i in a:
        k=ord(i)+b
        if k>122:
            k=96+(k-122)
            r+=chr(k)
        else:
            r+=chr(k)
    print(r)
    t-=1
'''

'''
class a:
    def _init_(self,n):
        self.n=n 
    def fact(self):
        r=1
        for i in range(1,self.n+1):
            r*=i 
        print(r)
ob=a(5)
ob.fact()
'''
'''

class c:
    def factorial(self,n):
        self.n=n
        print(self.fact(self.n))
    def fact(self,n):
        if n==0:
            return 1
        
        return n*self.fact(n-1)
c=c()
c.factorial(5)
'''           
count = [0] * (4 + 1)
print(count)






        







