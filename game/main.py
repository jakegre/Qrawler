from room import *
from npcgen import *

def operGet():
    oper = input("[T]est\n[P]lay\n[O]ptions\n[Q]uit\n > ")
    return oper
def menu():
    print("************************\nMENU, select an operation:")
    op = operGet()
    operGet = input("[T]est\n[P]lay\n[O]ptions\n[Q]uit\n > ")
    if op in ["t","T"]:
        newNPC = NPCgen()
        operGet = input("[T]est\n[P]lay\n[O]ptions\n[Q]uit\n > ")
    if op in ["O","o"]:
        print("NO OPTIONS YET LOL! FIXME!")
        operGet()
    if op in ["P","p"]:
        print("ADD THE GAME!")
        operGet()

        

if __name__ == "__main__":
    print("\n\n***************\nRunning Main Test Module...\n***************\n\n")
    testSelect = input("Enter M for Menu\nEnter Q to quit\n > ")
    if testSelect in ["m", "M"]:
        menu()
    elif testSelect in ['r', 'R']:
        makeRoom()
    elif testSelect in ['N', 'n']:
        type = input("Enter enemy type to create: [Player, Enemy, NPC, Boss]\n > ")
    elif testSelect in ['Q', 'q']:
        print("Bye!")
    

