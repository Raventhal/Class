biggest = -1
print("Before", biggest)
for numb in [52, 5, 7, 6, 43, 88, 9, 7, 3, 45]:
    if numb > biggest:
        biggest = numb
    print(biggest, numb)
print ("After", biggest)