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
            _split = list(map(lambda x: x.replace('press,', 'press'), _split))

            # START OF APPLICATION BASED CALLS

            # used to open/close applications
            if 'open' == textOutput[0:4]:
                kbKC.openAppsThroughCLI(textOutput)

            # Used to open programs and features to change/remove applications
            if 'programs and features' == textOutput[0:21]:
                kbKC.openProgramsOrFeatures()

            if 'close' == textOutput[0:5]:
                kbKC.closeAppsThroughCLI(textOutput)

            # Used to switch between open applications (LITTLE CLUNKY)
            if 'switch application' == textOutput[0:18]:
                # fixedNumAndLower = kbCUI.text2int(textOutput)
                kbKC.switchingApplications(textOutput)

            # Used to view open applications
            if 'view open applications' == textOutput[0:22]:
                kbKC.viewOpenApps()

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

                    elif _split[2] == 'and':
                        kbKC.multipleKeypresses(noCmdWord)
                    # Used for function key presses
                    else:
                        kbKC.customCommonFunctionKeys(noCmdWord)

        wait(2)


# Used to implement main
if __name__ == "__main__":
    main()

