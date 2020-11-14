import tkinter as tk
import pyperclip

root = tk.Tk()
root.title("Morse Translator")
root.resizable(width=False, height=False)

Title = tk.Label(root, text="MORSE TRANSLATOR", font="Helvetica 25 bold")
Title.grid(row=0, column=3)

def EngToMoCommand():
    NewWindow = tk.Toplevel(root)
    NewWindow.title("English to Morse Code")
    NewWindow.resizable(width=False, height=False)

    EngToMoTitle = tk.Label(NewWindow, text="English to Morse Code", font="Helvetica 25 bold")
    EngToMoTitle.grid(row=0, column=3)

    tk.Label(NewWindow, text="Text to translate:", font="Helvetica 16").grid(row=1, column=3)

    TextHere = tk.Entry(NewWindow)
    TextHere.grid(row=2, column=3)

    OutLab = tk.Label(NewWindow, text="")
    OutLab.grid(row=4, column=3)


    def ToMorseBut():
        x = TextHere.get()

        def split(x):
            return [char for char in x]

        ToTranslate = split(x)

        MorseList = []

        def TranslateToMorse(ToTranslate):
            for char in ToTranslate:
                if char == "A" or char == "a":
                    MorseList.append(".- ")
                elif char == "B" or char == "b":
                    MorseList.append("-... ")
                elif char == "C" or char == "c":
                    MorseList.append("-.-. ")
                elif char == "D" or char == "d":
                    MorseList.append("-.. ")
                elif char == "E" or char == "e":
                    MorseList.append(". ")
                elif char == "F" or char == "f":
                    MorseList.append("..-. ")
                elif char == "G" or char == "g":
                    MorseList.append("--. ")
                elif char == "H" or char == "h":
                    MorseList.append(".... ")
                elif char == "I" or char == "i":
                    MorseList.append(".. ")
                elif char == "J" or char == "j":
                    MorseList.append(".--- ")
                elif char == "K" or char == "k":
                    MorseList.append("-.- ")
                elif char == "L" or char == "l":
                    MorseList.append(".-.. ")
                elif char == "M" or char == "m":
                    MorseList.append("-- ")
                elif char == "N" or char == "n":
                    MorseList.append("-. ")
                elif char == "O" or char == "o":
                    MorseList.append("--- ")
                elif char == "P" or char == "p":
                    MorseList.append(".--. ")
                elif char == "Q" or char == "q":
                    MorseList.append("--.- ")
                elif char == "R" or char == "r":
                    MorseList.append(".-. ")
                elif char == "S" or char == "s":
                    MorseList.append("... ")
                elif char == "T" or char == "t":
                    MorseList.append("- ")
                elif char == "U" or char == "u":
                    MorseList.append("..- ")
                elif char == "V" or char == "v":
                    MorseList.append("...- ")
                elif char == "W" or char == "w":
                    MorseList.append(".-- ")
                elif char == "X" or char == "x":
                    MorseList.append("-..- ")
                elif char == "Y" or char == "y":
                    MorseList.append("-.-- ")
                elif char == "Z" or char == "z":
                    MorseList.append("--.. ")
                elif char == "1":
                    MorseList.append(".---- ")
                elif char == "2":
                    MorseList.append("..--- ")
                elif char == "3":
                    MorseList.append("...-- ")
                elif char == "4":
                    MorseList.append("....- ")
                elif char == "5":
                    MorseList.append("..... ")
                elif char == "6":
                    MorseList.append("-.... ")
                elif char == "7":
                    MorseList.append("--... ")
                elif char == "8":
                    MorseList.append("---.. ")
                elif char == "9":
                    MorseList.append("----. ")
                elif char == "0":
                    MorseList.append("----- ")
                elif char == ".":
                    MorseList.append(".-.-.- ")
                elif char == ",":
                    MorseList.append("--..-- ")
                elif char == " ":
                    MorseList.append(" / ")
                else:
                    MorseList.append(char)

        def listToString(MorseList):
            OutputMessage = ""
            for ele in MorseList:
                OutputMessage += ele
            return OutputMessage

        TranslateToMorse(ToTranslate)
        listToString(MorseList)
        OutLab["text"] = listToString(MorseList)

        def clipboardbutcom():
            pyperclip.copy(listToString(MorseList))

        clipButton = tk.Button(NewWindow, text="Copy to Clipboard", command=lambda: clipboardbutcom())
        clipButton.grid(row=5, column=3)

    ToMorseButton = tk.Button(NewWindow, text="TRANSLATE!", command=lambda: ToMorseBut()).grid(row=3, column=3)

