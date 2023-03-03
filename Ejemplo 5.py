from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QLabel,
    QWidget,
    QApplication,
    QVBoxLayout,
)

application = QApplication([])

mainWindow = QWidget()
mainWindow.setGeometry(0,0,300,400)
mainWindow.setWindowTitle('Pokemon')

verticalLayout = QVBoxLayout()

for num in range(3):
    label = QLabel()
    pixmap = QPixmap('Pikachu.png')
    label.setPixmap(pixmap)
    verticalLayout.addWidget(label)
    
mainWindow.setLayout(verticalLayout) 
mainWindow.show()
application.exec()