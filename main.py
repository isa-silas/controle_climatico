from PyQt5 import QtWidgets, uic
import sys
from funcoes import abrir_controle, guardar_recorrencia, liga_desliga,confere_horarios

app = QtWidgets.QApplication(sys.argv) 

login = uic.loadUi('tela_login.ui') # Load the .ui file
painel_controle = uic.loadUi('tela_painel_controle.ui')
painel_controle_adm = uic.loadUi('tela_painel_controle_adm.ui')
timer = uic.loadUi('tela_liga_timer.ui')
status = uic.loadUi('tela_adm_status.ui')

# Teste painel controle
painel_controle.show() 
painel_controle.btn_v1.clicked.connect(lambda x: abrir_controle(timer,1))
painel_controle.btn_v2.clicked.connect(lambda x: abrir_controle(timer,2))
timer.btn_recorrencia.clicked.connect(lambda: guardar_recorrencia(timer.btn_recorrencia))
timer.btn_on_off.clicked.connect(lambda: liga_desliga(timer.btn_on_off,painel_controle))
timer.btn_confirmar.clicked.connect(lambda: confere_horarios(timer.time_inicio,timer.time_fim,timer))

app.exec_() # Start the application







