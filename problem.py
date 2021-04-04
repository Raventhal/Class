while True:
    try:
        num = int(input("Enter a number 1-5! (0 to exit): "))
        if (num > 5 or num < 0):
        	print("Sorry, you must enter a number 1-5")
##        if (num < 0):
#        	print("Sorry, you must enter a number 1-5")
        	
        elif num == 0:
           quit()
           
		         
        else:
        	break
        print(num)
    except ValueError:
        print("Sorry, you must enter an integer")
num = num * -1

anumber = int(num)
thelist = [1, 2 , 3, 4, 5, 6]
print(thelist)
#print(alist[anumber:])
#print(alist[:anumber])
z = (thelist[anumber:] + thelist[:anumber])
print(z)
