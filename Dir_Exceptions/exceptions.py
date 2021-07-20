
# lets try to open this file wrongly by giving it a wrong name and we get an exception
# f = open('Dir_Exceptions/textFiles.txt')

# This code will throw a general exception which is not good
try:
    f = open('Dir_Exceptions/textFiles.txt')
except Exception:
    pass # print("Sorry this file does not exist")


try:
    f = open('Dir_Exceptions/textFile.txt') # Put in the corect file name
    # var = bad # Add a bad code
except Exception:
    pass #print("Sorry this file does not exist") # We still get file not found 

try:
    f = open('Dir_Exceptions/textFile.txt')
    # var = bad # Add a bad code
except FileNotFoundError: # This block is not executed because its not a file not found exception
    pass #print("Sorry this file does not exist")

# Handle multiple exceptions
try:
    f = open('Dir_Exceptions/textFile.txt')
    # var = bad # Add a bad code
except FileNotFoundError as e: 
    pass # print(e.message) # print correct exception
except Exception as e:
    pass # print(e.message)

# If no code throws an error, we can move onto to the else block
try:
    f = open('Dir_Exceptions/textFile.txt')
    # var = bad # Add a bad code
except FileNotFoundError as e: 
    pass #print(e.message) # print correct exception
except Exception as e:
    pass #print(e.message)
else:
    pass #print(f.read())
    pass #f.close()

# Finally block will run no matter what
try:
    f = open('Dir_Exceptions/textFile.txt')
    # var = bad # Add a bad code
except FileNotFoundError as e: 
    pass #print(e.message) # print correct exception
except Exception as e:
    pass #print(e.message)
else:
    pass #print(f.read())
finally:
    pass #print("Closing file to avoid memory leaks")
    pass #f.close()

# We can raise exceptions
try:
    f = open('Dir_Exceptions/curruptFile.txt')
    if f.name == 'Dir_Exceptions/curruptFile.txt':
        raise Exception
except FileNotFoundError as e: 
    print(e.message) # print correct exception
except Exception as e:
    print('error!')
else:
    print(f.read())
finally:
    print("Closing file to avoid memory leaks")
    f.close()
    
