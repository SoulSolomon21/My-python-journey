"""
from turtle import color
from unicodedata import name

fruit_tuple = ('apple', 'banana', 'pear', 'strawbwerry','orange') #this is how you declare a tuple
#values in a tuple are imutable,meaning they cannot be changed
print(fruit_tuple)
print(fruit_tuple.index('apple')) #this displays the index of the particular value passed to it
print(fruit_tuple[2]) #this is how to access data in the tuple

#lists
friends = ["Desire", "Sayed", "Soul", "Charles", "Sarah", "Peter"]
del friends[0] #removes an item from the given index
print(friends)
# friends.append(input("Enter a name: ")) #append adds an element o the end of the list
print(friends)
#the .sort method sorts the elements in the list into alphabetical order
#the sorted() function prints the list sorted in alphabetical order but the actual list remains unchanged
#getting slices from a list . this is done by specifying where the slice should start from and end as shown below
print(friends[1:4])

"""
"""
#dictionaries
#
student = {
    'name': 'Sekamatte Soul Solomon',
    'course': "BSCS",
    'residence': 'Nsibambi',
    'CGPA': 3.69
}

print(student['name']) #this is how you access data from the dictionary
student['residence'] = 'Outside'
print(student)
print(student.get('name')) #this is one way of accesing data inside the dictionary
#if we want to specify a message to be displayed when a key that does not exist is called, we can use the following
print(student.get('phone', 'Not found'))
#to add  a new key value pair to the dictionary we can do as below:
student['Access No.'] = 'A96920'
#the new key value pair is added to the end of the dictionary
print(student)
"""

countries = ('uganda','kenya','sudan','congo','rwanda')
print(countries)

for i in countries:
    print(i)

choice = str(input("Enter one of the countries above: "))

for i in countries:
    if choice == i:
        print({countries.index(choice)})
    # else:
    #     print("The country you have entered is not in the tuple")






