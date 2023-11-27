from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("vistas/testWithPyQt5.ui", self)
        self.show()
        
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(lambda :self.sayit(self.textEdit.toPlainText()))
        self.actionClose.triggered.connect(exit)
        
    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        
        if username == "admin" and password == "admin":
            self.label.setText("Login successful")
            self.textEdit.setEnabled(True)
            self.pushButton_2.setEnabled(True)
        else:
            message = QMessageBox()
            message.setText("Login failed")
            message.exec_()
    
    def sayit(self, msg):
        message = QMessageBox()
        message.setText(msg)
        message.exec_()

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()
    
if __name__ == "__main__":
    main()