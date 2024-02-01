
#wapp to read an integer and print
#if its even or odd
#try with try except and else



try:
	num = int(input("enter the number"))

except ValueError:
	print("u shud enter integer")
else:
	if num % 2 == 0:
		print("even number")
	else:
		print("odd")


print("bye")