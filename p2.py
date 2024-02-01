#wapp to read an integer and print
#if its even or odd
#try except

try:
	num = int(input("enter the number"))
	if num % 2 == 0:
		print("even number")
	else:
		print("odd")

except ValueError:
	print("u shud enter integer")
print("bye")