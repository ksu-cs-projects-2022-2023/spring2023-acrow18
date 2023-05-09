import VoiceIntake
import Keyboard
from sounddevice import wait


# Main function
def main(option=None):
    viVI = VoiceIntake.VoiceInput()
    viF = VoiceIntake.File()
    kbCUI = Keyboard.CleaningUpInput(option)
    kbKC = Keyboard.KeyboardClass(option)

    while 1 == 1:
        print("Recording")
        viVI.record_voice()
        text = viF.request_file()
        with open("output.txt") as f:
            line = f.readline()

            # process the voice recording
            textOutput = kbCUI.lowercasingOption(line)

            # used for multiple key presses
            _split = textOutput.split(' ')
            _fixedsplitwords = _split.replace("press, ", "press").strip()

            # START OF APPLICATION BASED CALLS

            # used to open/close applications
            if 'open' == textOutput[0:4]:
                kbKC.openAppsThroughCLI(textOutput)

            if 'close' == textOutput[0:5]:
                kbKC.closeAppsThroughCLI(textOutput)

            # Used to switch between open applications
            if 'switch application' == textOutput[0:18]:
                # fixedNumAndLower = kbCUI.text2int(textOutput)
                kbKC.switchingApplications(textOutput)

            # Used to view open applications
            if 'view open applications' == textOutput[0:22]:
                kbKC.viewOpenApps()

            # Used to open programs and features to change/remove applications
            if 'open programs and features' == textOutput[0:26]:
                kbKC.openChangeorRemoveApps()

            # END OF APPLICATION BASED CALLS

            # Used to type words
            if 'type' == textOutput[0:4]:
                kbKC.typingWords(textOutput)

            # Used for key presses
            if 'press' == textOutput[0:5]:
                noCmdWord = kbCUI.removingCommandWord(textOutput)
                fixedNumAndLower = kbCUI.text2int(noCmdWord)

                # Used for single letter key presses
                if any(num.isdigit() for num in fixedNumAndLower):
                    if fixedNumAndLower[2] == " ":
                        kbKC.customSingleLetterKeyPresses(fixedNumAndLower)

                    elif _split[0] == 'press':
                        print(_split)
                        #kbKC.multipleKeypresses(_split)
                    # Used for function key presses
                    else:
                        kbKC.customCommonFunctionKeys(noCmdWord)

            # multiple key presses
            if 'hold' == textOutput[0:4]:
                kbKC.multipleKeypresses(textOutput)

            # used to capitalize or lowercase letters
            if 'lower' == textOutput[0:5] or 'upper' == textOutput[0:5]:
                kbKC.lowerOrUpper(textOutput)

        wait(2)


# Used to implement main
if __name__ == "__main__":
    main()

