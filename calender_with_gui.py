#pip install PySide2

from PySide2.QtWidgets import QApplication, QWidget, QCalendarWidget, QVBoxLayout
import sys
from PySide2.QtGui import QIcon

class Window(QWidget):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Calendar with GUI")
        self.setGeometry(300,200,500,400)
        self.setIcon()
        self.createCalendar()
        self.show()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def createCalendar(self):
        vbox = QVBoxLayout()
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        vbox.addWidget(self.calendar)
        self.setLayout(vbox)

myapp = QApplication(sys.argv)
window = Window()
myapp.exec_()
sys.exit()
