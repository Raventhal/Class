TheDict= {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 100: 'one hundred'}
TheSuck= {2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
def pop():
	dumb = str(numb)
	x = dumb[0]
	y = dumb[1]
#	x = list(map(int, y))
	z = TheSuck.get(int(x))
	v = TheDict.get(int(y))
	print(z + "‐" + v)



while True:
	try:
		numb= int(input("Convert a number to word 1-100! 0 to quit: "))
		if numb == 0:
			break	
		elif numb == 16:
			print("Sweet", TheDict.get(numb) +"!")
		elif (numb < 0 or numb > 100):
			print("Number out of range!")
		elif numb == 100:
			print("You like big number", TheDict.get(numb), "huh?")
		elif numb <= 20:
			print(TheDict.get(numb))
		elif (numb >= 21 and numb <= 99):
			pop()
		
			
			
			
			
	except:
		print("Wrong bud!")
