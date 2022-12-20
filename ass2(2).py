x = open('ass2(2).txt','a')

import pandas as pd

def Addition(a,b):
    return(int(a+b))

def Subtraction(a,b):
    return(int(a-b))

def Multiplication(a,b):
    return(int(a*b))

def Division(a,b):
    return(float(a/b))

def Modulus(a,b):
    return(int(a%b))

num1 = int(input(' Enter the first number :'))
num2 = int(input(' Enter the second number :'))            
list1 = [f'{num1} + {num2}',f'{num1} - {num2}',f'{num1} * {num2}',f'{num1} / {num2}',f'{num1} % {num2}']
list2 = []
list2.append(Addition(num1,num2))
list2.append(Subtraction(num1,num2))                        
list2.append(Multiplication(num1,num2))
list2.append(Division(num1,num2))
list2.append(Modulus(num1,num2))

df = pd.Series(list2,index=list1)

print(df)

print(df,file=x)

x.close()