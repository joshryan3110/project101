import random

response = input("Type Y to roll the dice or type N to exit: ")

while response == "y":
    no = random.randint(1,6)
    if(no == 1):
        print("[-----]")
        print("[--O--]")
        print("[-----]")
    if(no == 2):
        print("[-----]")
        print("[-O-O-]")
        print("[-----]")
    if(no == 3):
        print("[--O--]")
        print("[--O--]")
        print("[--O--]")
    if(no == 4):
        print("[-O-O-]")
        print("[-----]")
        print("[-O-O-]")
    if(no == 5):
        print("[O---O]")
        print("[--O--]")
        print("[O---O]")
    if(no == 6):
        print("[-O-O-]")
        print("[-O-O-]")
        print("[-O-O-]")

