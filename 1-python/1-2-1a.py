PASSWORD = "secret" #Constant - Holds a fixed configuration, key, or default value that shouldn't change while the script runs.
success = False #Not a capital SUCCESS 
for attempt on range(5):
  your_password = input("Enter the password: ") #True variable - Holds dynamic data that changes based on user input, program state, or calculations.
  if your_password = PASSWORD:
    print("Access granted:")
    success = True
    break #Stops an iteration when you enter the password
  else:
      print("Access denied")
    
print(f"Attempt {attempt + 1} of 5")

if not success:
    print("You are locked out")
