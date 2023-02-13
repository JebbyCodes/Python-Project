import random

global filler
filler = "======================================================================================"
#print("You have a gun")


def getValues():

    def hit():
        #print("test", luck)
        hitChance = random.randint(1,100)
        #if hitChance <= luck:
            #print("target has been HIT")
        #else:
            #print("test", luck)
            #print("target MISS")
        print("Target has been HIT" if hitChance <= luck else "target MISS") #Credits to ChatGPT#

    def guardLuck():
        print(filler)
        guardChance = 100 - (randGuards * 2)
        print("You will have a", guardChance,"% chance to escape to a higher level")
        escapePrompt = input("escape? y|n => ").lower()
        print(filler)
        if escapePrompt == "y":
            escapeChance = random.randint(1,100)
            if escapeChance <= guardChance:
                print("ESCAPED")
                print("You now have a clear target.")
                print(filler)
                hit()
            else:
                #print("test", luck)
                print("CAUGHT")
        elif escapePrompt == "n":
            print("Bounty Lost: PLACEHOLDER")
        else:
            print("INVALID INPUT")
            guardLuck()

    print(filler)
    randObject = ["car", "building"]
    randObjectpick = random.choice(randObject)
    print("Your target is in a",randObjectpick)
    print(filler)

    if randObjectpick == "car":
        speed = random.randint(1,100)
        print(speed,"mph")

        print(filler)

        luck = 100 - speed
        print(luck,"% to hit")
        hit()
    else:
        print("Go highrise?")
        print(filler)
        randGuards = random.randint(1,20)
        print("There will be", randGuards, "guards around the building and inside")
        luck = 100 - (randGuards * 2)
        print(luck,"% to escape to a higher level")
        guardLuck()
        #hit()



getValues()

