players = ['charles', 'mary', 'john', 'jose', 'juan']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

for player in players[:3]:
    print(player.title())

print(f"The first three items in the list are: {players[:3]}")
print(f"Three items from the middle of the list are: {players[1:4]}")
print(f"The last three items in the list are: {players[-3:]}")