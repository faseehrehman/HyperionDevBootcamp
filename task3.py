#create variables for input and store the data (all time in minutes)
swimming_time = int(input("Please enter the time for the swimming event (Enter in Minutes)"))
cycle_time= int(input("Please enter the time for the cycle event (Enter in Minutes)"))
run_time= int(input("Please enter the time for the run event (Enter in Minutes)"))


#calculate total time taken to complete the triathalon
total_time = swimming_time + cycle_time + run_time

#determine the award for participant

#within qualifying time
if total_time <= 100:
    award = "Provincial colours"
#within 5 minutes
elif total_time <= 105:
    award = "Provincial half colours"
#within 10 minutes
elif total_time <= 110:
    award = "Provincial scroll"
#more than 10 minutes
else:
    award = "No award"

#Display the award the participant will recieve

print("The participant will receive a", award.upper(), "award.")
