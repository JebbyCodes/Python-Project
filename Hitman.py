
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import random

window = Tk()
window.title('hitman.py')
window.iconbitmap(r'C:\Users\Asala\OneDrive\Documents\Python Scripts\2023 Python\hitman.ico')
window.geometry("400x200+500+300") #"window width x window height + position right + position down"
#scroll = Scrollbar(window)
#scroll.pack()


#logoPath = r"C:\Users\Asala\OneDrive\Documents\Python Scripts\2023 Python\hitmanLogo.png"
logo = ImageTk.PhotoImage(Image.open(r"C:\Users\Asala\OneDrive\Documents\Python Scripts\2023 Python\hitmanLogo.png"))
showLogo = tk.Label(window, image = logo)
showLogo.pack()


restartWindow = Tk()
restartWindow.title('Restart')
restartWindow.iconbitmap(r'C:\Users\Asala\OneDrive\Documents\Python Scripts\2023 Python\restart.ico')
restartWindow.geometry("205x50+900+300") #"window width x window height + position right + position down"

def startPressed():
    startButton.pack_forget()
    getValues()

global filler
filler = "======================================================================================"
#print("You have a gun")


def getValues():
    
    for widget in window.winfo_children():
        widget.destroy()
    

    def hit():
        #print("test", luck)
        hitChance = random.randint(1,100)
        #if hitChance <= luck:
            #print("target has been HIT")
        #else:
            #print("test", luck)
            #print("target MISS")
        print("Target has been HIT" if hitChance <= luck else "target MISS") #Credits to ChatGPT

    def guardLuck():
        print(filler)
        guardChance = 100 - (randGuards * 2)
        print("You will have a", guardChance,"% chance to escape to a higher level")

        guardChancelabel = Label(window, text = f"You will have a {guardChance}% chance to escape to a higher level")
        guardChancelabel.pack()

        escapePromptlabel = Label(window, text="escape? y|n => ")
        escapePromptlabel.pack()

        #escapeConfirmbutton = Button(window, text="enter", command= checkEscapeprompt)
        #escapePrompt = input("escape? y|n => ").lower()

        escapeEntry = Entry(window,text='') # initial entry is blank
        escapeEntry.pack()


        def checkEscapeprompt():
            if escapeEntry.get() == "y":
                escapeEntry.forget()
                escapeConfirmbutton.forget()
               
                showEscapechoice = Label(window, text="[Yes] Selected")
                showEscapechoice.pack()

                escapeChance = random.randint(1,100)
                if escapeChance <= guardChance:
                    print("ESCAPED")
                    print("You now have a clear target.")
                    print(filler)
                    hit()
                else:
                    #print("test", luck)
                    print("CAUGHT")
            elif escapeEntry.get() == "n":
                escapeEntry.forget()
                escapeConfirmbutton.forget()
               
                showEscapechoice = Label(window, text="[No] Selected")
                showEscapechoice.pack()

                print("Bounty Lost: PLACEHOLDER")
            else:
                invalidInputlabel = Label(window,text="INVALID INPUT")
                invalidInputlabel.config(fg="yellow", bg = "black")
                invalidInputlabel.pack()
                fillerLabel = Label(window,text=filler)
                fillerLabel.pack()
                print("INVALID INPUT")
                guardLuck()

        escapeConfirmbutton = Button(window, text="enter", command= checkEscapeprompt)
        escapeConfirmbutton.pack()

        print(filler)
        #if escapePrompt == "y":
            #escapeChance = random.randint(1,100)
            #if escapeChance <= guardChance:
                #print("ESCAPED")
                #print("You now have a clear target.")
                #print(filler)
                #hit()
            #else:
                #print("test", luck)
                #print("CAUGHT")
        #elif escapePrompt == "n":
            #print("Bounty Lost: PLACEHOLDER")
        #else:
            #print("INVALID INPUT")
            #guardLuck()

    print(filler)
    randObject = ["car", "building"]
    randObjectpick = random.choice(randObject)
    print("Your target is in a",randObjectpick)
    Targetlabel = Label(window, text = f"Your target is in a {randObjectpick} ")
    Targetlabel.pack()
    print(filler)

    if randObjectpick == "car":
        speed = random.randint(1,100)
        speedLabel = Label(window, text=f"{speed} mph")
        speedLabel.pack()
        print(speed,"mph")

        print(filler)

        luck = 100 - speed
        chanceTohitLabel = Label(window, text=f"{luck}% chance to hit")
        chanceTohitLabel.pack()
        print(luck,"% to hit")
        hit()
    else:
        print("Go highrise?")
        print(filler)
        randGuards = random.randint(1,20)
        guardAmount = Label(window,text=f"There will be {randGuards} guards around the building and inside")
        guardAmount.pack()
        print("There will be", randGuards, "guards around the building and inside")
        luck = 100 - (randGuards * 2)
        print(luck,"% to escape to a higher level")
        guardLuck()
        #hit()


#getValues()

startButton = Button(window, text="Start", command = getValues)
startButton.pack()



def destroyWindow():
    for widget in window.winfo_children():
        widget.destroy()
    startButton = Button(window, text="Start", command = getValues)
    startButton.pack()

restartButton = Button(restartWindow, text="Restart?", command = destroyWindow)
restartButton.pack()

window.mainloop() # GUI main event loop #
