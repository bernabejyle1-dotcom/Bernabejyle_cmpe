import math

def get_capacitance_by_material(Permeability, Area, Distance):
    dielectricCon = 8.854e-12   # F/m
    capacitance = (Permeability * dielectricCon * Area) / Distance
    print(f"Capacitance of Material is: {capacitance}")
    return capacitance


def get_capacitance_BY_CV(Charge, Voltage):
    capacitance = Charge / Voltage
    print(f"Capacitance by C/V: {capacitance}")
    return capacitance


def get_capacitance_current(capacitance, dvoverdt):
    ic = capacitance * dvoverdt
    print(f"Capacitor current: {ic}")
    return ic


def get_capacitive_reactant(voltage, frequency, capacitance):
    reactance = 1 / (2 * math.pi * frequency * capacitance)
    print(f"Capacitive reactance is: {reactance}")
    return reactance


# Optional test
if __name__ == "__main__":
    get_capacitance_BY_CV(0.05, 5)
