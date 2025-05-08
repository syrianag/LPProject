"""
unit4projectpt2

Description:
"""

import random 
## Depending on the project being done the yarn length, hook sizes and prices may vary!
## Create a list made up of strings that identifies different projects that can be done
## Create a substring that identifies possible colors that can be used for the project 
## OR using dictionaries create an unordered key that identifies all the essentials needed for each project EXCEPT FOR CREDIT CARD INFORMATION
## Depending on the amount needed use the list.count to count roles or identify amount that can be bought

crochet_projects = ["Hat", "Plushie", "Bookmark", "Tubtop", "Coaster"]
avaliable_colors = ["Red", "Pink", "Black", "White", "Purple"]
rolls_of_yarn_options = ["1", "2", "3", "4", "5"]
price = ["$15", "$20", "$25", "$30", "$35"]

##Modify Strings 
purchases = []
card_information = []
#Create a while loop to ask questions and recieve answers
adding = True 
while adding:
    user_choice = input ("What would you like to make? (type quit to quit)")
    if user_choice.lower() == "quit":
        print(card_information)
        break
        
    if user_choice not in crochet_projects:
        print("Sorry, that's not an avalible project. Please choose from:", crochet_projects)
        continue
        
    color = input ("Sounds great!! What color yarn would you like to use? ")
    
    if color not in avaliable_colors:
        print("Sorry, we don't have that color. Please choose from:", avaliable_colors)
        continue 
        
    rolls_needed = input ("How many rolls of yarn are needed for your project?")
    
    if rolls_needed not in rolls_of_yarn_options:
        print("Sorry, we only have rolls in quantities:", rolls_of_yarn_options)
        continue 
        
    #Convert rols and price to integers 
    rolls_needed = int(rolls_needed)
    price = random.choice(price)
    
    print("Your total is $" + str(price))
    payment_method = input("Would you like to pay with card or cash?")
    if payment_method.lower() == "card":
          input("Please enter your card information: ")
          input("Would you like a digital or physical receipt?")

                           
    #Save purchase
    purchases.append({
        "project": user_choice,
        "color": color, 
        "rolls": rolls_needed,
        "payment": payment_method
    })
                           
    print("Thank you for your purchase!")
    

    
    

