fruit = {"Orange": "a sweet, orange citrus fruit",
         "Apple": "Round fruit used to make cider",
         "Banana": "Yellow fruit, used to make sandwiches",
         "Pear": "Wired shaped fruit",
         "Lime": "a sour green fruit"}


# while True:
#     dict_keys = input("Please enter a piece of fruit: ")
#     if dict_keys == 'quit':
#         print("Enough")
#         break
#     print(fruit.get(dict_keys, "We don't have " + dict_keys))
# 
# for snack in fruit:
#     print("Yummy " + snack + ", "+ fruit[snack])

# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
# 
# print('*' *50)

# order_keys = list(fruit.keys())
# order_keys.sort()
# order_keys = sorted(list(fruit.keys()))
# for f in order_keys:
#     print(f + ' - ' + fruit[f])

# 
# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])
# print(fruit.keys())
# # fruit_keys = fruit.keys()
# 
fruit["Tomato"] = "Great in a sandwich"
print(fruit.keys())

print(fruit)
print(fruit.items())

f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)
    
print(dict(f_tuple))