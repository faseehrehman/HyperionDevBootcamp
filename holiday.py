# def funct cost of the hotel  
def hotel_cost(num_nights):
    return num_nights * 70

#def funct cost of the flight cost
def plane_cost(city_flight):
    if city_flight == "Dubai":
        return 200
    elif city_flight == "London":
        return 790
    elif city_flight == "Paris":
        return 535
    elif city_flight == "Venice":
        return 458
    else:
         return 0
        
#def funct cost of car rental
def car_rental(rental_days):
    cost = rental_days * 50
    if rental_days >= 7:
        cost -=50
    elif rental_days >= 3:
        cost -= 20
    return cost

#Get user input - Details of holiday
city = input("Enter the city you wish to travel to")
num_nights = int(input("Enter the number of nights you will be staying"))
rental_days = int(input("Please enter the number of days you will be renting a car"))

#Calc total cost
total_cost = hotel_cost(num_nights) + plane_cost(city) + car_rental(rental_days)

#print all details of holiday and total cost
print("Your total cost is:\nCity Flight Cost: $", plane_cost(city), "\nHotel Cost: $", hotel_cost(num_nights), "\nCar Rental Cost: $", car_rental(rental_days), "\nTotal Cost: $", total_cost)
