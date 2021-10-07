# There will be three main steps:
# 1- Get information from user
# 2- Calculate number of payments
# 3- Present information to user

# Get information from user
name = input("What is your name? ")
item = input("What are you saving for? ")
cost = float(input("OK, "+name+". Please enter the cost of the "+item+": "))
saved = float(input("How much have you already saved? :"))
balance = cost - saved
period = input("How often will you save (day, week, month)? ")
# Put a float here or the input will be a string (can't do math with strings)
# Make sure balance is a non-negative number
if (balance < 0):
    print("Looks like you saved enough")
    balance = 0 
    payment = 1
else:    
    payment = float(input("Enter how much you will save each "+period+": "))
# We need to validate the input that it isn't 0
if (payment <= 0):
    payment = float(input("Enter a nonzero value"))
    if (payment <= 0):
        print(name+", nope, let's assume 1 per "+period+".")
        payment = 1
# Calculate number of payments that will be needed
num_remaining_payments = int(balance/payment)
if (num_remaining_payments < balance/payment):
    num_remaining_payments = num_remaining_payments + 1
# Present information to user
if (balance > 0):
    print(name+", if you save", payment, "each "+period+", you must make", num_remaining_payments, "more payments, and then you'll have your "+item+"!")
else:
    print("Transaction Completed")
