import shelve

# with shelve.open("bike") as bike:
#     bike["make"] = "Honda"
#     bike["Model"] = "250 dream"
#     bike["colour"] = "red"
#     bike["engine_size"] = 250
#     
#     print(bike["engine_size"])
#     print(bike["colour"])

with shelve.open("bike2") as bike:
#     bike["make"] = "Honda"
#     bike["Model"] = "500 dream"
    bike["colour"] = "red"
    bike["engine_size"] = 500
#      
#     del bike["engin_size"]
#     for key in bike:
#         print(key)
#     
    print('-' * 20)
    
    print(bike["engine_size"])
    print(bike["colour"])
    
    
