# EarthviewWallpaper:
This project fetches Google's [earthview images](https://earthview.withgoogle.com/) and changes your desktop wallpaper every 15 minutes to a random one of them.


## Installation Guide (Windows):
1. Clone this repository to your local machine
2. Install the required dependencies by running `pip install -r requirements.txt` from the root of your cloned repository
3. In "auto_change_wallpaper.bat" change path to "change_wallpaper.pyw"
4. Create a [shortcut](https://www.computerhope.com/issues/ch000739.htm) to "auto_change_wallpaper.bat"
5. Move the shortcut into your systems' startup folder
    1. Press <kbd>WIN</kbd>+<kbd>R</kbd>
    2. Type "shell:startup" and hit <kbd>ENTER</kbd>
    3. Move the file
6. Either execute the copied shortcut or restart your system
7. Your background should change after 15 minutes


## Installation Guide (OS X):
1. Clone this repository to your local machine
2. Install the required dependencies by running `pip3 install -r requirements.txt` from the root of your cloned repository
3. Build by running `python3 setup.py py2app`
4. Move the app to your systems' application folder by running `mv dist/app.app ~/Applications/EarthviewWallpaper.app`
5. Set *EarthviewWallpaper* as Login Item
    1. Go to System Preferences -> Users & Groups
    2. Select your user on the left
    3. Add *EarthviewWallpaper* as Login Item


## Open Tasks:
* Change ALL desktops for OS X
* Easier setup for Windows
* Handle network errors
* Check why OS X app is ~250MB