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

            # used to open/close applications
            if 'open' == textOutput[0:4]:
                kbKC.openAppsThroughCLI(textOutput)

            if 'close' == textOutput[0:5]:
                kbKC.closeAppsThroughCLI(textOutput)

            # used to type words
            if 'type' == textOutput[0:4]:
                kbKC.typingWords(textOutput)

            # WORKS UP TO THIS POINT

            # used for key presses
            # need to test another statement
            if 'press' == textOutput[0:5]:
                noCmdWord = kbCUI.removingCommandWord(textOutput)

                if 'for' == noCmdWord[2:5]:
                    kbKC.singleLetterKeyPresses(noCmdWord[0:1])
                # else if 'times' == noCmdWord[10:13] or 'times' == noCmdWord[7:11] or 'times' == noCmdWord[11:14]:
                 #   kbKC.mutipleSinglePresses(noCmdWord)
                else:
                    kbKC.commonFunctionKeys(noCmdWord)

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

