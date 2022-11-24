# Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

# for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.read().splitlines()

# Replace the [name] placeholder with the actual name.
for name in names:
    updated_letter = letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/{name}.txt", "w") as new_letter:
        new_letter.write(updated_letter)
