import AppOpener
import pyautogui
import pydirectinput
import re


class CleaningUpInput:

    # used to assign values for option
    def __init__(self, option):
        self.option = option

    # Used to get rid of any sort of punctuation
    def lowercasingOption(self, option):
        lowercaseOption = option.lower()

        if "." in lowercaseOption:
            lowercaseOption = lowercaseOption.replace(".", "")
        if "," in lowercaseOption:
            lowercaseOption = lowercaseOption.replace(",", "")
        if "?" in lowercaseOption:
            lowercaseOption = lowercaseOption.replace("?", "")

        print(lowercaseOption)

        return lowercaseOption

    # removing command word (a.k.a first word like open/close etc.) from string
    def removingCommandWord(self, option):
        # Removing Initial word from string
        # Using slicing
        x = option.split()
        res = " ".join(x[1:])

        return res

    # changes number words (ten) to number values (10)
    # pulled from https://stackoverflow.com/questions/493174/is-there-a-way-to-convert-number-words-to-integer (used to fix minor error with voice recognition)
    def text2int(self, textnum, numwords={}):
        if not numwords:
            units = [
                "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
                "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                "sixteen", "seventeen", "eighteen", "nineteen",
            ]

            tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

            scales = ["hundred", "thousand", "million", "billion", "trillion"]

            numwords["and"] = (1, 0)
            for idx, word in enumerate(units):  numwords[word] = (1, idx)
            for idx, word in enumerate(tens):       numwords[word] = (1, idx * 10)
            for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

        ordinal_words = {'first': 1, 'second': 2, 'third': 3, 'fifth': 5, 'eighth': 8, 'ninth': 9, 'twelfth': 12}
        ordinal_endings = [('ieth', 'y'), ('th', '')]

        textnum = textnum.replace('-', ' ')

        current = result = 0
        curstring = ""
        onnumber = False
        for word in textnum.split():
            if word in ordinal_words:
                scale, increment = (1, ordinal_words[word])
                current = current * scale + increment
                if scale > 100:
                    result += current
                    current = 0
                onnumber = True
            else:
                for ending, replacement in ordinal_endings:
                    if word.endswith(ending):
                        word = "%s%s" % (word[:-len(ending)], replacement)

                if word not in numwords:
                    if onnumber:
                        curstring += repr(result + current) + " "
                    curstring += word + " "
                    result = current = 0
                    onnumber = False
                else:
                    scale, increment = numwords[word]

                    current = current * scale + increment
                    if scale > 100:
                        result += current
                        current = 0
                    onnumber = True

        if onnumber:
            curstring += repr(result + current)

        return curstring


class KeyboardClass:

    def __init__(self, option):
        self.option = option

    # BEGINNING OF APPLICATION BASED CODE
    # Used to open applications through CLI (WORKS)
    def openAppsThroughCLI(self, option):

        kbCUI = CleaningUpInput(option)
        lowercaseOption = kbCUI.lowercasingOption(option)

        if "open" in lowercaseOption:
            app_name = lowercaseOption.replace("open ", "").strip()
            AppOpener.open(app_name, match_closest=True)

    # Used to close applications through CLI (WORKS)
    def closeAppsThroughCLI(self, option):

        kbCUI = CleaningUpInput(option)
        lowercaseOption = kbCUI.lowercasingOption(option)

        if "close" in lowercaseOption:
            app_name = lowercaseOption.replace("open ", "").strip()
            AppOpener.close(app_name, match_closest=True, output=False)

    # Used to switch between open applications (WORKS)
    def switchingApplications(self, option):
        kbCUI = CleaningUpInput(option)
        kbKC = KeyboardClass(option)
        fixedNumAndLower = kbCUI.text2int(option)

        if "switch application" in fixedNumAndLower:
            strippedFNL = fixedNumAndLower.replace("switch application ", "").strip()
            if "press" in strippedFNL:
                nocmdWords = strippedFNL.replace("press ", "").strip()
                if "write" in nocmdWords:
                    fixedNoCmdWords = nocmdWords.replace("write ", "right ").strip()
                pydirectinput.keyDown('alt')
                pydirectinput.press('tab')
                kbKC.repeatPresses(nocmdWords)
                pydirectinput.keyUp('alt')

    # Used to view open apps (WORKS)
    def viewOpenApps(self):
        pydirectinput.keyDown('alt')
        pydirectinput.press('tab')
        pydirectinput.time.sleep(2)
        pydirectinput.press('esc')
        pydirectinput.keyUp('alt')

    # Used to add and remove apps (POSSIBLY WORKS)
    def openProgramsOrFeatures(self):
        pyautogui.press('winleft')
        pydirectinput.write('appwiz.cpl')
        pydirectinput.press('enter')

    # END OF APPLICATION BASED CODE

    # Used to type words (WORKS)
    def typingWords(self, option):
        kbCUI = CleaningUpInput(option)
        lowercaseOption = kbCUI.lowercasingOption(option)
        noCmdWordOption = kbCUI.removingCommandWord(lowercaseOption)

        if "type" in lowercaseOption:
            pydirectinput.write(noCmdWordOption)

    # BEGINNING OF PRESSES

    # Common key presses (KIND OF WORKS)
    def customCommonFunctionKeys(self, option):
        kbKC = KeyboardClass(option)

        if option[2] != ' ':
            kbKC.repeatPresses(option)

    # Using custom function for all single letter key presses (WORKS)
    def customSingleLetterKeyPresses(self, option):
        kbKC = KeyboardClass(option)

        if option[1] == ' ' and 'z' >= option[0] >= 'a':
            kbKC.repeatPresses(option)

    # write a custom function (self, option, num)
    # loop num of times calling pydirectinput.press(option)
    # Used for multiple presses of the same key (WORKS/NEED TO ADD EDGE CASE FOR NOT SAYING NUMBER)
    def repeatPresses(self, option):
        kbCUI = CleaningUpInput(option)
        fixedNumAndLower = kbCUI.text2int(option)

        loopNum = int(re.search(r'\d+', fixedNumAndLower).group())  # gets number from string
        for x in range(loopNum):
            pydirectinput.press(option[:option.index(" ")])

    # Used for multiple key presses (WORKS KINDA)
    def multipleKeypresses(self, option):
        kbCUI = CleaningUpInput(option)
        lowercaseOption = kbCUI.lowercasingOption(option)

        _split = lowercaseOption.split(' ')

        if _split[0] == "control" or _split[0] == "ctrl":
            # for copy and paste
            if _split[2][0:1] == "c" or _split[2][0:1] == "v":
                with pyautogui.hold(_split[0]):
                    pydirectinput.press(_split[2][0:1])

            # for other multi key presses
            else:
                with pyautogui.hold(_split[0]):
                    pydirectinput.press(_split[2])

    # END OF PRESSES
# END OF ENTIRE CODE
