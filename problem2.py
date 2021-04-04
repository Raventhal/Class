
msg = "Please enter an integer!"


while True:
    try:
        number1 = int(input("Enter 1st number: "))
        break
    except:
        print(msg)
while True:
    try:
        number2 = int(input("Enter 2nd number: "))
        break
    except:
        print(msg)
while True:
    try:
        number3 = int(input("Enter 3rd number: "))
        break
    except:
        print(msg)

numberlist = []

numberlist.extend((number1, number2, number3))

users = sorted(numberlist)
#print(users[0])
#print(users[1])
#	print(users[2])

x = users[0]
y = users[1]
z = users[2]


if (x + 1 == y and z >= y + 2):
	print("true")
elif (y + 1 == z and x <= y + 2):
	print("true")
else:
	print('false')
