import os

def practice():
    #create input variables
    name=input("Please enter your name:\n")
    os.system('clear')
    country=input("Please enter your country:\n")
    os.system('clear')
    age=input("Please enter your age:\n")
    os.system('clear')
    hourly_wage=input("Please enter your hourly wage:\n")
    os.system('clear')
    daily_wage=int(hourly_wage)*8
    satisfied=input("Are you satisfied with your current wage?:")
    if satisfied == "yes" or "Yes":
        satisfied=True
    else:
        satisfied=False
    os.system('clear')
    #create final f' string from variables
    os.system('clear')
    final_=f"Hello {name}!\nYou live in {country}\nYou are {age} years old\nYou make {daily_wage} per day\nAre you Satisfied with your current wage? {satisfied}"
    print(final_)




shopping_lst=["Milk","Bread","Eggs","Peanut Butter","Jelly"]
print(shopping_lst)
shopping_lst[3]="Almond Butter"
print(shopping_lst)
shopping_lst.remove("Jelly")
print(shopping_lst)
shopping_lst.append("Coffee")
print(shopping_lst)
