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
    "hydrogen": 1.008,
    "helium": 4.0026,
    "lithium": 6.94,
    "beryllium": 9.0122,
    "boron": 10.81,
    "carbon": 12.011,
    "nitrogen": 14.007,
    "oxygen": 15.999,
    "fluorine": 18.998,
    "neon": 20.180,
    "sodium": 22.990,
    "magnesium": 24.305,
    "aluminum": 26.982,
    "silicon": 28.085,
    "phosphorus": 30.974,
    "sulfur": 32.06,
    "chlorine": 35.45,
    "argon": 39.948,
    "potassium": 39.098,
    "calcium": 40.078,
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
