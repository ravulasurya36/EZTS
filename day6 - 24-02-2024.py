'''
class classn:
    def __init__(self,n):
        self.n=n
    def isprime(self):
        c=0
        for i in range(1,self.n):
            if self.n%i==0:
                c+=1
        if c>1:
            return ('No')
        else:
            return ('Yes')
ob1=classn(5)
ob2=classn(12)
print(ob1.isprime())
print(ob2.isprime())
'''

'''
class classn:
    def __init__(self,n):
        self.n=n
    def ispalindrome(self):
        c=self.n
        r=0
        while self.n>0:
            r=r*10+self.n%10
            self.n//=10
        if r==c:
            print('yes')
        else :
            print('no')
        
ob1=classn(1221)
ob2=classn(12321)
ob1.ispalindrome()
ob2.ispalindrome()
'''

'''
class classn:
    def __init__(self,n):
        self.n=n
    def ispalindrome(self):
        if self.n==self.n[::-1]:
            print('Yes')
        else :
            print('NO')
        
ob1=classn('Hello')
ob2=classn('SuS')
ob1.ispalindrome()
ob2.ispalindrome()
'''

'''
class classn:
    def __init__(self,n):
        self.n=n
    def isprime(self):
        c=0
        for i in range(1,self.n):
            if self.n%i==0:
                c+=1
        if c>1:
            print('No')
        else:
            print('Yes')
    def ispalindrome(self):
        x=self.n
        r=0
        while x>0:
            r=r*10+x%10
            x//=10
        if r==self.n:
            print('Yes')
        else :
            print('No')
ob1=classn(11)
ob2=classn(12321)
ob1.ispalindrome()
ob2.ispalindrome()
ob1.isprime()
ob2.isprime()
'''

'''
class classn:
    def __init__(self,n,s):
        self.n=n
        self.s=s
    def isprime(self):
        c=0
        for i in range(1,self.n):
            if self.n%i==0:
                c+=1
        if c>1:
            print('No')
        else:
            print('Yes')
    def ispalindrome(self):
        if self.s==self.s[::-1]:
            print('Yes')
        else :
            print('NO')

ob1=classn(11,'sas')
ob2=classn(12321,'hello')
ob1.ispalindrome()
ob2.ispalindrome()
ob1.isprime()
ob2.isprime()
'''

'''
class Car:
    maxspeed = 0
    name = ""
    def __init__(self):
        self.maxspeed = 200
        self.name = "Supercar"
    def drive (self):
        print (self.maxspeed)
carl = Car ()
carl.drive ()
carl.maxspeed = 10
carl.drive ()
'''

'''
class Car:
    __maxspeed = 0
    __name = ""
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
    def drive (self):
        print (self.__maxspeed)
carl = Car ()
carl.drive ()
carl.__maxspeed = 10
carl.drive ()
'''

'''
class dob:
    def __init__(self,date,month,year):
        self.date=date
        self.month = month
        self.year = year
    def display1(self):
        d = {1:"Jan",2:"Feb"}
        print(self.date)
        print(d[self.month])
        print(self.year)
class details(dob):
    def __init__(self,name,age,date,month,year):
        self.name = name
        self.age = age
        self.date = date
        self.month = month
        self.year = year
        super().__init__(date,month,year)
    def display(self):
        print(self.name)
        print(self.age)
        print(self.date)
        print(self.month)
        print(self.year)
p = details("abc",27,24,1,2001)
p.display()
p.display1()
'''

'''
class vehicle:
    def __init__(self,fuel):
        self.fuel = fuel
    def display3(self):
        print(self.fuel)
class motor(vehicle):
    def __init__(self,cc,fuel):
        self.cc = cc
        self.fuel = fuel
        super().__init__(fuel)
    def display2(self):
        print(self.cc)
        print(self.fuel)
class car(motor):
    def __init__(self,name,cc,fuel):
        self.name = name
        self.cc = cc
        self.fuel = fuel
        super().__init__(cc,fuel):
    def display1(self):
        print(self.name)
        print(self.cc)
        print(self.fuel)
v1 = car("BMW","300cc","Petrol")
v1.display1()
v1.display2()
v1.display3()
'''

'''
from abc import ABC,abstractmethod
class a(ABC):
    @abstractmethod
    def display(self):
        pass
class b(a):
    def display(self):
        print("Class B")
class c(a):
    def display(self):
        print("Class c")

c1 = c()
c1.display()
c2 = b()
c2.display()
'''

'''
try:
    a = int(input())
    c= a // 2
except ZeroDivisionError:
    print("division error")
except Exception as e:
    print(e)
else:
    print(c)
finally:
    print("Hello")
'''

































