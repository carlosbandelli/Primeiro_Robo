import webbrowser
import pyautogui
import time

time.sleep(1)

# x, y = pyautogui.position()
# print(x, y)
# Email
webbrowser.open("https://gmalato.bamboohr.com/login.php?r=%2Fhome")
time.sleep(5)

pyautogui.moveTo(824, 623, duration=0.25)
pyautogui.click(824, 623, button='left', duration=0.25)
time.sleep(5)
pyautogui.moveTo(481, 457, duration=0.25)
pyautogui.click(481, 457, button='left', duration=0.25)
time.sleep(3)
pyautogui.moveTo(715, 1059, duration=0.25)
pyautogui.click(715, 1059, button='left', duration=0.25)
pyautogui.moveTo(856, 1061, duration=0.25)
pyautogui.click(856, 1061, button='left', duration=0.25)
pyautogui.moveTo(953, 1062, duration=0.25)
pyautogui.click(953, 1062, button='left', duration=0.25)
pyautogui.moveTo(906, 1067, duration=0.25)
pyautogui.click(906, 1067, button='left', duration=0.25)

time.sleep(3)

webbrowser.open("https://www.youtube.com/")
time.sleep(3)
pyautogui.moveTo(793, 106, duration=0.25)
pyautogui.click(793, 106, button='left', duration=0.35)
pyautogui.write("Liu @ Lollapalooza (Live Set)", interval=0.25)

pyautogui.moveTo(1200, 107, duration=0.25)
pyautogui.click(1200, 107, button='left', duration=0.25)
time.sleep(3)
pyautogui.moveTo(706, 367, duration=0.25)
pyautogui.click(706, 367, button='left', duration=0.25)
time.sleep(8)
pyautogui.moveTo(1259, 753, duration=0.25)
pyautogui.click(1259, 753, button='left', duration=0.25)
time.sleep(8)
pyautogui.moveTo(1259, 753, duration=0.25)
pyautogui.click(1259, 753, button='left', duration=0.25)
time.sleep(8)
pyautogui.moveTo(1259, 753, duration=0.25)
pyautogui.click(1259, 753, button='left', duration=0.25)
time.sleep(8)
pyautogui.moveTo(1259, 753, duration=0.25)
pyautogui.click(1259, 753, button='left', duration=0.25)

# Abre plataforma da Digital Innovation One
webbrowser.open("https://kanboard.gmalato.com.br/")
time.sleep(5)

# Abre a plataforma da mesttra
webbrowser.open("https://www.linkedin.com/feed/")
time.sleep(4)
