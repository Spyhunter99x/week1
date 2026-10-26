
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice: "))

if choice == 1:
    c = float(input("Enter Celsius: "))
    print("Fahrenheit:", celsius_to_fahrenheit(c))
elif choice == 2:
    f = float(input("Enter Fahrenheit: "))
    print("Celsius:", fahrenheit_to_celsius(f))
else:
    print("Invalid choice!")
