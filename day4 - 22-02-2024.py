'''s=input()
s1=set()
for i in s:
    if i.isalpha():
        s1.update(i)
if len(s1)==26:
    print('pangram')
else:
    print('not pangram')
print(s1)

'''


'''

a={'g', 'p', 'x', 'j', 'l', 'f', 'b', 's', 'e', 'o', 'h', 'q', 'i', 'm', 'y', 'n', 'w', 'k', 'v', 't', 'c', 'a', 'd', 'r', 'z', 'u'}
s=input()
d={}
for i in s:
    if i in a :
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
x=d.keys()
if len(x)==26:
    print('pangram')
else:
    print('not pangram')


'''


'''
t=int(input())
while t>0:
    a={'g', 'p', 'x', 'j', 'l', 'f', 'b', 's', 'e', 'o', 'h', 'q', 'i', 'm', 'y', 'n', 'w', 'k', 'v', 't', 'c', 'a', 'd', 'r', 'z', 'u'}
    s=input()
    d={}
    for i in s:
        if i in a :
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
    print(len(d))
    for i in range d:
        if d[i]>1:
            print(i)
            break
        elif i==len(d)-1:
            print('.')
        
    t-=1
'''

'''

n = int(input())
d = {}
for i in range(n):
    s = input()
    if s in d:
        d[s] = d[s] +1
    else:
        d[s] = 1
#print(d)
x = max(d.values())
z = []
for i in d:
    if d[i] == x:
        z.append(i)
print(max(z),x)

'''
'''
n = int(input())
d = {}
for i in range(n):
    name, num = input().split()
    d [name] = num
while True:
    s = input()
    if s in d:
        print (f"{s}={d[s]}")
    else:
        print("Not Found")
'''
'''
t = int(input())
for i in range(t):
    n,r = map(int, input().split())
    d = {}
    for j in range(r):
        sid, cid = map(int, input().split())
        if cid not in d:
            d[cid] = [sid]
        else:
            d[cid].append(sid)
            print (d)
            for j in d:
                if len (d[j]) > n:
                    print(f"Scenario #(i+1): Impossible")
                    break
                else:
                    print (f"Scenario #(i+1): Possible")
'''
'''
n = int(input())
route = {}
for i in range(n):
    c1,c2 = input().split()
    if c1 not in route:
        route [c1] = [c2]
    else:
        route [c1].append(c2)
print(route)
city = input()
if city in route:
    print(*route [city], sep="")
else:
    print("None")


'''




            





