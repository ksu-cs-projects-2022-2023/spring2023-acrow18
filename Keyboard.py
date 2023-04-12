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

        finalizedOutput = lowercaseOption.split(' ', 1)

        if "type" in lowercaseOption:
            pydirectinput.write(finalizedOutput[1])

    # Common key presses
    def commonFunctionKeys(self, option):
        kbCUI = CleaningUpInput(option)
        lowercaseOption = kbCUI.lowercasingOption(option)

        _split = lowercaseOption.split(' ', 1)

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
    def singleLetterKeyPresses(self, option):
        kbCUI = CleaningUpInput(option)
        lowercaseOption = kbCUI.lowercasingOption(option)

        _split = lowercaseOption.split(' ', 1)
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

    # Used for multiple key presses
    def multipleKeypresses(self, option):
        kbCUI = CleaningUpInput(option)
        lowercaseOption = kbCUI.lowercasingOption(option)

        _split = lowercaseOption.split(' ', 1)

        if _split[0] == "hold" or _split[0] == "hold,":
            with pyautogui.hold(_split[1]):
                pydirectinput.press(_split[2][0])

    # Used to capitalize or lowercase letters
    def lowerOrUpper(self, option):
        kbCUI = CleaningUpInput(option)
        lowercaseOption = kbCUI.lowercasingOption(option)

        _split = lowercaseOption.split(' ', 1)

        if _split[0] == "lower" or _split[0] == "lower,":
            pydirectinput.press(_split[1][0])

        if _split[0] == "upper" or _split[0] == "upper,":
            with pyautogui.hold("shift"):
                pydirectinput.press(_split[1][0])
