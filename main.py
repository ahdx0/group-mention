import pyautogui

Members = int(input(" How many members of the group? "))
pyautogui.sleep(1.5)
for i in range(0, Members):
    pyautogui.write("@")
    pyautogui.press("Down")
    pyautogui.press("Enter")
    print(i)
pyautogui.press("Enter")