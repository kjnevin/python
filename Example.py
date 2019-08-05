ipAdd = input("Please enter an ip address: ")

if ipAdd[-1] != '.':
    ipAdd+= '.'

# print(ipAdd)
seg = 1
seg_len = 0
character = '.'

for character in ipAdd:
    if character == '.':
        print("Segment {} is {} long".format(seg,seg_len))
        seg += 1
        seg_len = 0
    else:
        seg_len += 1