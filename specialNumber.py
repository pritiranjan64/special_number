#--------------------using loop------------------------
n=int(input('enter a number'))
dummy=n
s=0
while dummy>0:
    rem=dummy%10
    dummy//=10
    f=1
    for i in range(1,rem+1):
        f*=i
    s+=f    
if n==s:
    print('special number')
else:
   print(' not a special number')
  
#--------------------using function-------------------
def isSpecial(n):
    dummy=n
    s=0
    while dummy>0:
        rem=dummy%10
        dummy//=10
        f=1
        for i in range(1,rem+1):
            f*=i
        s+=f    
    if n==s:
        print('special number')
    else:
        print(' not a special number')
isSpecial(n=int(input('enter a number')))

  