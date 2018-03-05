import ctypes
import random
import urllib.request
import os
import schedule
import time

def set_old_wallpaper():
    path_to_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.isfile(path_to_dir + "\\wallpaper.jpg"):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path_to_dir + "\\wallpaper.jpg", 0x3)

def change_wallpaper():
    with open("prettyearth.txt") as file:
        content = file.readlines()
        content = [x.strip("\n") for x in content]

        random_img_url = content[random.randint(0, len(content) - 1)]

        urllib.request.urlretrieve(random_img_url, "wallpaper.jpg")

    path_to_dir = os.path.dirname(os.path.abspath(__file__))

    # Use SystemParametersInfoA for Python 2
    # Use absolute path for image
    # SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path_to_dir + "\\wallpaper.jpg", 0x3)

# Load once on startup
set_old_wallpaper()
# and after that every 15 minutes
schedule.every(15).minutes.do(change_wallpaper)

while True:
    schedule.run_pending()
    time.sleep(1)
