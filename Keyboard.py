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
        kbCUI = CleaningUpInput(option)
        lowercaseOption = kbCUI.lowercasingOption(option)
        noCmdWordOption = kbCUI.removingCommandWord(lowercaseOption)

        if "press" in lowercaseOption:
            if noCmdWordOption == 'enter':
                pydirectinput.keyDown('enter')
            elif noCmdWordOption == "backspace":
                pydirectinput.press("backspace")
            elif noCmdWordOption == "tab":
                pydirectinput.press("tab")
            elif noCmdWordOption == "escape":
                pydirectinput.press("esc")
            elif noCmdWordOption == "space":
                pydirectinput.press("space")
            elif noCmdWordOption == "right":
                pydirectinput.press("right")
            elif noCmdWordOption == "left":
                pydirectinput.press("left")
            elif noCmdWordOption == "up":
                pydirectinput.press("up")
            elif noCmdWordOption == "down":
                pydirectinput.press("down")

    # Used for all single letter key presses
    def singleLetterKeyPresses(self, option):
        kbCUI = CleaningUpInput(option)
        lowercaseOption = kbCUI.lowercasingOption(option)
        noCmdWordOption = kbCUI.removingCommandWord(lowercaseOption)

        if lowercaseOption[0:5] == "press":
            if noCmdWordOption == "a":
                pydirectinput.press("a")
            elif noCmdWordOption == "b":
                pydirectinput.press("b")
            elif noCmdWordOption == "c":
                pydirectinput.press("c")
            elif noCmdWordOption == "d":
                pydirectinput.press("d")
            elif noCmdWordOption == "e":
                pydirectinput.press("e")
            elif noCmdWordOption == "f":
                pydirectinput.press("f")
            elif noCmdWordOption == "g":
                pydirectinput.press("g")
            elif noCmdWordOption == "h":
                pydirectinput.press("h")
            elif noCmdWordOption == "i":
                pydirectinput.press("i")
            elif noCmdWordOption == "j":
                pydirectinput.press("j")
            elif noCmdWordOption == "l":
                pydirectinput.press("l")
            elif noCmdWordOption == "m":
                pydirectinput.press("m")
            elif noCmdWordOption == "n":
                pydirectinput.press("n")
            elif noCmdWordOption == "o":
                pydirectinput.press("o")
            elif noCmdWordOption == "p":
                pydirectinput.press("p")
            elif noCmdWordOption == "q":
                pydirectinput.press("q")
            elif noCmdWordOption == "r":
                pydirectinput.press("r")
            elif noCmdWordOption == "s":
                pydirectinput.press("s")
            elif noCmdWordOption == "t":
                pydirectinput.press("t")
            elif noCmdWordOption == "u":
                pydirectinput.press("u")
            elif noCmdWordOption == "v":
                pydirectinput.press("v")
            elif noCmdWordOption == "w":
                pydirectinput.press("w")
            elif noCmdWordOption == "x":
                pydirectinput.press("x")
            elif noCmdWordOption == "y":
                pydirectinput.press("y")
            elif noCmdWordOption == "z":
                pydirectinput.press("z")

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
