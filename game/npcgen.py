from random import randint as r
from main import menu
class NPCgen:

    def __init__(self, type = "npc", enemy = False):
        validTypes = ["Player", "Enemy", "NPC", "Boss"]
        self.getType = input("Enter type (Player, Enemy, NPC, Boss)\n > ")
        if self.getType not in validTypes:
            raise "Error, not a valid character type"
        else:
            self.charInfo = {"Type": self.getType, "Stats": 
            {"Vitality": 0, "Stamina": 0, "Strength": 0, "Dexterity": 0, "Attunement": 0, "Speech": 0}}
            self.assignStats(self.getType)
        
    def assignStats(self, char):
        statPts = 10
        statmsg = "Assinging stats to {}. {} Points remaining".format(char, statPts)
        print(statmsg, self.charInfo)
        while statPts != 0:
            selectStat = input("Choose a stat to add a skill pt:\nVitality\nStamina\nStrength\nDexterity\nAttunement\nSpeech\n > ")
            selectAmount = int(input("How many Stat Points to add?\n > "))
            self.addStatPoint(selectStat, selectAmount)
            statPts -= selectAmount
            update = "CURRENT CHAR STATS:\n\t{}\nSTAT PTS REMAINING:{}\n".format(self.charInfo["Stats"], statPts)
            print(update)
        if statPts == 0:
            queryWrite = input("********************\nStats complete. Write to file? y/n\n > ")
            if queryWrite in ["y", "Y"]:
                self.writeCharToFile(self.charInfo)
            else:
                menu()

    
    def addStatPoint(self, stat, amount):
        self.charInfo["Stats"][stat] += amount

    def writeCharToFile(self, charBuild):
        nameChar = input("\tFILE WRITE\nName Character:\n > ")
        charfile = open("CharInfoMaster", 'a')
        charString = "\n*******************\n%s, %s:\nStats:\n%s\n*******************\n" % (nameChar, self.charInfo["Type"], self.charInfo["Stats"])
        print("Writing to file...")
        charfile.write(charString)
        print("Character written!")




