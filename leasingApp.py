#Name: Joel Mondal
#Project: Leasing application

# opens intro file
intro = open("intro.txt", "r")
print(intro.read())
#list of apartments
apartmentList= [["(1)Bedroom(1)Bath","1500","800","1" ],
                ["(2)Bedroom(1)Bath","1800","1000","2"],
                ["(2)Bedroom(2)Bath","2000","1200","3"],
                ["(3)Bedroom(2)Bath","2500","1400","4"]]
print("| Apartment Type | Recommended Income | Rent | Option |")
# print apartment list
for choice in apartmentList:
    print(choice[0],"        ",
          choice[1],"      ",
          choice[2],"      ",
          choice[3]," ")
# Takes user input choice    
userChoice=int(input("Which apartment option you would like to apply for: "))
#fail-safe incase user choice is invalid
while userChoice <1 or userChoice>4:
    print("You need to pick a valid option")
    userChoice=int(input("Which apartment option you would like to apply for: "))

#takes user choice of aparment and calls application()          
def choices():

    while userChoice >=1 or userChoice<=4:
        
        if userChoice == 1:
            confirmation=input("You want to apply to our: (1)Bedroom(1)Bath Correct? ")
            if confirmation == 'yes':
                print('Great! Typically you need an credit score of 600 or more for this apartment')
                application()
                break
            else:
                print('Have a good day!')
                break 
        if userChoice == 2:
            confirmation=input("You want to apply to our: (2)Bedroom(1)Bath Correct?")
            if confirmation == 'yes':
                print('Great! Typically you need an credit score of 630 or more for this apartment')
                application()
                break
            else:
                print('Have a good day!')
                break          
        if userChoice == 3:
            confirmation=input("You want to apply to our: (2)Bedroom(2)Bath Correct?")
            if confirmation == 'yes':
                print('Great! Typically you need an credit score of 650 or more for this apartment')
                application()
                break
            else:
                print('Have a good day!')
                break           
        if userChoice == 4:
            confirmation=input("You want to apply to our: (3)Bedroom(2)Bath Correct?")       
            if confirmation == 'yes':
                print('Great! Typically you need an credit score of 680 or more for this apartment')
                application()
                break
            else:
                print('Have a good day!')
                break

# function used in choices() to continue application
#takes user income and credit score
def application():
    userIncome=int(input('What is your income? '))
    
    if userIncome >= 1500 and userChoice==1:
            userScore=int(input('What is your credit score? '))
            if userScore>=600:
                congrats()
                return
            elif userScore<600:
                print('Sorry, credit score too low')
                sorry()
                return
    elif userIncome <1500:
        print('Sorry, your income is too low')
        sorry()
        return
    
    if userIncome >= 1800 and userChoice==2:
            userScore=int(input('What is your credit score? '))
            if userScore>=630:
                congrats()
                return
            elif userScore<630:
                print('Sorry, credit score too low')
                sorry()
                return
    elif userIncome < 1800:
        print('Sorry, your income is too low')
        sorry()
        return
    
    if userIncome >= 2000 and userChoice==3:
            userScore=int(input('What is your credit score? '))
            if userScore>=650:
                congrats()
                return
            elif userScore<650:
                print('Sorry, credit score too low')
                sorry()
                return            
    elif userIncome <2000:
        print('Sorry, your income is too low')
        sorry()
        return
    
    if userIncome >= 2500 and userChoice==4:
            userScore=int(input('What is your credit score? '))
            if userScore>=680:
                congrats()
            elif userScore<600:
                print('Sorry, credit score too low')
                sorry()
                return
    elif userIncome < 2500:                
        print('Sorry, your income is too low')
        sorry()
        return

#calls sorry.txt text face file    
def sorry():
    intro = open("sorry.txt", "r")
    print(intro.read())
#calls conrats.txt face file    
def congrats():
    intro=open("congrats.txt","r")
    print(intro.read())
#runs choices function that takes users choice input
#program wont run properly without function call    
choices()
