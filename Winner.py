from PyQt5.QtCore import Qt # type: ignore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout # type: ignore
from random import randint

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Winner')

text1 = QLabel("Натисни щоб дізнатись переможця:")
text2 = QLabel("?")
button = QPushButton("Згенерувати")

v_line = QVBoxLayout()

v_line.addWidget(
    text1,  alignment = Qt.AlignCenter

)
v_line.addWidget(
    text2,  alignment = Qt.AlignCenter

)

v_line.addWidget(
    button,  alignment = Qt.AlignCenter

)


def number():
    text1.setText('Переможець:')
    run_num = randint(1,100)
    text2.setText(str(randint(1,100)))
button.clicked.connect(number)


main_win.setLayout(v_line)


main_win.show()
app.exec_()