# =====================================
# THE DRAGON CAVE
# Change the code in the CUSTOMIZE area!
# =====================================

# --- CUSTOMIZE YOUR DRAGON ---

dragon_name = "Sparky"
dragon_age = 100
favorite_food = "rainbow cupcakes"
treasure = "a golden game controller"

print("Welcome to the Dragon Cave!")
print("My name is", dragon_name)

# Add two print commands:
# 1. Print the dragon's age
# 2. Print the dragon's favorite food



# Draw your dragon using print commands:

print("       / \\")
print("  ____/   \\____")
print(" <    o   o    >")
print("  \\     ^     /")
print("   \\_________/")

# --- GAME CODE ---
# You do not need to change this part.

print()
print("You see two mysterious doors.")
print("Door 1 is glowing blue.")
print("Door 2 is shaking!")

choice = input("Choose door 1 or door 2: ")

if choice == "1":
    print("The door opens...")
    print("You found", treasure + "!")

elif choice == "2":
    print("ROAAAR!")
    print(dragon_name, "jumps out and eats", favorite_food + "!")
    print("Luckily, the dragon wants to be your friend.")

else:
    print("The cave disappears in a cloud of purple smoke!")