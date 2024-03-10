name=input('Enter your name : ')
print('Hello '+name+('\n\n'))
print('Calculator application :\n')
while True :
  a=float(input('Enter the first number : '))
  b=input('Enter subtraction(-) or addition(+) or multiplication(x) or divided(/) or power(p) or radical(r) or average(a) : ')
  c=float(input('Enter the second number : '))
  if b == ('+') :
    print(a,'+',c, '=' ,a+c)
  elif b == ('-') :
    print(a,'-',c, '=' ,a-c)
  elif b == ('x') :
    print(a,'x',c, '=' ,a*c)
  elif b == ('/') :
    print(a,'/',c, '=' ,a/c)
  elif b == ('P') :
    print(a,'^',c, '=' ,a**c)
  elif b == ('r') :
    print(a,'√',c,'=' ,a*(c**0.5))
  elif b == ('a') :
    print(a,'~',c,'=' ,0.5*(a+c)) 
print('tnx for using the program\n\n')