def MoToEngCommand():
    NewWindow = tk.Toplevel(root)
    NewWindow.title("Morse Code to English")
    NewWindow.resizable(width=False, height=False)

    EngToMoTitle = tk.Label(NewWindow, text="Morse Code to English", font="Helvetica 25 bold")
    EngToMoTitle.grid(row=0, column=3)

    tk.Label(NewWindow, text="Morse Code to translate:", font="Helvetica 16").grid(row=1, column=3)

    TextHere = tk.Entry(NewWindow)
    TextHere.grid(row=2, column=3)

    OutLab = tk.Label(NewWindow, text="")
    OutLab.grid(row=4, column=3)

    def ToEngBut():
        x = TextHere.get()

        def convlist(x):
            li = list(x.split(" "))
            return li

        ToTranslate = convlist(x)

        EngList = []

        def TranslateToMorse(ToTranslate):
            for i in ToTranslate:
                if i == ".-":
                    EngList.append("a")
                elif i == "-...":
                    EngList.append("b")
                elif i == "-.-.":
                    EngList.append("c")
                elif i == "-..":
                    EngList.append("d")
                elif i == ".":
                    EngList.append("e")
                elif i == "..-.":
                    EngList.append("f")
                elif i == "--.":
                    EngList.append("g")
                elif i == "....":
                    EngList.append("h")
                elif i == "..":
                    EngList.append("i")
                elif i == ".---":
                    EngList.append("j")
                elif i == "-.-":
                    EngList.append("k")
                elif i == ".-..":
                    EngList.append("l")
                elif i == "--":
                    EngList.append("m")
                elif i == "-.":
                    EngList.append("n")
                elif i == "---":
                    EngList.append("o")
                elif i == ".--.":
                    EngList.append("p")
                elif i == "--.-":
                    EngList.append("q")
                elif i == ".-.":
                    EngList.append("r")
                elif i == "...":
                    EngList.append("s")
                elif i == "-":
                    EngList.append("t")
                elif i == "..-":
                    EngList.append("u")
                elif i == "...-":
                    EngList.append("v")
                elif i == ".--":
                    EngList.append("w")
                elif i == "-..-":
                    EngList.append("x")
                elif i == "-.--":
                    EngList.append("y")
                elif i == "--..":
                    EngList.append("z")
                elif i == ".----":
                    EngList.append("1")
                elif i == "..---":
                    EngList.append("2")
                elif i == "...--":
                    EngList.append("3")
                elif i == "....-":
                    EngList.append("4")
                elif i == ".....":
                    EngList.append("5")
                elif i == "-....":
                    EngList.append("6")
                elif i == "--...":
                    EngList.append("7")
                elif i == "---..":
                    EngList.append("8")
                elif i == "----.":
                    EngList.append("9")
                elif i == "-----":
                    EngList.append("0")
                elif i == ".-.-.-":
                    EngList.append(".")
                elif i == "--..--":
                    EngList.append(",")
                elif i == "/":
                    EngList.append(" ")
                else:
                    EngList.append(i)

        def listToString(EngList):
            OutputMessage = ""
            for ele in EngList:
                OutputMessage += ele
            return OutputMessage

        TranslateToMorse(ToTranslate)
        listToString(EngList)
        OutLab["text"] = listToString(EngList)

        def clipboardbutcom():
            pyperclip.copy(listToString(EngList))

        clipButton = tk.Button(NewWindow, text="Copy to Clipboard", command=lambda: clipboardbutcom())
        clipButton.grid(row=5, column=3)

    ToEngButton = tk.Button(NewWindow, text="TRANSLATE!", command=lambda: ToEngBut()).grid(row=3, column=3)

def HelpButCommand():
    NewWindow = tk.Toplevel(root)
    NewWindow.title("Help Window")

    HelpTitle = tk.Label(NewWindow, text="Help Window", font="Helvetica 25 bold")
    HelpTitle.grid(row=0, column=3)

    MoEngHelpTit = tk.Label(NewWindow, text="Morse Code to Text", font="Helvetica 16")
    MoEngHelpTit.grid(row=2, column=3)

    MoEngHelp = tk.Label(NewWindow, text="Letters must be separated by a single space (ex: .... .. = hi)\n"
                                         " and words must be separated by a forward slash with a space before and after: "
                                         "' / ' (ex: .... ..  / - .... . .-. . = hi there)")
    MoEngHelp.grid(row=3, column=3)

    EngMoHelpTit = tk.Label(NewWindow, text="Text to Morse Code", font="Helvetica 16")
    EngMoHelpTit.grid(row=5, column=3)

    EngMoHelp = tk.Label(NewWindow, text="Text can simply be entered how you would expect them to be.\nThe only accepted"
                                         " characters are the english alphabet (a-z), numbers (0-9), a period (.), and a comma (,).")
    EngMoHelp.grid(row=6, column=3)

MoToEng = tk.Button(root, text="Morse to Text", font="Helvetica 16", command=lambda: MoToEngCommand())
MoToEng.config(height=5, width=35, bg="grey")
MoToEng.grid(row=1, column=3)

EngToMo = tk.Button(root, text="Text to Morse", font="Helvetica 16", command=lambda: EngToMoCommand())
EngToMo.config(height=5, width=35, bg="grey")
EngToMo.grid(row=2, column=3)

HelpBut = tk.Button(root, text="Help", font="Helvetica 8", command=lambda: HelpButCommand())
HelpBut.config(height=3, width=70, bg="grey")
HelpBut.grid(row=3, column=3)

root.mainloop()
