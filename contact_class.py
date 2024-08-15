
from PyQt5.QtWidgets import  *
from  add_contact import  *

class ContactWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.oynalar = []
        self.setFixedSize(400,600)
        self.setWindowTitle("Contact oynasi")
        self.Create_nav()
        self.contacts_layot = QVBoxLayout()
        self.contacts = []
        self.vertikal = QVBoxLayout()
        self.vertikal.addLayout(self.nav)



        self.widget = QWidget()
        self.widget.setLayout(self.vertikal)
        self.setCentralWidget(self.widget)


        self.add_btn.clicked.connect(self.Create_contact)


    def Create_nav(self):

        self.label = QLabel("Kontaktlarim")
        self.add_btn = QPushButton("+")
        self.nav = QHBoxLayout()
        self.nav.addWidget(self.label)
        self.nav.addWidget(self.add_btn)
        font = self.font()
        font.setPointSize(25)
        self.label.setFont(font)
        self.add_btn.setFont(font)



    def Create_contact(self):
        oyna = AddContact()
        oyna.show()
        self.oynalar.append(oyna)


