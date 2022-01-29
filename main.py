from PyQt5 import QtWidgets, uic
import sys
from funcoes import Painel


app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
login = uic.loadUi('tela_login.ui') # Load the .ui file
painel_controle = uic.loadUi('tela_painel_controle.ui')
painel_controle_adm = uic.loadUi('tela_painel_controle_adm.ui')
timer = uic.loadUi('tela_liga_timer.ui')
painel_controle.show() # Show the GUI
painel = Painel(painel_controle,timer)
app.exec_() # Start the application



