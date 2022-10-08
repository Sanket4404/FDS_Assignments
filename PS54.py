bal = int(input("Enter opening balance : "))




def deposit(amt):
	amt=int(input("Enter deposite amount:"))
	global bal
	fin = bal
	fin = fin + amt
	bal = fin
	return bal
	
def withdraw(amt):
	amt=int(input("Enter withdrawal amount:"))
	global bal
	fin = bal
	if bal <= amt:
		print(" \nInsufficient Funds!!!")
		print("Transaction Unsuccessful")
	else:
		fin = fin - amt
		bal = fin
		print(" \nTransaction Successful")
	return bal

while True:
	sum = 0
	print()
	a = input("Enter command : ")
	if a == "exit" or a == "EXIT":
		print("\nFinal balance is : ", bal)
		exit()
	else:
		for i in range(1, len(a)):
			if a[i].isdigit() == True:
				sum  = sum * 10 + int(a[i])
			else:
				print("Invalid!!!")
				break
		if a[0] == "D":
			bal = deposit(sum)
			print(" \nTransaction Successful")
			print("Balance is : ", bal)
		elif a[0] == "W":
			bal = withdraw(sum)
			print("Balance is : ", bal)
		else:
			print("Invalid Command!!! \n")
