#Simple interest... formula=pnr/100(principle amount,no. of years,rate of interest)
p=float(input("Enter the principle amount: "))
n=float(input("Enter the number of years: "))
r=float(input("Enter the rate of interest: "))
si=(p*n*r)/100
amt=si+p
print("The simple interst is =",si,"The amount is =",amt)
