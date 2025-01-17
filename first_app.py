from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from random import choice

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("My first App")
main_window.resize(300, 200)

# Create all app objects
title = QLabel("Random Keywords")

text1 = QLabel("Keyword 1")
text2 = QLabel("Keyword 2")
text3 = QLabel("Keyword 3")

button1 = QPushButton("click me")
button2 = QPushButton("click me")
button3 = QPushButton("click me")

my_words = ['musica', 'programacao', 'jogos', 'pintura', 'fotografia']

# All design
master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row1.addWidget(title, alignment=Qt.AlignCenter)

row2 = QHBoxLayout()
row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

row3 = QHBoxLayout()
row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)

# Create functions
def random_word1():
    word = choice(my_words)
    text1.setText(word)

def random_word2():
    word = choice(my_words)
    text2.setText(word)

def random_word3():
    word = choice(my_words)
    text3.setText(word)

# Events
button1.clicked.connect(random_word1)
button2.clicked.connect(random_word2)
button3.clicked.connect(random_word3)

#show/run app
main_window.show()
app.exec()