import pyautogui, time

position = pyautogui.position()
pesan = "coba test spam"
for a in range(5):
    pyautogui.click(position.x, position.y)
    pyautogui.typewrite(pesan)
    print(pesan)
    time.sleep(1)
    pyautogui.typewrite(["enter"])