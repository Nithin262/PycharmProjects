size = input("What size pizza you want(s/m/l)?")
bill = 0
if size == 's':
    bill = bill + 100
    print("small pizza is 100$")
elif size == 'm':
    bill += 150
    print("medium pizza is 150$")
else:
    bill += 200
    print("large pizza is 200$")
add_pepperoni = input("do you need pepperoni(y/n)?")
if add_pepperoni == 'y':
    if size == 's':
        bill += 30
    else:
        bill += 50
want_cheese = input("do you need extra cheese(y/n)?")
if want_cheese == 'y':
    bill += 20
print(f"your total bill is {bill}")
print("Thank you..enjoy your pizza")
