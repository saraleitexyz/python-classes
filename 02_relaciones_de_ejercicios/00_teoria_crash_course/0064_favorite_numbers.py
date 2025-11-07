# Favorite Numbers: Modify your program from Exercise 6-2 (page 99) so each
# person can have more than one favorite number. Then print each person’s name along
# with their favorite numbers.

favorite_numbers = {
    'mark': [3, 2, 8],
    'sarah': [9, 6],
    'daniel': [5, 7]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"{number}")