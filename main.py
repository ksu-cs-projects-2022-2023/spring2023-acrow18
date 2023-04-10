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
            #finalizedOutput = textOutput.split(' ', 1)

            #print(finalizedOutput)

            if 'open' == textOutput[0:4]:
                kbKC.openAppsThroughCLI(textOutput)
        wait(2)


# Used to implement main
if __name__ == "__main__":
    main()
