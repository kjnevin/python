import shelve
# with shelve.open('shelfTest') as fruit:
fruit = shelve.open('ShelfTest')
# fruit['orange'] = "a sweet orange, citrus fruit"
# fruit['apple'] = "good for making cider"
# fruit['lemon'] = "a yellow, citrus fruit"
# fruit['grape'] = "a small, sweet fruit grows in bunches"
# fruit['lime'] = "a sour, green citrus fruit"
    
# print(fruit["lemon"])
# print(fruit["grape"])
# fruit["lime"] = "Great with tequila"
# 
# for snack in fruit:
#     print(snack + ": " + fruit[snack])

# while True:
#     dict_key = input("please enter a key: ")
#     if dict_key == "quit":
#         break
#     
#     if dict_key in fruit:
#         description = fruit[dict_key]
#         print(description)
#     else:
#         print("We don't have any " + dict_key)
# 
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# 
# for f in ordered_keys:
#     print(f + "- " + fruit[f])
#     

for v in fruit.values():
    print(v)
print(fruit.values())
 
for f in fruit.items():
    print(f)
print(fruit.items())
fruit.close()
# print(fruit)
