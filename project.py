import random

cargo_locations = [1, 3, 5] 
cargo_weights = [200, 300, 213]  
total_cargo_weight = sum(cargo_weights)
found_cargo_weight = 0

print("Welcome, Martians! Let's find your buried cargo.")
print("Hint: Your cargo is divided into 3 boxes, and the total weight is 713 kg.\n")

def move_boxes(locations):
    return [loc + random.randint(-2, 2) for loc in locations]

while found_cargo_weight != total_cargo_weight:
    print(f"Current total weight found: {found_cargo_weight} kg (needs to be {total_cargo_weight} kg)")
    
    guesses = []
    for i in range(3):
        guess = int(input(f"Enter the kilometer mark for box {i + 1}: "))
        guesses.append(guess)
    
    found_cargo_weight = 0
    for guess in guesses:
        if guess in cargo_locations:
            index = cargo_locations.index(guess)
            found_cargo_weight += cargo_weights[index]
    
    if found_cargo_weight == total_cargo_weight:
        print("\nCongratulations! You found all the boxes.")
        print(f"The cargo was located at {cargo_locations}, with a total weight of {total_cargo_weight} kg.")
    else:
        print("\nIncorrect locations. The boxes are moving to new locations!\n")
        cargo_locations = move_boxes(cargo_locations)

print("Thank you for saving the day! The Martians are grateful.")
