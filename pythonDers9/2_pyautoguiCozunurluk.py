import pyautogui
# ekran çözünürlüğü
screenWidth, screenHeight=pyautogui.size()
print("ekran çözünürlüğü :", screenWidth, screenHeight)
# fare pozisyonu
currentMouseX, currentMouseY=pyautogui.position()
print(currentMouseX, currentMouseY)