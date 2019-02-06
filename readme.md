# EarthviewWallpaper:
This project fetches Google's [earthview images](https://earthview.withgoogle.com/) and changes your desktop wallpaper every 15 minutes to a random one of them.


## Installation Guide (Windows):
1. Clone this repository to your local machine
2. Install the required dependencies by running `pip install -r requirements.txt` from the root of your cloned repository
3. Build by running `pyinstaller --clean --noconsole --name EarthviewWallpaper --add-data="prettyearth.txt;." --add-data="icon.ico;." app.py` from the root of your cloned repository
4. Optional: Automatically start *EarthviewWallpaper* on login
    1. Create a [shortcut](https://www.computerhope.com/issues/ch000739.htm) to "/dist/EarthviewWallpaper/EarthviewWallpaper.exe"
    2. Press <kbd>WIN</kbd>+<kbd>R</kbd>
    3. Type "shell:startup" and hit <kbd>ENTER</kbd>
    4. Move the shortcut to this location


## Installation Guide (OS X):
1. Clone this repository to your local machine
2. Install the required dependencies by running `pip3 install -r requirements.txt` from the root of your cloned repository
3. Build by running `python setup.py py2app` from the root of your cloned repository
4. Move the app to your systems' application folder by running `mv dist/app.app /Applications/EarthviewWallpaper.app`
5. Optional: Automatically start *EarthviewWallpaper* on login by running `mv local.earthviewwallpaper.agent.plist ~/Library/LaunchAgents`


## Open Tasks:
* Change ALL desktops for OS X
* Handle network errors
* Use PyInstall on OS X, too
* Grant permanent permission on OS X Mojave

## Credits:
* Icon from https://icon-icons.com/icon/earth-globe/70179
