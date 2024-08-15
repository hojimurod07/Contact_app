
from  PyQt5.QtWidgets import *

import  json
class  AddContact(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(300,250)

        self.vertical = QVBoxLayout()


        self.line = QLineEdit()
        self.line.setPlaceholderText("Enter name contact: ")
        self.line.setStyleSheet("border: none;font-size: 20px;")

        self.line2 = QLineEdit()
        self.line2.setPlaceholderText("Enter number contact: ")
        self.line2.setStyleSheet("border: none;font-size: 20px;")
        self.buttons = QHBoxLayout()
        self.ok_btn  = QPushButton("Ok")
        self.cansel_btn = QPushButton("Cansel")
        font = self.font()
        font.setPointSize(18)
        self.ok_btn.setFont(font)
        self.cansel_btn.setFont(font)

        self.buttons.addWidget(self.cansel_btn)
        self.buttons.addWidget(self.ok_btn)

        self.vertical.addWidget(self.line)
        self.vertical.addWidget(self.line2)
        self.vertical.addLayout(self.buttons)

        self.w = QWidget()
        self.w.setLayout(self.vertical)
        self.setCentralWidget(self.w)

        self.ok_btn.clicked.connect(self.Malumot_yoz)
        self.ok_btn.clicked.connect(self.close)

    def Malumot_yoz(self):

        import json

        data_name = self.line.text().capitalize()
        data_number = self.line2.text()
        all_contacts = {}

        try:
            # Try reading the existing data
            with open("malumot.json", "r") as file:
                all_contacts = json.load(file)
        except FileNotFoundError:
            # If file doesn't exist, it will be created when writing later
            pass

        # Update the dictionary with new contact
        all_contacts[data_name] = data_number

        # Write updated data back to the file
        with open("malumot.json", "w") as file:
            json.dump(all_contacts, file, indent=4)

        self.close()