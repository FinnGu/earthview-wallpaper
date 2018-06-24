"""Main module of EarthviewWallpaper."""

from threading import Thread, Event
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from change_wallpaper import ChangeWallpaper
import sys


app = QApplication([])
stopFlag = Event()


class TimerThread(Thread):

    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(15.0 * 60.0):
            ChangeWallpaper.fetch_and_set_random_wallpaper()


def next():
    """Callback of system tray action 'Next background' that changes the wallpaper to a random one."""
    ChangeWallpaper.fetch_and_set_random_wallpaper()


def quit():
    """Callback of system tray action 'Quit' that exits the app."""
    stopFlag.set()
    app.quit()


def main():
    # Create the icon
    if sys.platform.startswith("win32"):
        icon = QIcon("icon.ico")
    elif sys.platform.startswith("darwin"):
        icon = QIcon("icon.icns")

    # Create the tray
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    # Create the background thread
    thread = TimerThread(stopFlag)

    # Create the menu
    menu = QMenu()

    action_next = QAction("Next background")
    action_next.triggered.connect(next)
    menu.addAction(action_next)

    action_quit = QAction("Quit")
    action_quit.triggered.connect(quit)
    menu.addAction(action_quit)

    # Add the menu to the tray
    tray.setContextMenu(menu)

    thread.start()
    app.exec_()


if __name__ == '__main__':
    main()
