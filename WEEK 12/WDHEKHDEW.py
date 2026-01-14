import time

# Displays of the menu of available unit conversions
def show_menu():
    print("UNIT CONVERTER")
    print("1. Meters to Centimeters")
    print("2. Centimeters to Meters")
    print("3. Kilograms to Grams")
    print("4. Grams to Kilograms")
    print("5. Celsius to Fahrenheit")
    print("6. Fahrenheit to Celsius")
    print("7. Meters to Kilometers")
    print("8. Kilometers to Meters")
    print("9. Liters to Milliliters")
    print("10. Milliliters to Liters")
    print("11. Hours to Seconds")
    print("12. Seconds to Hours")
    print("13. Exit")

# This function displays all available unit conversions options to the user
def meters_to_cm(v): return v * 100
def cm_to_meters(v): return v / 100
def kg_to_grams(v): return v * 1000
def grams_to_kg(v): return v / 1000
def celsius_to_fahrenheit(v): return (v * 9 / 5) + 32
def fahrenheit_to_celsius(v): return (v - 32) * 5 / 9
def meters_to_km(v): return v / 1000
def km_to_meters(v): return v * 1000
def liters_to_ml(v): return v * 1000
def ml_to_liters(v): return v / 1000
def hours_to_seconds(v): return v * 3600
def seconds_to_hours(v): return v / 3600


print("Loading Unit Converter.......................")
time.sleep(1.5)

# This is the main program where i use loop
while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "13":
        print("Exiting program..............................")
        time.sleep(1)
        print("Thank you for using our Unit Converter.")
        break

    try:
        value = float(input("Enter the value you want to convert: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        time.sleep(1)
        continue

#in this part i add units to easily identify the values

    if choice == "1":
        result, unit = meters_to_cm(value), "cm"
    elif choice == "2":
        result, unit = cm_to_meters(value), "m"
    elif choice == "3":
        result, unit = kg_to_grams(value), "g"
    elif choice == "4":
        result, unit = grams_to_kg(value), "kg"
    elif choice == "5":
        result, unit = celsius_to_fahrenheit(value), "°F"
    elif choice == "6":
        result, unit = fahrenheit_to_celsius(value), "°C"
    elif choice == "7":
        result, unit = meters_to_km(value), "km"
    elif choice == "8":
        result, unit = km_to_meters(value), "m"
    elif choice == "9":
        result, unit = liters_to_ml(value), "mL"
    elif choice == "10":
        result, unit = ml_to_liters(value), "L"
    elif choice == "11":
        result, unit = hours_to_seconds(value), "s"
    elif choice == "12":
        result, unit = seconds_to_hours(value), "hr"
    else:
        print("Invalid menu choice.")
        time.sleep(1)
        continue

    print("\nCalculating...")
    time.sleep(1)

    print("Converted value:", round(result, 2), unit)
    time.sleep(1.5)

    print("Arigato!")
    break








