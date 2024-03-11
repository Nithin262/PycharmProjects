height = int(input("what is your height in feet:"))
if height >= 3:
    print("you can ride")
    age = int(input("what is your age?"))
    if age <= 18:
        print("pay 260$")
    else:
        print("pay 500$")
else:
    print("can't ride")
print("bye")


height = int(input("what is your height in feet:"))
if height >= 3:
    print("you can ride")
    age = int(input("what is your age?"))
    if age < 12:
        print("pay 150$")
    elif age <= 18:
        print("pay 250$")
    else:
        print("pay 500$")
else:
    print("can't ride")
print("bye")
