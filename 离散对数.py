#p=257914399, g=3, t=177985882
#p=528649698299, g=2, t=149085463602
#p=34260590035568446981, g=6, t=25292156174011578005
#p=910448576901027401405851, g=7, t=575965469036372948060666
#p=21389604391654683144213769, g=7, t=7417803252846392445739601

from functools import reduce
import time
import random
import math

def func():
    print("a^e = b (mod p)")
    print("g^e = t (mod p)")
    print('输入a(g)')
    g=int(input())
    print('输入b(t)')
    t=int(input())
    print('输入p')
    p=int(input())
    
    start_time=time.time()
    Pohlig_Hellman(g,t,p)
    end_time=time.time()
    run_time=end_time-start_time
    
    print("time=",run_time,"s",)

def Pohlig_Hellman(g,t,p):
      Lst_qe=qe(p-1)
      Lst_g=[pow(g,(p-1)//i,p) for i in Lst_qe]
      Lst_t=[pow(t,(p-1)//i,p) for i in Lst_qe]
      print('List g=',Lst_g)
      print('List t=',Lst_t)
      length=len(Lst_qe)
      Lst_ai=[]
      for i in range(length):
            Lst_ai.append(shanks(Lst_g[i],Lst_t[i],Lst_qe[i],p))
      print('List a=',Lst_ai)
      E=CRT(Lst_qe,Lst_ai)
      if pow(g,E,p)==t:
          print("成功 e = ",E)
      else:print("Wrong Answer")

#求List q^e
def qe(n):
    ans=[]
    print('first n',n)
    while True:
        temp=pollard(n)
        print('temp',temp)
        temp1=temp
        n=n//temp
        print('n',n)
        while(n%temp==0):
            temp1=temp*temp
            n=n//temp
            print('nnnnn',n)
        ans.append(temp1)
        print('ans',ans)
        if (n==1):
            print('ans',ans)
            return ans
        if judge(n):
            ans.append(n)
            print('ans',ans)
            return ans

#p方法
def f(x,number):
    x=(x*x+1)%number
    return x

def pollard(num):
    if(judge(num)):
       print(num)
       return
    a=2
    b=a
    d=1
    while d==1:
        a=f(a,num)
        b=f(f(b,num),num)
        d=math.gcd(abs(b-a),num)
    return d

def judge(number):
   if (number in [2,3,5,7,11,13]):
      return True
   if (number%2==0 or number%3==0 or number%5==0 or number%7==0 or number%11==0 or number%13==0):
      return False
   a=random.randint(2,10)
   t=number-1
   k=0
   while(t%2==0):
      t=t//2
      k=k+1
   x=pow(a,t,number)
   while(k>0):
      last=x
      x=x*x%number
      if(x==-1):
          return True
      if(x==1 and last!=1 and last!=number-1):
          return False
      k=k-1
   if(x!=1):
      return False
   return True

#大步小步
def shanks(g,t,p,arg):
    s = int(math.sqrt(p))+1
    hashmap = {}
    g_step = pow(g,s,arg)
    tem = t
    for r in range(s):
        hashmap[tem] = r
        tem =tem * g % arg
    tem = 1
    for k in range(1,s+1):
        tem =tem * g_step % arg  
        if tem in hashmap.keys():
            return (k*s - hashmap[tem])
    return False

#中国剩余定理
def CRT(m,b):
      Num=len(m)
      M=reduce(lambda x,y: x*y, m)
      Mi=[M//i for i in m]
      t=[]
      for i in range(Num):
          arr=[0,1,]
          res=ex_gcd(Mi[i],m[i],arr)
          if res==1:
              result=int ((arr[0]%m[i]+m[i])%m[i])
          else:
              result=-1
          t.append(result)
      x=0
      for i in range(Num):
            x+=b[i]*t[i]*Mi[i]
      return x%M

def ex_gcd(a,b,arr):
    if b==0:
        arr[0]=1
        arr[1]=0
        return a
    r=ex_gcd(b,a%b,arr)
    tmp=arr[0]
    arr[0]=arr[1]
    arr[1]=tmp-int(a/b)*arr[1]
    return r

