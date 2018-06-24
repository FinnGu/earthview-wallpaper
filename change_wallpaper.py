"""Provides utility methods to fetch earthview images and set them as wallpaper."""

import ctypes
import random
import urllib.request
import os
import sys


class ChangeWallpaper:
    """Provides utility methods to fetch earthview images and set them as wallpaper."""

    @staticmethod
    def set_wallpaper(wallpaper_name):
        """Sets image as wallpaper. Image has to be in current working directory."""
        path_to_dir = os.getcwd()

        # Use SystemParametersInfoA for Python 2
        # Use absolute path for image
        # SPI_SETDESKWALLPAPER = 20
        if sys.platform.startswith("win32"):
            if os.path.isfile(path_to_dir + "\\" + wallpaper_name):
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path_to_dir + "\\" + wallpaper_name, 0x3)
        elif sys.platform.startswith("darwin"):
            if os.path.isfile(path_to_dir + "/" + wallpaper_name):
                os.system("osascript -e 'tell application \"System Events\" to set picture of every desktop to POSIX file \"" +
                          path_to_dir + "/" + wallpaper_name + "\"'")

    @staticmethod
    def fetch_and_set_random_wallpaper():
        """Fetches random url from 'prettyearth.txt', downloads it, and calls the set_downloaded_image_as_wallpaper() method."""
        with open("prettyearth.txt") as file:
            content = file.readlines()
            content = [x.strip("\n") for x in content]

            random_img_url = content[random.randint(0, len(content) - 1)]
            wallpaper_name = "wallpaper" + str(ChangeWallpaper.get_last_number() + 1) + ".jpg"

            urllib.request.urlretrieve(random_img_url, wallpaper_name)
            ChangeWallpaper.delete_old_image()

        ChangeWallpaper.set_wallpaper(wallpaper_name)

    @staticmethod
    def delete_old_image():
        """Deletes file starting with 'wallpaper', followed by the highest number if one exists. Uses the method get_last_number()
        to determine highest available number."""
        path_to_dir = os.getcwd()
        previous_number = ChangeWallpaper.get_last_number() - 1

        if os.path.isfile(path_to_dir + "/wallpaper" + str(previous_number) + ".jpg"):
            os.remove(path_to_dir + "/wallpaper" +
                      str(previous_number) + ".jpg")

    @staticmethod
    def get_last_number():
        """Searches current directory for images starting with 'wallpaper',
        succeeded by a number and returns the highest number of those."""
        wallpapers = [filename for filename in os.listdir(".") if filename.startswith("wallpaper")]
        numbers = [int(wallpaper[9:][:-4]) for wallpaper in wallpapers]

        if numbers:
            numbers.sort()
            numbers.reverse()

            return numbers[0]

        return 0
