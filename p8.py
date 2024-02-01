#wapp to read the number and square root of number
#raise
try: 
	num = float(input("enter the number"))
	if num > 0.0 :
		r = num ** 0.5
		msg = round(r,2)
		print("square root",msg)
	else:
		raise Exception("u shud enter _ve number only")

except ValueError :
	print("integer should be +ve only")
except Exception as e :
	print(e)

print("bye")

 