from AppOpener import open, close
import pyautogui
import pydirectinput


class CleaningUpInput:

    # used to assign values for option
    def __init__(self, option):
        self.option = option

    # Used to get rid of any sort of punctuation
    def cleaningUpOption(self):

        optionclean = self.option.replace(".", "")
        optionclean = self.option.replace("?", "")
        optionclean = self.option.replace("!", "")
        optionclean = self.option.replace(",", "")

        print(optionclean)

        optionlower = optionclean.lower()

        print(optionlower)

        return optionlower

    # Used to split the option into tokens
    def tokenizingInput(self):

        option = CleaningUpInput.CleaningUpOption(self.option)

        if "." in option:
            optionsplit = option.split(".", 1)
            if optionsplit[0] == optionsplit[1]:
                option = optionsplit[0]
            else:
                option = option.replace(".", "")
        option = option.replace("?", "")
        option = option.replace(",", "")

        print(option)

        option = option.lower()

        print(option)

        _split = option.split(" ", 1)
        _completerSplit = option.split(" ")


class KeyboardClass:

    def __init__(self, option):
        self.option = option

    # Used to open applications through CLI (not working yet)
    def openAppsThroughCLI(self):
        if "open" in self.option:
            app_name = self.option.replace("open ", "").strip()
            open(app_name, match_closest=True)

    # Used to close applications through CLI (not working yet)
    def closeAppsThroughCLI(self):
        if "close" in self.option:
            app_name = self.option.replace("close ", "").strip()
            close(app_name, match_closest=True, output=False)

    # Used to type words
    def typingWords(self):
        _split = CleaningUpInput.CleaningUpOption.tokenizingInput(self.option)

        if _split[0] == "type.":
            pydirectinput.write(_split[1])

    # Common key presses
    def commonFunctionKeys(self):
        _split = CleaningUpInput.CleaningUpOption.tokenizingInput(self.option)

        if _split[0] == "press" or _split[0] == "press,":
            if _split[1] == "enter":
                pydirectinput.press("enter")
            elif _split[1] == "backspace":
                pydirectinput.press("backspace")
            elif _split[1] == "tab":
                pydirectinput.press("tab")
            elif _split[1] == "escape":
                pydirectinput.press("esc")
            elif _split[1] == "space":
                pydirectinput.press("space")
            elif _split[1] == "right":
                pydirectinput.press("right")
            elif _split[1] == "left":
                pydirectinput.press("left")
            elif _split[1] == "up":
                pydirectinput.press("up")
            elif _split[1] == "down":
                pydirectinput.press("down")

    # Used for all single letter key presses
    def singleLetterKeyPresses(self):
        _split = CleaningUpInput.CleaningUpOption.tokenizingInput(self.option)

        if _split[0] == "press" or _split[0] == "press,":
            if _split[1] == "a":
                pydirectinput.press("a")
            elif _split[1] == "b":
                pydirectinput.press("b")
            elif _split[1] == "c":
                pydirectinput.press("c")
            elif _split[1] == "d":
                pydirectinput.press("d")
            elif _split[1] == "e":
                pydirectinput.press("e")
            elif _split[1] == "f":
                pydirectinput.press("f")
            elif _split[1] == "g":
                pydirectinput.press("g")
            elif _split[1] == "h":
                pydirectinput.press("h")
            elif _split[1] == "i":
                pydirectinput.press("i")
            elif _split[1] == "j":
                pydirectinput.press("j")
            elif _split[1] == "l":
                pydirectinput.press("l")
            elif _split[1] == "m":
                pydirectinput.press("m")
            elif _split[1] == "n":
                pydirectinput.press("n")
            elif _split[1] == "o":
                pydirectinput.press("o")
            elif _split[1] == "p":
                pydirectinput.press("p")
            elif _split[1] == "q":
                pydirectinput.press("q")
            elif _split[1] == "r":
                pydirectinput.press("r")
            elif _split[1] == "s":
                pydirectinput.press("s")
            elif _split[1] == "t":
                pydirectinput.press("t")
            elif _split[1] == "u":
                pydirectinput.press("u")
            elif _split[1] == "v":
                pydirectinput.press("v")
            elif _split[1] == "w":
                pydirectinput.press("w")
            elif _split[1] == "x":
                pydirectinput.press("x")
            elif _split[1] == "y":
                pydirectinput.press("y")
            elif _split[1] == "z":
                pydirectinput.press("z")

    # def multiple Key presses(option):

    # Used to capitalize or lowercase letters
    def lowerOrUpper(self):
        _split = CleaningUpInput.CleaningUpOption.tokenizingInput(self.option)

        if _split[0] == "lower" or _split[0] == "lower,":
            pydirectinput.press(_split[1][0])

        if _split[0] == "upper" or _split[0] == "upper,":
            with pyautogui.hold("shift"):
                pydirectinput.press(_split[1][0])
