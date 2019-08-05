p1 = input("P1 - Please input your choice: ").lower()
p2 = input("P2 - Please input your choice: ").lower()

choice =list(["paper","rock","scissors"])

if p1 not in choice:
    print("P1 goof")
if p2 not in choice:
    print("P2 goof")

if choice.index(p1) == (choice.index(p2) + 1)%3:
    print("P2 wins")
if choice.index(p2) == (choice.index(p1) + 1)%3:
    print("P1 wins")