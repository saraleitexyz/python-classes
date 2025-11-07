# A dictionary of similar objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language}.")

for name in favorite_languages.keys():
    print(name.title())
# for name in favorite_languages works the same, but I like to be explicit.

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("\nThe following languages have been mentioned:")
# Set identifies the unique items in the list and builds a set from those items.
for language in set(favorite_languages.values()):
    print(language.title())

# Make a list of people who should take the favorite languages
# poll. Include some names that are already in the dictionary
# and some that are not.
participants_needed = ['mark', 'elon', 'marina', 'sarah']

# Loop through the list of people who should take the poll. If
# they have already taken the poll, print a message thanking
# them for responding. If they have not yet taken the poll, print
# a message inviting them to take the poll.
for name in participants_needed:
    if name not in favorite_languages.keys():
        print(f"{name.title()} should take the poll.")
    else:
        print(f"{name.title()}, thank you for taking the poll.")