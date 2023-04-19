"""

Running code multiple times

//JS Code for a for loop:
for(let i = 0; i < 100; i++) {

}


for (let fruit of fruits) {


}

"""

#Can loop a certain # of times
#for i in range(100):
#    print(i)

#print(list(range(15)))


#Can loop Through Strings
string_example = "This is a string"

for char in string_example:
    print(char)

# Loop through lists
fruits = ["banana", "apple", "clementine"]

for fruit in fruits:
    print(fruit)

print("-=-=-=-=-=-=-=-=-=-=-=-=-=")

#Sorts your array, string, etc. for you (so long as it knows how to tell if something is bigger/smaller)
for fruit in sorted(fruits):
    print(fruit)

# Loop through something with index kept in mind
for index, fruit in enumerate(fruits):
    print(index, fruit)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=")

# Loop through numbers in steps

for i in range(0, 10, 2):
    print(i)
print(list(range(0,10,2)))


for i in range(10, -1, -1):
    print(i)


# While Loops

counter = 0

while counter <= 10:
    print(counter, "bottles of beer on the wall, ", counter, " bottles of beer")
    print("pass one down, pass it around, ", counter, " bottles of beer on the wall")
    counter+=1



