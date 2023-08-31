import time
import keyboard
import pyautogui as pyautogui
import winsound
from datetime import date

# GENERATE EXECUTABLE FILE#
# pip install pyinstaller
# pyinstaller  --onefile main.py [(-w) USE THIS COMMAND ONLY IF YOU PROGRAMM USES ITERATIONS WINDOWS]
# after generatel can you delete build folder / main.specp
# we need just a dist folder

onoff = False #TODO implements this

def main():

    data_atual = date.today()
    data_limite = date(2024, 6, 23)

    if data_atual < data_limite:

        while True:
            #if True:
                #time.sleep(60)
            if keyboard.is_pressed('page up'):
                time.sleep(0.3)

                pyautogui.press('f1')
                time.sleep(0.1)

                pyautogui.press('f2')
                time.sleep(0.1)

                pyautogui.press('6')
                time.sleep(0.1)

                pyautogui.press('8')
                time.sleep(0.1)

                pyautogui.press('f2')
                time.sleep(0.1)

                pyautogui.press('8')

                writeGenericMessage()

                pyautogui.press('f1')

            # if keyboard.is_pressed('page down'):

def writeGenericMessage():
    time.sleep(0.3)
    pyautogui.write('<<YOUR MSG HERE>>', interval=0.0)
    pyautogui.press('enter')
    time.sleep(0.3)
    pyautogui.write('<<YOUR MSG HERE>>', interval=0.0)
    pyautogui.press('enter')
    time.sleep(0.3)
    pyautogui.write('<<YOUR MSG HERE>>', interval=0.0)
    pyautogui.press('enter')
    time.sleep(0.3)


def makeSound():
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 350  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

main()