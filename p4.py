#wapp to read the number and square root of number
#try with multiple

try: 
	num = float(input("enter the number"))
	r = num ** 0.5
	msg = round(r,2)
	print("square root",msg)

except ValueError:
	print("integer only")

except TypeError:
	print("interger +ve only")

print("bye")

 