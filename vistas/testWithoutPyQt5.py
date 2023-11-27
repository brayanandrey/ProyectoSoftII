from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(100, 100, 280, 300)
    window.setWindowTitle("My simple GUI")
    
    layout = QVBoxLayout()
    
    label = QLabel("Press The Button Below!")
    textbox = QTextEdit()
    button = QPushButton("Press Me!")
    
    button.clicked.connect(lambda: on_clicked(textbox.toPlainText()))
    
    layout.addWidget(label)
    layout.addWidget(button)
    layout.addWidget(textbox )
    
    window.setLayout(layout)
    
    window.show()
    app.exec_()
    
def on_clicked(msg):
    alert = QMessageBox()
    alert.setText(msg)
    alert.exec_()

if __name__ == '__main__':
    main()