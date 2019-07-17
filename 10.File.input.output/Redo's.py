# cities = ["Adelaide", "Alice Springs","MElbourne","Sydney"]
# 
# with open("cities.txt",'w') as city_file:
#     for city in cities:
#         print(city, file=city_file, flush = True)
# 
# cities = []
# with open("cities.txt",'r') as city_file:
#     for city in city_file:
#         cities.append(city)
#         
# print(cities)
# for city in cities:
#     print(city)

Imelda = "More Mayham","Imelda May", "2013",(
    (1,"Pulling"),(2,"Pushing"),(3,"Nope"),(4,"Yup"))
 
with open("Imelda3.txt", 'w') as imelda_file:
    print(Imelda, file=imelda_file)