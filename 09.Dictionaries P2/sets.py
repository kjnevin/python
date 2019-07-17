# farm_animals = {"Sheep","Pigs","Cows"}
# # print(farm_animals)
#  
# for animal in farm_animals:
#     print(animal)
#      
# print("=" * 40)
#  
# wild_animals = set(["Lions","Tigers","Shark"])
# print(wild_animals)
# 
# print("=" * 40)
#  
# wild_animals.add("Horse")
# farm_animals.add("Horse")
# 
# print(sorted(wild_animals))
# print(sorted(farm_animals))

# # print(animals)
# # 
# # empty_set = set()
# # empty_set_2 = {}
# # empty_set.add("a")
# from test.test_builtin import StrSquares
#  
# even = set(range(0,40,2))
# print(sorted(even))
# print(len(even))
#   
# squares_tuple = (4,6,9,16,25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))
#   
# print(even.union(squares))
# print(len(even.union(squares)))
#   
# print(squares.union(even))
#     
# print(even.intersection(squares))
# print(even & squares)
#    
# print(squares.intersection(even))
# print(squares & even)
#    
# even = set(range(0, 40, 2))
# print(sorted(even))
# 
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(sorted(squares))

# print("Even minus squares")
# print(sorted(even.difference(squares)))
# print(sorted(even-squares))
#   
# print("squares minus even")
# print(squares.difference(even))
# print(squares - even)

# squares.discard(4)
# squares.remove(16)
# print(squares)
# 
# squares.discard(8)
# print(squares)

# even = set(range(0,40,2))
# print(sorted(even))
# 
# squares_tuple = (4,6,16)
# squares = set(squares_tuple)
# 
# print(sorted(squares))
# 
# if squares.issubset(even):
#     print("Squares is a subset of even")
# if even.issuperset(squares):
#     print("Even is a subset of squares")

# even = frozenset(range(0,20,2))
# print(even)
# even.add(3)

