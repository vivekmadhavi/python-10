#wapp to read the number and square root of number
#try with single exception


try: 
	num = float(input("enter the number"))
	r = num ** 0.5
	msg = round(r,2)
	print("square root",msg)

except Exception:
	print("integer should be +ve only")

print("bye")

 