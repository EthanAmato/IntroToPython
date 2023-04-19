"""

Get user input from a console


f-Strings are similar to ` ${varName}` in Javascript
or String.format() in Java

"""

# inputs ALWAYS cast the user answer to a string datatype
user_input = input("What is your favorite number: ")
print("The user said: ", user_input)

print("Lets do some math with the user's favorite number")
print(f"{user_input}")


print(type(user_input))
user_input_as_number = int(user_input)
print(type(user_input_as_number))

print(f"If we were to try to add 100 to it you would get {user_input_as_number + 100}")
