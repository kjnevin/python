import pickle
# # 
# # imelda = ('More Mayhem', 'Imelda May','2011',((1,"pushing"),(2, "shoving"),(3,'pulling'),(4,'nope')))
# # 
# # 
# # with open('Imelda.pickle','wb') as pickle_file:
# #     pickle.dump(imelda, pickle_file)
# 
# # 
# # with open('Imelda.pickle','rb') as imelda_pickled:
# #     imelda2 = pickle.load(imelda_pickled)
# # 
# # print(imelda2)
# # album,artist, year, track_list = imelda2
# # 
# # print(album)
# # print(artist)
# # print(year)
# # for track in track_list:
# #     track_number, track_title =track
# #     print(track_number,track_title)
# 
# import pickle
#  
# imelda = ('More Mayhem', 'Imelda May','2011',((1,"pushing"),(2, "shoving"),(3,'pulling'),(4,'nope')))
#  
# even = list(range(0,10,2))
# odd = list(range(1,10,2))
#  
# with open('Imelda.pickle','wb') as pickle_file:
#     pickle.dump(imelda, pickle_file, protocol = pickle.HIGHEST_PROTOCOL)
#     pickle.dump(even,pickle_file, protocol = 0)
#     pickle.dump(odd,pickle_file, protocol = pickle.DEFAULT_PROTOCOL)
#     pickle.dump(2998302,pickle_file, protocol = pickle.DEFAULT_PROTOCOL)
# 
# with open('Imelda.pickle', 'rb') as imelda_pickled:
#     imelda2 = pickle.load(imelda_pickled)
#     even_list = pickle.load(imelda_pickled)
#     odd_list = pickle.load(imelda_pickled)
#     x = pickle.load(imelda_pickled)
#  
# print(imelda2)
# album, artist, year, track_list = imelda2
#  
# print(album)
# print(artist)
# print(year)
# for track in track_list:
#     track_number, track_title = track
#     print(track_number, track_title)
# 
# print("--"*20)
# 
# for i in even_list:
#     print(i)
#         
# print("--"*20)
# 
# for i in odd_list:
#     print(i)
#     
# print("--"*20)
# 
# print(x)

pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR.")




