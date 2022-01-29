from PyQt5 import QtWidgets, uic
import sys

app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
login = uic.loadUi('tela_login.ui') # Load the .ui file
painel_controle = uic.loadUi('tela_login.ui')
login.show() # Show the GUI
app.exec_() # Start the application

