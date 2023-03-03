from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QLabel,
    QWidget,
    QApplication,
    QHBoxLayout,
)

application = QApplication([])

mainWindow = QWidget()
mainWindow.setGeometry(0,0,720,480)
mainWindow.setWindowTitle('Pokemon')

horizontalLayout = QHBoxLayout()

for num in range(4):
    label = QLabel()
    pixmap = QPixmap('Pikachu.png')
    label.setPixmap(pixmap)
    horizontalLayout.addWidget(label)
    
mainWindow.setLayout(horizontalLayout) 
mainWindow.show()
application.exec()