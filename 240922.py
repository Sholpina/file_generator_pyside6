import sys
from PySide6.QtWidgets import (
        QMainWindow, QApplication, QPushButton, QVBoxLayout,
        QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
        QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QWidget, QToolBar
)
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPalette, QColor, QPixmap


class MainWindow(QWidget):

        def __init__(self):
                super().__init__()
                # Add a title
                self.setWindowTitle("File Generator!!")

                # Resize window
                self.setMinimumSize(QSize(600, 420))
                self.setMaximumSize(QSize(800, 600))

                # Create a QVBoxLayout instance
                vbox = QVBoxLayout(self)
                vbox.setContentsMargins(50, 10, 50, 10)
                vbox.setSpacing(21)

                # Create a Label
                my_label = QLabel("Pick  files to download")
                font = my_label.font()
                font.setPointSize(27)
                my_label.setFont(font)
                my_label.setPixmap(QPixmap('Images/file_gena.png'))
                my_label.setScaledContents(True)
                my_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                #  Create a Spin box
                my_spin = QWidget()
                my_spin = QSpinBox()
                my_spin.setMinimum(1)
                my_spin.setMaximum(50)
                my_spin.setPrefix("file ")
                my_spin.setSingleStep(3)
                font = my_spin.font()
                font.setPointSize(19)
                my_spin.setFont(font)
                my_spin.setAlignment(Qt.AlignBottom | Qt.AlignBottom)
                my_spin.valueChanged.connect(self.value_changed)
                my_spin.textChanged.connect(self.value_changed_str)

                # Create a button
                my_button = QWidget()
                my_button = QPushButton("Download")
                my_button.clicked.connect(self.buttonClick(my_button))
                my_button.setGeometry(100,100,130,130)
                my_button.setFont("Georgia")
                font = my_button.font()
                font.setPointSize(19)
                my_button.setFont(font)
                my_button.setIconSize(QSize(19,19))

                # Add widgets to the layout or Put Label on the screen
                vbox.addWidget(my_label)
                vbox.addWidget(my_spin)
                vbox.addWidget(my_button)

                self.setLayout(vbox)
                self.show()

        def buttonClick(self, my_button):
                with open("anyfile.txt", "w") as f:
                        f.write("Hello world!")

        def value_changed(self, i):
                print(i)
        #
        def value_changed_str(self, s):
                print(s)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()