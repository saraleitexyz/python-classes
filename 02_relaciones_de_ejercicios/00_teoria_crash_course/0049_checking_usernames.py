from numpy.core.defchararray import lower

current_users = ["Anna", "olivia", "marc", "anthony", "paula"]
new_users = ["pepe", "juana", "anna", "fernando", "anthony"]

copy_current_users = lower(current_users.copy())

for new_user in new_users:
    if new_user.lower() in copy_current_users:
        print(f"{new_user}, you need to enter a new username.")
    else:
        print(f"The username {new_user} is available.")