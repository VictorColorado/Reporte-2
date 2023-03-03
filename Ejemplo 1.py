from PyQt5.QtWidgets import QWidget, QApplication

application = QApplication([])
mainWindow = QWidget()

mainWindow.setGeometry(0,0,720,480)
mainWindow.setWindowTitle('Hola mundo')

mainWindow.show()
application.exec()