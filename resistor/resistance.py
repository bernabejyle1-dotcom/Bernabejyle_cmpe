def get_resistance_of_material(resistivity, length, area):
    resistance = resistivity * (length / area)
    print("Resistance of material is: ", resistance)
    return resistance

def get_resistance_by_ohms_law(Voltage, Current):
    resistance = Voltage / Current
    print("Resistance is: " + str(resistance)+ "ohms")
    return resistance



# Assuming you have a function like this in resistor.py
# def get_resistance_by_ohms_law(Voltage, Current):
#     resistance = Voltage / Current
#     print("Resistance is: " + str(resistance) + " ohms")
#     return resistance

if __name__ == "__main__":
    get_resistance_by_ohms_law(10, 5)  # Correct function call with positional arguments


