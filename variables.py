"""
Javascript:

const, let, var for variables

var x = "This is in the global scope"
console.log(x)

function testFunction() {
    let x = "This is in the scope of testFunction"
    return x
}


console.log(x)
console.log(testFunction())

"""

# Instantiating a new variable in python doesn't require a datatype,
# or a const, let, var keyword - python does all the interpreting for you
x = "This is in the global scope"
print(x)


def testFunction():
    x = "This is in the scope of testFunction"
    return x


print(testFunction())


# Datatypes
number = 10 # an int (short for integer)
float_example = 10.5 # a float (a number with a decimal)
string_example = "This is a string" # it's a string
boolean_example = True # True for true value, False for false value

# Data Structures 

#Lists - can add, remove, and access variables by index and value
list_example = [1, 2, 3]
list_example.append(4)
print(list_example)
print(list_example[2])
list_example.remove(2)
print(list_example)

#Dicts - key value pairs, access specific entry with []
dict_example = {'firstName': 'Lebron', 'lastName':'James', 'lovesClass': True}
print(dict_example)
print(dict_example['firstName'])
