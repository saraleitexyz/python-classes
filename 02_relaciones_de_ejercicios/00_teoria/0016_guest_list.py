guest_list = ["Iker Jimenez", "Aitana", "Quevedo"]
print(f"You're invited to the dinner, {guest_list[0]}.")
print(f"You're invited to the dinner, {guest_list[1]}.")
print(f"You're invited to the dinner, {guest_list[2]}.")

print(f"{guest_list[1]} can't come!")

guest_list[1] = "Katy Perry"

print(f"You're invited to the dinner, {guest_list[0]}.")
print(f"You're invited to the dinner, {guest_list[1]}.")
print(f"You're invited to the dinner, {guest_list[2]}.")

print("I found a bigger dinner table!")
guest_list.insert(0, "Elon Musk")
guest_list.insert(2, "Sara Carbonero")
guest_list.append("Omar Montes")

print(f"You're invited to the dinner, {guest_list[0]}.")
print(f"You're invited to the dinner, {guest_list[1]}.")
print(f"You're invited to the dinner, {guest_list[2]}.")
print(f"You're invited to the dinner, {guest_list[3]}.")
print(f"You're invited to the dinner, {guest_list[4]}.")
print(f"You're invited to the dinner, {guest_list[5]}.")

print("Sorry, I can only invite two people for dinner!")
removed_guest1 = guest_list.pop()
print(f"You're no longer invited to the dinner, {removed_guest1}.")
removed_guest2 = guest_list.pop()
print(f"You're no longer invited to the dinner, {removed_guest2}.")
removed_guest3 = guest_list.pop()
print(f"You're no longer invited to the dinner, {removed_guest3}.")
removed_guest4 = guest_list.pop()
print(f"You're no longer invited to the dinner, {removed_guest4}.")

print(f"You are still invited, {guest_list[0]}")
print(f"You are still invited, {guest_list[1]}")
print(f"I'm inviting {len(guest_list)} people.")

del guest_list[1]
del guest_list[0]

print(guest_list)
