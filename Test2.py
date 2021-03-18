hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)
ot = r * float(40) + (h - float(40)) * (r * 1.5) 
if h > 40 :
    print(ot)
else : 
    print(r * h)