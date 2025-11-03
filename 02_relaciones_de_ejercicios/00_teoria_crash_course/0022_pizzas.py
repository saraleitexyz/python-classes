pizza_kinds = ["pineapple", "bbq", "cheese and ham"]

for pizza_kind in pizza_kinds:
    print(f"I would like a {pizza_kind} pizza now!")

print("I really love pizza!")

friend_pizzas = pizza_kinds[:]
pizza_kinds.append("burger")
friend_pizzas.append("blue cheese")
print("My favorite pizzas are:")
for pizza_kind in pizza_kinds:
    print(pizza_kind)
print("My friend's favorite pizzas are:")
for pizza_kind in friend_pizzas:
    print(pizza_kind)
