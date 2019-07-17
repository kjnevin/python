import shelve
# 
# blt = ["Bacon","Lettuce","tomato","bread"]
# beans_on_toast = ["Beans","bread"]
# scrambled_eggs = ["Eggs","bread"]
soup = ["Soup"]
# pasta = ["pasta","cheese"]

with shelve.open('recipes', writeback=True) as recipes:
#     recipes["blt"] = blt
#     recipes["beans on toast"] = beans_on_toast
#     recipes["scrammbled eggs"] = scrambled_eggs
#     recipes["soup"] = soup
#     recipes["pasta"] = pasta
#    
#     recipes["blt"].append("butter")
#     recipes["pasta"].append("tomatoes")

#     temp_list = recipes["blt"]
#     temp_list.append("butter")
#     recipes["blt"] = temp_list
#  
#      
#     temp_list = recipes["pasta"]
#     temp_list.append("tomato")
#     recipes["pasta"] = temp_list
    
#     recipes["soup"].append("croutons")
    recipes["soup"] = soup
    recipes.sync()
    soup.append("cream")
    

    for snack in recipes:
        print("{0} contains {1}".format(snack, recipes[snack]))
