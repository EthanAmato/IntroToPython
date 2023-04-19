

# How to define a function in python
def myFirstMethod():
    print("Inside of method")

#Calling a function is the same as in JS
myFirstMethod()

#Having input parameters is the same as in JS
def myInputMethod(userString):
    print("The user says: ", userString)

my_message = "Today is a good day"
myInputMethod(my_message)

#Return statements work the same as in JS and Java
def myReturnMethod(x, y):
    return x*y

multiplication_result = myReturnMethod(5,10)
print(multiplication_result)
