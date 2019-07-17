import shelve
books = shelve.open("book")

books["recipes"] = {"blt" : ["Bacon",'Lettuce',"tomato"],
                    "beans on toast": ["beans","bread"],
                    "soup": ["can of soup"],
                    "pasta": ["pasta","cheese"]}
books["maintence"] = {"stuck":["oil"],
                      "loose":["gaffer tape"]}

print(books["recipes"])

print(books["maintence"])

books.close()