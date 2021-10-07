# There will be three main steps:
# 1- Get information from user
# 2- Calculate number of payments
# 3- Present information to user

# Get information from user
# Put a float here or the input will be a string (can't do math with strings)
balance = float(input("Enter how much you want to save: "))
payment = 1
# Make sure balance is a non-negative number
if (balance < 0):
    print("Looks like you saved enough")
    balance = 0    

if (balance>0):
    payment = float(input("Enter how much you will save each period: "))
# We need to validate the input that it isn't 0
if (payment == 0):
    payment = float(input("Enter a nonzero value"))
# Calculate number of payments that will be needed
# we will not use number of months, simple division here
num_remaining_payments = balance/payment
# Present information to user
if (balance > 0):
    print("You must make", num_remaining_payments, "payments")
else:
    print("Transaction Completed")
