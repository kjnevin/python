# cities = ["Adalaide", "Sydney", "Darwin", "Melbourne"]
# 
# with open("cities.txt") as city_file:
#     for city in cities:
#         print(city)
#     
# 
# cities = []
# with open("cities.txt",'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip('\n'))
#         
# print(cities)
# for city in cities:
#     print(city)
# 
# Imelda = "More Mayham","Imelda May", "2013",(
#     (1,"Pulling"),(2,"Pushing"),(3,"Nope"),(4,"Yup"))
# 
# with open("Imelda3", 'w') as imelda_file:
#     print(Imelda, file=imelda_file)

with open("Imelda3.txt", 'r') as imelda_file:
        contents = imelda_file.readline()
        
imelda = eval(contents)

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)