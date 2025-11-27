import math


def get_inductor_by_material(relative_permeability, permeability, area, length, turns):
    inductance = (relative_permeability * permeability * (turns ** 2) * area) / length
    print(f"Inductor value: {inductance} H")
    return inductance


def get_inductive_reactance(frequency, inductance):
    reactance = 2 * math.pi * frequency * inductance
    print(f"Inductive reactance is: {reactance} ohms")
    return reactance


if __name__ == "__main__":
    get_inductive_reactance(
        frequency=1000,
        inductance=0.00025
    )




