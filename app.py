from threading import Thread, Event
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from change_wallpaper import ChangeWallpaper


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
    ChangeWallpaper.fetch_and_set_random_wallpaper()

def quit():
    stopFlag.set()
    app.quit()

def main():

    # Create the icon
    icon = QIcon("icon.icns")

    # Create the tray
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    # Create the background thread
    thread = TimerThread(stopFlag)

    # Create the menu
    menu = QMenu()

    actionNext = QAction("Next background")
    actionNext.triggered.connect(next)
    menu.addAction(actionNext)

    actionQuit = QAction("Quit")
    actionQuit.triggered.connect(quit)
    menu.addAction(actionQuit)

    # Add the menu to the tray
    tray.setContextMenu(menu)

    thread.start()
    app.exec_()


if __name__ == '__main__':
    main()
