import pandas as pd
x = open('ass2(1).txt','a')                             # Opening files in append mode
inputs = [int(input('Enter number :')) for _ in range(5)]    # input of the Five numbers 
list_1=[]
for i in inputs:
    power= i**2                                             # Power of the five numbers
    list_1.append(power)
df = pd.Series(list_1,index=inputs)                               # Taking the input and power value into the Series
print(df)
print(df,file=x)                                        # output into the file
x.close()