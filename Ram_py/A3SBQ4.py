
my_tuple = (10, 20, 30, 20, 40, 50, 30, 60, 10)


repeated_items = []
for item in my_tuple:
    if my_tuple.count(item) > 1 and item not in repeated_items:
        repeated_items.append(item)


print("Repeated items:", repeated_items)
