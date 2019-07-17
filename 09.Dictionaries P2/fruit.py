fruit = {"Orange": "a sweet, orange citrus fruit",
         "Apple": "Round fruit used to make cider",
         "Banana": "Yellow fruit, used to make sandwiches",
         "Pear": "Wired shaped fruit",
         "Lime": "a sour green fruit"}

print(fruit)

veg = {"cabbage" : "a child's fav",
       "sprouts" : "yuck",
       "spinage" : "yummmy"
       }
print(veg)

veggy = veg.copy()
veggy.update(fruit)
print(veggy)