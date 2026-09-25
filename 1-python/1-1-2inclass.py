# Let' write a program to divide up the check among diners in a party.
check_amount = float(input("Enter the restaurant check amount: "))
tip_percent = float(input("Enter the tip percentage: "))
number_of_diners = int(input("Enter the number of diners: "))

# Write a program to input the amount of a restaurant check, tip %, and number of diners
tip_amount = check_amount * tip_percent / 100
total_amount = check_amount + tip_amount
amount_per_diner = total_amount / number_of_diners

# The program should output the total amount with tip, and the amount each diner owes.
print(f"Total amount with tip: ${total_amount:.2f}")
print(f"Amount each diner owes: ${amount_per_diner:.2f}")
