import pyautogui,time
import keyboard 

MessageLimit = int(input("Please State Message Limit in Numbers: "))
Message = str(input('Please State Message: '))
for i in range(1,6):
    print(str(i))
    time.sleep(1)




def main(): 
    for i in range(0,MessageLimit):
        pyautogui.typewrite(Message)
        pyautogui.press("enter")
        pyautogui.press("enter")
        time.sleep(0.1)
        if keyboard.is_pressed('O'):
            return True

main()
 