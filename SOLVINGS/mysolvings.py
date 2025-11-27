'''
from capacitor import capacitance

print("capacitance calculator")

charge = float(input("Please enter charge"))
voltage = float(input("Please enter voltage"))

capacitance.get_capacitance_BY_CV(charge, voltage)
'''''


from capacitor import capacitance
from resistor import resistance
from inductance import inductor

while True:
    selector = input("Please select calculator: ")

    match selector.upper():
        case "CC_CV":
            print("Capacitance Calculator")

            charge = float(input("Please enter charge: "))
            voltage = float(input("Please enter voltage: "))



            capacitor.get_capacitance_by_CV(charge, voltage)

        case "R_OHM":
            print("Resistance OHM'S LAW")

            current = float(input("Please enter current: "))
            voltage = float(input("Please enter voltage: "))

            resistor.get_resistance_by_ohms_law(voltage, current)

        case "L_REACT":
            print("Inductive Reactance Calculator")

            frequency = float(input("Please enter frequency (HZ): "))



