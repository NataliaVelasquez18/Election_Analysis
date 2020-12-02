print ("Hello World!") 


#Conditionals

    #counties
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])



if counties[2] != 'Jeffersion':
    print(counties[2])


    #temperature
    temperature = int(input("What is the temperature outside?"))

    if temperature > 80:
        print("Turn on the AC.")
    else: 
        print("Open the windows.")


#repetition statements

#iterate through a list

    #for loops
for county in counties:
    print(county)

    #iterate through a tuple

counties_tuple = ("Arapahoe","Denver","Jefferson")
for i in counties_tuple:
    print(i)

    #range
for x in range(len(counties)):
        print(counties[x])


for i in range(len(counties_tuple)):
        print(counties_tuple[i])


#Iterate through a dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

    #get the key only  (method 1)
    
for county in counties_dict:
    print(county)


    #get the key only (method 2)
for county in counties_dict.keys():
    print(county)


#Get the values only

    #Method 1: values()

for voters in counties_dict.values():
    print(voters)


    #method 2: dictionary_name[key] include the key "county" in the for loop

for county in counties_dict:
    print(counties_dict[county])

    #Method 3: get()
for county in counties_dict:
    print(counties_dict.get(county))

#get the key-value pairs of a dictionary

    #method items()
    #for key, value in dictionary_name.items():
        #(key, value)
for county, voters in counties_dict.items():
    print(county, voters)

#Iterate through a list of dictionaries
    #Get each dictionary in a list of dictionaries: we use for loop

voting_data = [{"county": "Arapahoe", "registered_voters": 422829}, 
                {"county": "Denver", "registered_voters": 463353},
                {"county": "Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)

    #use  the range() to iterate over the list of dictionaries

for county_dict in range(len(voting_data)):
        print(voting_data[county_dict])

#get the values from a list of dictionaries: Nested for loop: 
#First, use the for loop: for county_dict in voting_data: to retrieve each dictionary. 
# Then, in the second for loop, use the values() method on the variable county_dict to 
# reference the data in the second for loop in order to get each value.

voting_data = [{"county": "Arapahoe", "registered_voters": 422829}, 
                {"county": "Denver", "registered_voters": 463353},
                {"county": "Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)


#How would you retrieve the number of registered voters from each dictionary?
for county_dict in voting_data:
    print(county_dict["registered_voters"])


#If we only want to print the county name from each dictionary, we can use 
# county_dict['county'] in the print statement for the for loop.
for county_dict in voting_data:
    print(county_dict["county"])


#The print() function
#so far we have used it to print simple statements but it can become
#cumbersome when we need to print items from a list of values from a dictionary.
#this is where F-strings come in.
#F-strings can be used in place of concatenation. This is the format:
    #The f-string begins with an f followed by a string contained within quotes. 
        # (The term f-string comes from the leading "f" character preceding the string literal.)
    #In the f-string, curly braces are used to add variables or expressions to the f-string. Example

#here is the original code:
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

#QUESTION1:And here's how you would edit the code to use f-strings.
#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f" I received {my_votes / total_votes * 100}% of the total votes. ")


#Using F-Strings with Dictionaries
#F-strings can be used to print out 
# the keys or values of a dictionary. This will make our code easier to write and read.

    #THIS IS HOW THE CODE LOOKS AS YOU DID IT BEFORE WITHOUT F-STRINGG:
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(str(county)+ " " "county has" " " + str(voters)+ " ""registered voters.")


    #????Question2: THIS IS HOW IT IS USING F-STRINGS TO BE MORE INTUITIVE AND CLEAR
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#Dependencies: ARE MODULES AND PACKAGES or programing scripts that speed efficiency
#Inside dependencies are functions, classes, or variables.

#?????? Question 3.  Why I get a weird format Import the datetime class from th edatetime module.
import datetime
#use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
#print the present time.
print("The time righ now is ", now)

#Let's break it down:
#To use the datetime module all we need to do is to import it using import datetime.
#In line 4, we declare the now variable to hold the time right "now".
#The now variable is set equal to datetime.datetime.now(), where:
#The first datetime is the datetime module, (first doll).
#The second datetime is the datetime class (second doll).
#Then we use the datetime attribute, now(), (third doll) on the datetime class, i.e., 
#datetime.now(), to get the current time.
#To reduce the confusion on importing a module with the same name as a class we can use an 
#abbreviated alias dt for the datetime module.

#????? Question 4. I get the same weird format: 
# ('The time righ now is ', datetime.datetime(2020, 11, 25, 13, 55, 15, 462925))
#  Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

#PACKAGES are folders that contain a set of python modules.  The folders in the packages may
#contain various subpackages, or other folders. To import packages, use the import statetment as we
#did with the datetime module.

#MODULES: are a separate software component. They are usually Python files with a .py extension
#the name of the module will be the name of the file.  A python module can have functions, classes,
#or variables defined and implemented.
#use by simple statement like import- datetime -. To use a specific function, class, or variable from a 
# module, you use a statement like- from import -.
#If your script requires the use of programs, modules, and packages, one of the first steps is to 
# import dependencies for your Python script.


#The CSV Module
#In Python there's a built-in module called csv, which allows users to easily pull in data 
# from external CSV files and perform operations on them.
#To see all the functions available in the csv module, follow these steps:

#1. Launch the Python interpreter.
#2. Type import csv to import the module.
#3. Press Enter.
#4. Type dir(csv). The "dir" is short for "directory".
#5. The Python interpreter should look like this:

#>>> import csv
#>>> dir(csv)

##OPEN AND READ FILES USING PYTHON:
#There are two ways to read a file in using a programming language: 
# 1.supply
# a direct path to the file or use an indirect path.
import csv

