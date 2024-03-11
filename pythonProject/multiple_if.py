height = int(input("what is your height in feet:"))
bill = 0
if height >= 3:
    print("you can ride")
    age = int(input("what is your age?"))
    if age < 12:
        bill = 150
        print("pay 150$")
    elif age <= 18:
        bill = 250
        print("pay 250$")
    else:
        bill = 500
        print("pay 500$")
    want_photo = input("Do you want to take photos?")
    if want_photo == 'yes':
        bill = bill + 50
    print(f"your total bill is {bill}")

else:
    print("can't ride")
print("Thank you.. for your ride")
