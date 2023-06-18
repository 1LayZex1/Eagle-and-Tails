from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, 
QPushButton, QLabel, QVBoxLayout, QHBoxLayout, 
QButtonGroup, QMessageBox
)

app = QApplication([])
window = QWidget()
button_group = QButtonGroup()
window.setWindowTitle('Симулятор подбрасывания монеты')
window.resize(400, 200)
window.move(800, 800)

title = QLabel('Подбросьте монетку')
btn = QPushButton('Подбросить')

def orel():
    victory_win = QMessageBox()
    victory_win.setText('Орёл')
    victory_win.exec()
def reshka():
    victory_lose = QMessageBox()
    victory_lose.setText('Решка')
    victory_lose.exec()

layoutV = QVBoxLayout()
layoutH = QHBoxLayout()
layoutH1 = QHBoxLayout()

layoutH.addWidget(title, alignment = Qt.AlignCenter)
layoutH1.addWidget(btn, alignment = Qt.AlignCenter)

layoutV.addLayout(layoutH)
layoutV.addLayout(layoutH1)
window.setLayout(layoutV)

number = randint(0,2)
def rand_num():
    if number == 1:
        orel()    
    elif number == 2:
        reshka()

btn.clicked.connect(rand_num)

window.show()
app.exec_()
