elements_atomic_numbers = {
    "hydrogen": 1,
    "helium": 2,
    "lithium": 3,
    "beryllium": 4,
    "boron": 5,
    "carbon": 6,
    "nitrogen": 7,
    "oxygen": 8,
    "fluorine": 9,
    "neon": 10,
    "sodium": 11,
    "magnesium": 12,
    "aluminum": 13,
    "silicon": 14,
    "phosphorus": 15,
    "sulfur": 16,
    "chlorine": 17,
    "argon": 18,
    "potassium": 19,
    "calcium": 20,
}


element_atomic_mass = {
    "hydrogen": 1,
    "helium": 4,
    "lithium": 7,
    "beryllium": 9,
    "boron": 11,
    "carbon": 12,
    "nitrogen": 14,
    "oxygen": 16,
    "fluorine": 19,
    "neon": 20,
    "sodium": 23,
    "magnesium": 24,
    "aluminum": 27,
    "silicon": 28,
    "phosphorus": 31,
    "sulfur": 32,
    "chlorine": 35,
    "argon": 40,
    "potassium": 39,
    "calcium": 40,
}

def electron_finder():
    ele_choice = input("Enter Element name: ")
    print(f"The Electrons in {ele_choice} is {elements_atomic_numbers[ele_choice]}")

def proton_finder():
    ele_choice = input("Enter Element name: ")
    print(f"The Protons in {ele_choice} is {elements_atomic_numbers[ele_choice]}")

def atomic_number_finder():
    ele_choice = input("Enter Element name: ")
    print(f"The Atomic Number of {ele_choice} is {elements_atomic_numbers[ele_choice]}")

def atomic_mass_finder():
    ele_choice = input("Enter Element name: ")
    print(f"The Atomic Mass of {ele_choice} is {element_atomic_mass[ele_choice]}")

def neutron_finder():
    ele_choice = input("Enter Element name: ")
    print(f"The neutron in {ele_choice} is {element_atomic_mass[ele_choice] - elements_atomic_numbers[ele_choice]}")

def distribution_electrons():
    ele_choice = input("Enter Element name: ")
    k = 0
    l = 0
    m = 0
    n = 0
    electron = elements_atomic_numbers[ele_choice]
    # Fill K shell (max 2)
    if electron > 0:
        k = min(electron, 2)
        electron -= k

    # Fill L shell (max 8)
    if electron > 0:
        l = min(electron, 8)
        electron -= l

    # Fill M shell (max 8 for elements up to Calcium)
    if electron > 0:
        m = min(electron, 8)
        electron -= m

    # Fill N shell (remaining electrons)
    if electron > 0:
        n = electron

    print(
        f"\nElectron Distribution for {ele_choice} (Atomic Number: {elements_atomic_numbers[ele_choice]}):"
    )
    print(f"K shell: {k}")
    print(f"L shell: {l}")
    print(f"M shell: {m}")
    print(f"N shell: {n}")

distribution_electrons()