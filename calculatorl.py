from PyQt5.QtWidgets import QLineEdit, QGridLayout, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QFont

class CalcApp(QWidget):

    def __init__(self):
        super().__init__()

        # App Settings
        self.setWindowTitle("Calculator")
        self.resize(250, 300)

        # App Objects/Widgets
        self.text_box = QLineEdit()
        self.text_box.setFont(QFont("Helvetica", 32))

        self.grid = QGridLayout()

        self.buttons = [
            "7", "8", "9", "/", 
            "4", "5", "6", "*", 
            "1", "2", "3", "-", 
            "0", ".", "=", "+"
            ]
        
        row, col = 0, 0
        for text in self.buttons:
            if col > 3:
                row += 1
                col = 0
            button = QPushButton(text)
            button.clicked.connect(self.button_click)
            button.setStyleSheet("QPushButton { font: 25pt Helvetica; padding: 10px}")
            self.grid.addWidget(button, row, col)
            col += 1

        self.clear = QPushButton("C")
        self.clear.setStyleSheet("QPushButton { font: 25pt Helvetica; padding: 10px}")

        self.delete = QPushButton("Del")
        self.delete.setStyleSheet("QPushButton { font: 25pt Helvetica; padding: 10px}")


        # App Design
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)
        master_layout.addLayout(button_row)
        master_layout.setContentsMargins(25, 25, 25, 25)

        self.setLayout(master_layout)

        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)

    def button_click(self):
        button = app.sender()
        text = button.text()
        if text == "=":
            symbol = self.text_box.text()
            try:
                res = eval(symbol)
                self.text_box.setText(str(res))
            except Exception as e:
                print("Error : ", e)
        elif text == "C":
            self.text_box.clear()
        elif text == "Del":
            current_value = self.text_box.text()
            self.text_box.setText(current_value[:-1])
        else:
            current_value = self.text_box.text()
            self.text_box.setText(current_value + text)


# show/run app
if __name__ == "__main__":
    app = QApplication([])
    main_window = CalcApp()
    main_window.setStyleSheet("QWidget {background-color: rgb(0, 0, 0); color: rgb(255, 255, 255)}")
    main_window.show()
    app.exec()
