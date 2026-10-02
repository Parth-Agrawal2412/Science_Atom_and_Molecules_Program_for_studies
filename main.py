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


def electron_finder():
    ele_choice = input("Enter Element name: ")
    print(f"The Electron in {ele_choice} is {elements_atomic_numbers[ele_choice]}")

def proton_finder():
    ele_choice = input("Enter Element name: ")
    print(f"The Proton in {ele_choice} is {elements_atomic_numbers[ele_choice]}")

electron_finder()