import ctypes
import random
import urllib.request
import os
import sys

class ChangeWallpaper:

    @staticmethod
    def set_downloaded_image_as_wallpaper():
        path_to_dir = os.getcwd()

        # Use SystemParametersInfoA for Python 2
        # Use absolute path for image
        # SPI_SETDESKWALLPAPER = 20
        if sys.platform.startswith("win32"):
            if os.path.isfile(path_to_dir + "\\wallpaper.jpg"):
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path_to_dir + "\\wallpaper.jpg", 0x3)
        elif sys.platform.startswith("darwin"):
            last_number = ChangeWallpaper.get_last_number()

            if os.path.isfile(path_to_dir + "/wallpaper" + str(last_number) + ".jpg"):
                os.system("osascript -e 'tell application \"System Events\" to set picture of every desktop to POSIX file \"" + path_to_dir + "/wallpaper" + str(last_number) + ".jpg\"'")

    @staticmethod
    def fetch_and_set_random_wallpaper():
        with open("prettyearth.txt") as file:
            content = file.readlines()
            content = [x.strip("\n") for x in content]

            random_img_url = content[random.randint(0, len(content) - 1)]
            next_number = ChangeWallpaper.get_last_number() + 1

            urllib.request.urlretrieve(random_img_url, "wallpaper" + str(next_number) + ".jpg")
            ChangeWallpaper.delete_old_image()

        ChangeWallpaper.set_downloaded_image_as_wallpaper()

    @staticmethod
    def delete_old_image():
        path_to_dir = os.getcwd()
        previous_number = ChangeWallpaper.get_last_number() - 1

        if os.path.isfile(path_to_dir + "/wallpaper" + str(previous_number) + ".jpg"):
            os.remove(path_to_dir + "/wallpaper" + str(previous_number) + ".jpg")

    @staticmethod
    def get_last_number():
        numbers = [int(filename[9:][:-4]) for filename in os.listdir('.') if filename.startswith("wallpaper")]

        if numbers:
            numbers.sort()
            numbers.reverse()

            return numbers[0]

        return 0