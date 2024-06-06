#Compound interest... 
p=float(input("Enter the principle amount: "))
n=float(input("Enter the number of years: "))
r=float(input("Enter the rate of interest: "))
ci=p*((1+r/100)**n-1)
amt=p+ci
print("The compound interest is =",ci,"The amount is =",amt)
