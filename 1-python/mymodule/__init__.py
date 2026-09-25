if __name__ == "__main__": # This checks if the module is being run directly or imported
    print("Hello from mymodule!")

print("Hello from mymodule!")

country = "USA" # Variable that is in mymodule

def say_hi(name: str):
    """Function that is in mymodule"""
    print(f"Hi, {name}!") # This should print a greeting with the name


if __name__ == "__main__": # This checks if the module is being run directly or imported
    print("Goodbye from mymodule!") # This should print a goodbye message when the function is called

    '''
    __name__ is when you run the module directly, it will be "__main__". 
    If you import the module, it will be "mymodule". 
    This is a way to check if the module is being run directly or imported.
    '''

def area_of_rectangle(length: float, width: float) -> float:
    """Function that calculates the area of a rectangle"""
    return length * width # This should return the area of the rectangle

def test_area_of_rectangle():
   length = 10
   width = 5
   expect = 50
   actual = area_of_rectangle(length, width)
   assert actual == expect, f"Expected {expect}, but got {actual}" # This should raise an AssertionError if the actual value is not equal to the expected value

if __name__ == "__main__":
    print("Running tests...")
    test_area_of_rectangle() # This should run the test function and raise an AssertionError if the actual value is not equal to the expected value