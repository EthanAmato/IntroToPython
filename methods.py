


def myFirstMethod():
    print("Inside of method")


myFirstMethod()


def myInputMethod(userString):
    print("The user says: ", userString)

my_message = "Today is a good day"
myInputMethod(my_message)


def myReturnMethod(x, y):
    return x*y

multiplication_result = myReturnMethod(5,10)
print(multiplication_result)
