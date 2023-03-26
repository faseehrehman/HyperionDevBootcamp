#Ask user to input their full name
while True:
    fullname = input("Please enter your full name: ")
   #If input is blank
    if not fullname:
            print("You haven't entered anything. Please enter your full name")
    #If input is less than 4 characters
    elif len(fullname) < 4:
        print("You have entered less than 4 Characters. Please make sure you enter your full name")
    #if input is greater than 25 characters
    elif len(fullname) > 25:
        print("You have entered more than 25 characters. Please make sure you have only entered your full name")
    #if input is correct
    else: 
        print("Thank you for entering your name")