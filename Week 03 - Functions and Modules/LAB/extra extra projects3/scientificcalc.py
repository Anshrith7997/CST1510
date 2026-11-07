print("Scientific Calculator")
print("Select operation:")
print("1. meters to feet")
print("2. inches to centimeters")
print("3. miles to kilometers")
print("4. celsius to fahrenheit")

choice = input("Enter choice (1/2/3/4): ")
value = float(input("Enter value to convert: "))    

if choice == '1':
    result = value * 3.28084
    print(f"{value} meters is equal to {result} feet.")
elif choice == '2':
    result = value * 2.54
    print(f"{value} inches is equal to {result} centimeters.")
elif choice == '3':
    result = value * 1.60934
    print(f"{value} miles is equal to {result} kilometers.") 
elif choice == '4':
    result = (value * 9/5) + 32
    print(f"{value} celsius is equal to {result} fahrenheit.")
else:
    print("Invalid input.")
print("Thank you for using the Scientific Calculator!")


print("knock knock")
response = input("you: ")
print("the cow goes")
response = input("you: ")
print("no the cow goes moo")
print("hahah")