import mymodule # When you run it, you should see "Hello from mymodule!"

print(mymodule.country) # This should print "USA"

import mymodule as mm # Just a way to rename the module when you import it
# Import with an alias so you can use mm instead of mymodule
print (mm.country) # This should also print "USA"

mm.say_hi("Alice") # This should print "Hi, Alice!"

from mymodule import say_hi # This imports only the say_hi function from mymodule
# Import by cherrypicking the function you want to use from the module
say_hi("Bob") # This should print "Hi, Bob!"

from mymodule import say_hi as greet # This imports the say_hi function but renames it to greet
greet("Charlie") # This should print "Hi, Charlie!"
print(mymodule.country) # This should print "USA"

'''
The code that is inline but the functions and variables are in the module. 
The module is imported and then the functions and variables are used from the module.
'''

import mymodule # When you run it, you should see "Hello from mymodule!"

import mymodule
print (__name__)
print(mymodule.__name__) # This should print "mymodule" because the module is being imported, not run directly

mymodule.cheese.say_cheese() # This should print "Cheese!" when the function is called