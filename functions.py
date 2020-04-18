def square(x):
    return x * x

# If, for example, functions.py also included the example loop demonstration of the square function, 
# that loop would be executed every time square was imported from functions, 
# because the Python interpreter reads through the entire functions.py file. 
# To remedy this, code that should only run when their containing file is run 
# directly should be encapsulated in a function, called, for example, main. 
# After, the following should be appended:

def main():
    for i in range(10):
        print("{} squared is {}".format(i, square(i)))

if __name__ == "__main__":
    main()
