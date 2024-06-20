#Task 1: Code Correction
#You are provided with a Python script that is supposed to help in event planning, 
#but it has errors. Identify and fix them.


attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

#Task 2: Venue Selection

#Based on the corrected code from Task 1, further enhance the program 
#to recommend additional facilities like "audio system" or "projector" 
#based on the number of attendees.

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "audio system" if attendees > 50 else "projector" if attendees < 25 else "conference room"
print(venue)

#Task 3: Catering Choices
#Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" 
#if yes, otherwise recommend "Gourmet Meals Caterers".

Meal = input("Would you like vegetarian food: yes or no ")
Meal = "Veggie Delight Caterers" if Meal == "yes" else "Gourmet Meals Caterers"
print(Meal)