#SOLVED: get the values from a list of dictionaries: Nested for loop: 
#First, use the for loop: for county_dict in voting_data: to retrieve each dictionary. 
# Then, in the second for loop, use the values() method on the variable county_dict to 
# reference the data in the second for loop in order to get each value.

voting_data = [{"county": "Arapahoe", "registered_voters": 422829}, 
                {"county": "Denver", "registered_voters": 463353},
                {"county": "Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#Question1
#here is the original code:
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

#QUESTION:And here's how you would edit the code to use f-strings.
#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f" I received {my_votes / total_votes * 100}% of the total votes. ")

 #Question2
 # THIS IS HOW THE CODE LOOKS AS YOU DID IT BEFORE WITHOUT F-STRINGG:
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(str(county)+ " " "county has" " " + str(voters)+ " ""registered voters.")


    #Question: THIS IS HOW IT IS USING F-STRINGS TO BE MORE INTUITIVE AND CLEAR
#for county, voters in counties_dict.items():
    #print(f'{county} county has {voters} registered voters.')
