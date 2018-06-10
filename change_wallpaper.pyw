import ctypes
import random
import urllib.request
import os
import schedule
import time
import sys


def set_downloaded_image_as_wallpaper():
    path_to_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Use SystemParametersInfoA for Python 2
    # Use absolute path for image
    # SPI_SETDESKWALLPAPER = 20
    if sys.platform.startswith("win32"):
        if os.path.isfile(path_to_dir + "\\wallpaper.jpg"):
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path_to_dir + "\\wallpaper.jpg", 0x3)
    elif sys.platform.startswith("darwin"):
        last_number = get_last_number()

        if os.path.isfile(path_to_dir + "/wallpaper" + str(last_number) + ".jpg"):
            os.system("python3 set_desktops.py --path " + path_to_dir + "/wallpaper" + str(last_number) + ".jpg")

def fetch_and_set_random_wallpaper():
    with open("prettyearth.txt") as file:
        content = file.readlines()
        content = [x.strip("\n") for x in content]

        random_img_url = content[random.randint(0, len(content) - 1)]
        next_number = get_last_number() + 1

        urllib.request.urlretrieve(random_img_url, "wallpaper" + str(next_number) + ".jpg")
        delete_old_image()

    set_downloaded_image_as_wallpaper()

def delete_old_image():
    path_to_dir = os.path.dirname(os.path.abspath(__file__))
    previous_number = get_last_number() - 1

    if os.path.isfile(path_to_dir + "/wallpaper" + str(previous_number) + ".jpg"):
        os.remove(path_to_dir + "/wallpaper" + str(previous_number) + ".jpg")

def get_last_number():
    numbers = [int(filename[9:][:-4]) for filename in os.listdir('.') if filename.startswith("wallpaper")]

    if numbers:
        numbers.sort()
        numbers.reverse()

        return numbers[0]
    
    return 0

# Load once on startup (probably only important for windows)
set_downloaded_image_as_wallpaper()
# and after that every 15 minutes
schedule.every(15).minutes.do(fetch_and_set_random_wallpaper)

while True:
    schedule.run_pending()
    time.sleep(1)
