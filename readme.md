# Earth-View-Wallpaper:
This project fetches Google's [Earth-View images](https://earthview.withgoogle.com/) and changes your desktop wallpaper every 15 minutes to a random one of them.


## Installation Guide:
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


## Open Tasks:
* Change ALL desktops for OS X
* Show as System Tray Icon
* Allow user to change time interval from there