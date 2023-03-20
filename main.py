import VoiceIntake
import Keyboard
from sounddevice import wait

#Main function
def main():
    while 1==1:
        print("Recording")
        VoiceIntake.record_voice()
        text = VoiceIntake.request_file()
        with open("output.txt") as f:
            line = f.readline()

            #process the voice recording
            Keyboard.CleaningUpInput.cleaningUpOption(line)
        wait(2)

                                            
#Used to implement main
if(__name__ == "__main__"):
    main()
