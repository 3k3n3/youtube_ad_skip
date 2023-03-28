import pyautogui
import time

# Images and Description stored as dictionary K,V pairs 
images = {
    "images/skip.png": "Skip icon",
    "images/white_x.png": "White X icon",
    "images/black_x.png": "Black X icon"
    }

def skip_ad():
    while True:
        # Images and their x, y screen coordinates where image is found
        icon_cords = [(images[image], pyautogui.locateCenterOnScreen(image)) for image in images]

        for icon, cords in icon_cords:
            if cords:
                print(f"{icon} is found at: {cords}")

                pyautogui.click(cords)

    # 2 seconds delay to prevent multiple clicks
    time.sleep(2)
    skip_ad()

skip_ad()
