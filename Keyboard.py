import AppOpener
import pyautogui
import pydirectinput


class CleaningUpInput:

    # used to assign values for option
    def __init__(self, option):
        self.option = option

    # Used to get rid of any sort of punctuation
    def lowercasingOption(self, option):
        lowercaseOption = option.lower()

        if "." in lowercaseOption:
            lowercaseOption = lowercaseOption.replace(".", "")

        print(lowercaseOption)

        return lowercaseOption

    # removing command word (a.k.a first word like open/close etc.) from string
    def removingCommandWord(self, option):
        # Removing Initial word from string
        # Using slicing
        x = option.split()
        res = " ".join(x[1:])

        return res


class KeyboardClass:

    def __init__(self, option):
        self.option = option

    # Used to open applications through CLI
    def openAppsThroughCLI(self, option):

        kbCUI = CleaningUpInput(option)
        lowercaseOption = kbCUI.lowercasingOption(option)

        if "open" in lowercaseOption:
            app_name = lowercaseOption.replace("open ", "").strip()
            AppOpener.open(app_name, match_closest=True)

    # Used to close applications through CLI
    def closeAppsThroughCLI(self, option):

        kbCUI = CleaningUpInput(option)
        lowercaseOption = kbCUI.lowercasingOption(option)

        if "close" in lowercaseOption:
            app_name = lowercaseOption.replace("open ", "").strip()
            AppOpener.close(app_name, match_closest=True, output=False)

    # Used to type words
    def typingWords(self, option):
        kbCUI = CleaningUpInput(option)
        lowercaseOption = kbCUI.lowercasingOption(option)
        noCmdWordOption = kbCUI.removingCommandWord(lowercaseOption)

        if "type" in lowercaseOption:
            pydirectinput.write(noCmdWordOption)

    # Common key presses
    def commonFunctionKeys(self, option):

        if option == "enter":
            pydirectinput.press("enter")
        elif option == "backspace":
            pydirectinput.press("backspace")
        elif option == "tab":
            pydirectinput.press("tab")
        elif option == "escape":
            pydirectinput.press("esc")
        elif option == "space":
            pydirectinput.press("space")
        elif option == "right":
            pydirectinput.press("right")
        elif option == "left":
            pydirectinput.press("left")
        elif option == "up":
            pydirectinput.press("up")
        elif option == "down":
            pydirectinput.press("down")

    # Used for all single letter key presses
    def singleLetterKeyPresses(self, option):
        # command is "press "letter" for "word starting with letter" e.g. Press a for apple
        if option == "a":
            pydirectinput.press("a")
        elif option == "b":
            pydirectinput.press("b")
        elif option == "c":
            pydirectinput.press("c")
        elif option == "d":
            pydirectinput.press("d")
        elif option == "e":
            pydirectinput.press("e")
        elif option == "f":
            pydirectinput.press("f")
        elif option == "g":
            pydirectinput.press("g")
        elif option == "h":
            pydirectinput.press("h")
        elif option == "i":
            pydirectinput.press("i")
        elif option == "j":
            pydirectinput.press("j")
        elif option == "l":
            pydirectinput.press("l")
        elif option == "m":
            pydirectinput.press("m")
        elif option == "n":
            pydirectinput.press("n")
        elif option == "o":
            pydirectinput.press("o")
        elif option == "p":
            pydirectinput.press("p")
        elif option == "q":
            pydirectinput.press("q")
        elif option == "r":
            pydirectinput.press("r")
        elif option == "s":
            pydirectinput.press("s")
        elif option == "t":
            pydirectinput.press("t")
        elif option == "u":
            pydirectinput.press("u")
        elif option == "v":
            pydirectinput.press("v")
        elif option == "w":
            pydirectinput.press("w")
        elif option == "x":
            pydirectinput.press("x")
        elif option == "y":
            pydirectinput.press("y")
        elif option == "z":
            pydirectinput.press("z")

    # Used for multiple single presses
    def mutipleSinglePresses(self, option):
        if option == "right":
            pydirectinput.press("right")
        elif option == "left":
            pydirectinput.press("left")
        elif option == "up":
            pydirectinput.press("up")
        elif option == "down":
            pydirectinput.press("down")

    # Used for multiple key presses
    def multipleKeypresses(self, option):
        kbCUI = CleaningUpInput(option)
        lowercaseOption = kbCUI.lowercasingOption(option)
        noCmdWordOption = kbCUI.removingCommandWord(lowercaseOption)

        _split = lowercaseOption.split(' ', 1)

        if _split[0] == "hold" or _split[0] == "hold,":
            with pyautogui.hold(_split[1][0]):
                pydirectinput.press(_split[1][1])

    # Used to capitalize or lowercase letters
    def lowerOrUpper(self, option):
        kbCUI = CleaningUpInput(option)
        lowercaseOption = kbCUI.lowercasingOption(option)
        noCmdWord = kbCUI.removingCommandWord(lowercaseOption)

        if lowercaseOption[0:5] == "lower":
            pydirectinput.press(noCmdWord)

        if lowercaseOption[0:5] == "upper":
            with pyautogui.hold("shift"):
                pydirectinput.press(noCmdWord)
