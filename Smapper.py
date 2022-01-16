import pyautogui, time, cowsay, os

print("--------------------------------------------------------------")

cowsay.meow('welcome to spammer')
print("______________________________________________________")
Text = input("Enter the text : ")



time.sleep(5)

while True:
    pyautogui.typewrite(Text)

    pyautogui.press("enter")
    
