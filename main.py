import VoiceIntake
import Keyboard
from sounddevice import wait

# Main function
def main():
    while 1 == 1:
        print("Recording")
        VoiceIntake.VoiceInput.record_voice()
        text = VoiceIntake.File.request_file()
        with open("output.txt") as f:
            line = f.readline()

            # process the voice recording
            option = Keyboard.CleaningUpInput.lowercasingOption(line)
            tokenizedOption = Keyboard.CleaningUpInput.tokenizingInput(line)

            if tokenizedOption[0] == 'open':
                Keyboard.KeyboardClass.openAppsThroughCLI(option)
        wait(2)

# Used to implement main
if __name__ == "__main__":
    main()
