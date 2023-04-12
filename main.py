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

            # parse first part of string i.e. (open, close etc.)
            # finalizedOutput = textOutput.split(' ', 1)

            # print(finalizedOutput)

            # used to open/close applications
            if 'open' == textOutput[0:4]:
                kbKC.openAppsThroughCLI(textOutput)

            if 'close' == textOutput[0:5]:
                kbKC.closeAppsThroughCLI(textOutput)

            # used to type words
            if 'type' == textOutput[0:4]:
                kbKC.typingWords(textOutput)

            # used for key presses
            # need to test another statement
            if 'press' == textOutput[0:5]:

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

