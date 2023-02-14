from time import sleep
import pyautogui
import os
from sounddevice import wait
import pydirectinput
import random
import pyowm

#Used to get rid of any sort of punctuation
def tokenizingInput(option):
    
    if "." in option:
        optionsplit = option.split(".", 1)
        
        if(optionsplit[0] == optionsplit[1]):
            option = optionsplit[0]
        else:
            option = option.replace(".", "")
    option = option.replace("?", "")
    option = option.replace("!", "")
    option = option.replace(",", "")
    
    print(option)
    
    option = option.lower()
    
    print(option)
    
    _split = option.split(" ", 1)
    _completeSplit = option.split(" ")

#Used to open lnk files through the command prompt
def openFilesThroughCommandPrompt(option):
    _split = tokenizingInput(option)
    
    if(_split[0] == "open," or _split[0] == "open"):
        os.system('cmd /c "cd lnks && START {name}.lnk"'.format(name = _split[1])) #types in the command prompt START and the name of the file to open

#Used to type words
def typingWords(option):
    _split = tokenizingInput(option)

    if(_split[0] == "type"):
        pydirectinput.write(_split[1])

#Common key presses
def commonFunctionKeys(option):
    _split = tokenizingInput(option)
    
    if(_split[0] == "press" or _split[0] == "press,"):
        if(_split[1] == "enter"):
            pydirectinput.press("enter")
        elif(_split[1] == "backspace"):
            pydirectinput.press("backspace")
        elif(_split[1] == "tab"):
            pydirectinput.press("tab")
        elif(_split[1] == "escape"):
            pydirectinput.press("esc")
        elif(_split[1] == "space"):
            pydirectinput.press("space")
        elif(_split[1] == "right"):
            pydirectinput.press("right")
        elif(_split[1] == "left"):
            pydirectinput.press("left")
        elif(_split[1] == "up"):
            pydirectinput.press("up")
        elif(_split[1] == "down"):
            pydirectinput.press("down")

#Used to captialize or lowercase letters          
def lowerOrUpper(option):
    _split = tokenizingInput(option)
         
    if(_split[0] == "lower" or _split[0] == "lower,"):
        pydirectinput.press(_split[1][0])     

    if(_split[0] == "upper" or _split[0] == "upper,"):
        with pyautogui.hold("shift"):
            pydirectinput.press(_split[1][0])    
            
def openCommon(option):
    _split = tokenizingInput(option)
    
    #opens google chrome then displays youtube
    if(option.startswith("use youtube")):
        Movement("open google")
        
        sleep(6)

        pyautogui.write("youtube.com")
        pyautogui.press("enter")

        sleep(6)

        for i in range(4):
            pydirectinput.press("tab")
        Movement("type " + option.replace("use youtube ", ""))
        Movement("press enter")
