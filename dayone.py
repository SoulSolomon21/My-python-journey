# this is the print function in python
print("Hello world")
print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")
  
#this is how variable definition is done in python
character_name = "John"
character_age = "70"
print("There once was a man named " + character_name + " ,")
print("he was " + character_age +" years old.")
#since they are variables, they can be changed midway the program
character_name = "Timmy"
character_age = "30"
print("He really liked the name " + character_name + ", ")
print("but he didnt like being " + character_age + " .")

#datatypes- string, numbers, booleans e.g
character_name = "John"
character_age = 70
characters_age = 50.45636
isMale = True
 
#working with strings
print("Sekamatte \n \" Soul \" \n Solomon")
#in python we can also store/create string variables
phrase = "I am Soul "
phrase2 = "Solomon Sekamatte"
#this is how we print out string variables
print(phrase)
#this is how we do string concatenation in python we can add two or more strings as shown below
print(phrase + phrase2 + " and I am cool")

#python also functions that work with strings as shown below
#the function below transforms all the text in the string to upper case
print(phrase2.upper())
#this function checks whether the string is in upper case and it gives a true or false value
print(phrase2.isupper)
#we can also combine functions as below
print(phrase2.upper().isupper)
#we can also use functions to find the length of a string ie the length function
print(len(phrase2))
#we can also get individual characters in a string or find the inidices of the characters in the string
print(phrase2[0])#this would give me the first character in the string
print(phrase2.index("k"))#this would give me the index of the letter k in the string
print(phrase2.index("Solo"))#this would give me where that string of characters starts in the string i have given the program
#the function below is used to replace certain characters/strings in the string that has been given
print(phrase2.replace("Solomon", "King"))#the first parameter is the what you want to replace, the second one is what you want to replace it with

#working with numbers
print(2)# this prints out a number whether +ve, -ve or decimal
print(200%15)#we can do all types of mathematical calculations in this print function
print((2*8)+5-(23/8))
# we can store numbers inside variables as shown below and then print them out
my_number = 44
print(my_number)
# we can also convert numbers into strings using the str keyword. this is especially important when we want to print out a number variable together with a string
print(str(my_number) + " is my favorite number")

#common math Functions used when working with numbers in python

#abs function, gives the absolute value of a number
my_num1 = -1234
print("The absolute value of my_num is " +  str(abs(my_num1)))
#pow function gives the power of a number, the first value is the number and the second is the power we want to raise it to
print("2 to the power of 3 is " +  str(pow(2,3)))
#max function returns the largest of the numbers that we pass into it
print("the bigger of the numbers 21 and 19 is " +  str(max(21,19)))
#min function gives you the smaller of the numbers you have given it
#round function rounds off a number to the nearest whole number
print("32.233 rounded to the nearest whole number is " + str(round(32.233)))

#in order to use to use some special math functions we need to import them into our program as shown below
from math import *
#we have the floor function which gives the number below the one we have put in
print("the floor of the number 3.4 is " + str(floor(3.4)))
#we have the ceil function which gives the number above the one we have put in
print("the ceiling of the number 3.4 is " + str(ceil(3.4)))
#we have the sqrt function which gives the number below the one we have put in
print("the squareroot of the number 265 is " + str(sqrt(265)))

#getting input from the user
#to get input from the user we use the input function and inside the input function, we put a prompt
#in order to store the users input, we equate the input function to a variable as shown below
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + " !\n" + "Your age is " + str(age) + ".")
#when we get input from a user, python takes it to be a string by default

num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
#if i just did this, python would treat them as string and just stick one number to the end of the other
#result = num1 + num2
#to add the two numbers , i need to convert the srings into numbers by adding int.
#the above only works for integer numbers; to make it work, we can use the float function
# result = int(num1) + int(num2)
result = float(num1) + float(num2)
print(result)

#madlibs game
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity_name = input("Enter a celebrity name: ")

print("Roses are " + color + " , ")
print(plural_noun + " are blue, ")
print("I love " + celebrity_name)

#lists
#these work alot like arrays, only that we can store different datatypes inside of these lists
friends = ["Desire", "Sayed", "Soul", "Charles", "Sarah", "Peter"]
example_list = ["Soul", False, 22]
example_list[1] = "Davis" #this is how we modify elements in the list

#this is how e access values in different positions
#we can also access elements from the back of the list as shown below
print(friends[0])
print(friends[-1]) #this would be the last element in the list
print(friends[1:]) #this lets us access values from index 1 to the last
print(friends[1:3]) #this is how we select a range of elements in a list

#list functions
friends.extend(example_list) #this adds a list to the end of another list
print(friends)
friends.append("Solomon") #this allows us to append or add another element to the end of the list 
print(friends)
# friends.append(input("Enter a name")) #this is how you can scan and add an item to the end of the list
print(friends)
friends.insert(1, "Kelly") #this function inserts a value at a certain point in the list, this adds the value at that point and the rest of the values get pushed by one index, the first parameter is the index you want to insert the value in and the second one is the value you want to put there
print(friends)
friends.remove("Solomon") #this removes the element from the list 
print(friends)
# friends.clear() #this function removes all the elements in the list
friends.pop() #this removes the last element from the list
print(str(friends.index("Desire")) + " is the index of the element Desire") #the .index function tells you the index of the item in the list
print(friends.count("Soul")) #this function counts how amny times an element appears in a list 
friends.sort() #this sorts the list in ascending order
print(friends)
# friends.reverse() #this reverses the order of the list
friends2 = friends.copy() #this will make another list with the same elements as the first one

#tuples
#its a container for storing multiple bits of data. in daily aplication, tuples are used for data that is never going to change
#to create a tuple, we use parentheses as shown below
coordinates = (4,5) #tuples cant be changed or modified
print(coordinates[0])# this is how we access variables inside a tuple













