Floyd = int(input("Enter the amount of rows you want."))
number = 1
for i in range (Floyd):
    for j in range (i + 1):
        print(number, end = "")
        number = number + 1
    print()