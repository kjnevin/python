import shelve
books = shelve.open("book")

books["recieps"] = {"blt" : ["bacon", "Lettuce", "tomatoe", "bread"],
                    "Beans on toast": ["beans", "butter", "bread"],
                    "scrambled eggs":["eggs", "bread"],
                    "soup": ["tin of soup"],
                    "pasta": ["pasta", "cheese"]}

books["maintence"] = {"stuck":['oil'],
                     "loose": ["gaffer tape"]}

print(books["recipes"])
# print(books["recipes"]["scrambled eggs"])
# 
# print(books["maintence"]["loose"])
books.close()
