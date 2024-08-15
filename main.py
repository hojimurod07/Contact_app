

from  PyQt5.QtWidgets import  *

from  contact_class import  *


app  = QApplication([])

window = ContactWindow()
window.show()
app.exec_()