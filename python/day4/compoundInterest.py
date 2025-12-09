# coumpound interest
# A=P(1+R/100)^t
# coumpond interest=A-P
p=float(input("enter the principal amount"))
r=float(input("enter the rate of interest"))
t=int(input("enter the time in years"))
A=p*(pow((1+r/100),t))
print(f"{A-p:.2f}")