# import sys
# 
# playerA = input("Input Rock, paper or scissors: ")
# playerB = input("Input Rock, paper or scissors: ")
# 
# 
# def compare(u1, u2):
#     if u1 == u2:
#         return("Its a draw")
#     
#     elif u1 == 'rock':
#         if u2 == 'paper':
#             print("Paper wins")
# 
#     elif u1 == 'rock':
#         if u2 == 'scissors':
#             print('Rock wins')
#                 
#     elif u1 == 'paper':
#         if u2 == 'scissors':
#             print("scissors wins")
# 
#     elif u1 == 'paper':
#         if u2 == 'rock':
#             print("paper wins")
# 
#     elif u1 == 'scissors':
#         if u2 == 'rock':
#             print('Rock wins')
#     
#     elif u1 == 'scissors':
#         if u2 == 'paper':
#             print("paper wins")
#             
#     else:
#         return('invalid input, try again!')
#     sys.exit()
# 
#     
# print(compare(playerA, playerB))
#         

# p1 = input("P1 entry: ")
# p2 = input("P2 entry: ")
# 
# choices = list["paper","rock","scissors"].lower()
# 
# if p1 or p2 not in choices:
#     print("Goof")
# 
# if choices.index(p1) == (choices.index(p2) + 1) % 3:
#     print("Player 2 wins!")
# if choices.index(p2) == (choices.index(p1) + 1) % 3:
#     print("Player 1 wins")

p1 = input("P1 - Please enter your choice: ").lower()
p2 = input("P2 - Please enter your choice: ").lower()

choices = list(["paper", "rock", "scissors"])

if p1 not in choices:
    print("P1 goof")
if p2 not in choices:
    print("P2 goof")

if p1 == p2:
    print("Tie")
    
if choices.index(p1) == (choices.index(p2) + 1) % 3:
    print("P2 wins")
if choices.index(p2) == (choices.index(p1) + 1) % 3:
    print("P1 wins")

