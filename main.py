import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QGroupBox, QHBoxLayout, QPushButton, \
    QVBoxLayout, QProgressBar


class SmartWasteDisposalWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Smart Waste Disposal")
        self.setGeometry(300, 150, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.smart_container_progress_bar = QProgressBar()

        main_layout = QGridLayout()
        self.central_widget.setLayout(main_layout)

        buttons_groupbox = self.create_button_groupbox()
        smart_container_groupbox = self.create_progressbar_groupbox()

        main_layout.addWidget(buttons_groupbox, 0, 0, 1, 1)
        main_layout.addWidget(smart_container_groupbox, 1, 0, 1, 1)



    def create_button_groupbox(self):
        buttons_groupbox = QGroupBox("Operator Buttons")
        buttons_layout = QHBoxLayout()
        buttons_groupbox.setLayout(buttons_layout)

        empty_container_button = QPushButton("Empty container", self)
        # empty_container_button.clicked

        restore_button = QPushButton("Restore", self)
        # restore_button.clicked

        buttons_layout.addWidget(empty_container_button)
        buttons_layout.addWidget(restore_button)

        return buttons_groupbox


    def create_progressbar_groupbox(self):
        smart_container_groupbox = QGroupBox("Smart Container Storage")
        smart_container_layout = QVBoxLayout()
        smart_container_groupbox.setLayout(smart_container_layout)

        self.smart_container_progress_bar.setOrientation(1)
        self.smart_container_progress_bar.setMinimum(0)
        self.smart_container_progress_bar.setMaximum(100)
        self.smart_container_progress_bar.setValue(10) #just an example

        smart_container_layout.addWidget(self.smart_container_progress_bar)

        return smart_container_groupbox


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = SmartWasteDisposalWindow()
    window.show()
    sys.exit(app.exec_())
