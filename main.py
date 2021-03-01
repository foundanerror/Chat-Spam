import pyautogui,time
import keyboard 

for i in range(1,6):
    print(str(i))
    time.sleep(1)




def main(): 
    for i in range(0,1000):
        pyautogui.typewrite('@Pr1nce')
        pyautogui.press("enter")
        pyautogui.press("enter")
        time.sleep(0.1)
        if keyboard.is_pressed('O'):
            return True

main()
 