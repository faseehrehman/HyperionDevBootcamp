numbers = []
while True:
    num = int(input("Enter a number (-1 to stop): ")) #get user input 
    if num == -1:
        break
    numbers.append(num) #add numbers to a list

if numbers:
    avg = sum(numbers) / len(numbers) # calculate numbers
    print(f"Average of numbers entered (excluding -1): {avg}")
else:
    print("No numbers entered.")


