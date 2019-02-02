n=input()
if n.isnumeric():
	t=int(n)
	if (t%2==0):
		print("Even")
	else:
		print("Odd")
else:
	print("Invalid")
