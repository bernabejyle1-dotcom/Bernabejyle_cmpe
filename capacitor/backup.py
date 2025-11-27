def get_capacitance_by_material(Permeability, Area, Distance):
    dielectricCon = 8.854 *10e-12 #f/n
    capacitance = (Permeability * dielectricCon * Area) / distance
    print(f"Capacitance of Material is: {Capacitance}")
    return capacitance

def get_capacitance_by_CV(Charge, Voltage):
    capacitance = Charge / Voltage
    print(f"Capacitance by CV: {Capacitance}")
    return capacitance


def get_capacitance_current(capacitance, dvoverdt)
    1c = capacitance * dvoverdt
    print(f"Capacitor current: {ic}")
    return ic


def get_capacitive_reactant(volatage, current):
    reactance = 1 / (2 * math.pi * frequency * capacitance)
    print("Capacitive reactance is: ", reactance)
    return reactance

if __name__ == "__main__"
    get_capacitance_by_CV(Charge: 0.05, Voltage: 5)