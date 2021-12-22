no_of_days=int(input("How many day's Temperature  "))
temperature=[]
for i in range(1,no_of_days+1):
    n=int(input(f"Day {i}'s High Temperature "))
    temperature.append(n)
Average_Temperature=sum(temperature)/no_of_days
print(f"Average_Temperature is {Average_Temperature}.")
c=0
for i in temperature:
    if i> Average_Temperature:
        c+=1
print(f"{c} day(s) above average temperature")