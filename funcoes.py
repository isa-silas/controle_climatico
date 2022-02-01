from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, uic


recorrencia = 0
estado = False
timer_confirmado = False
qual_vent = 0


def abrir_controle(janela_controle, ventilador: int):
    """
    [Resumo]
                    Função responsável por abrir a janela de configurações de
                    cada ventilador.

    Args:
            ventilador (int): [nº do ventilador sendo configurado]
    """
    janela_controle.show()
    global qual_vent 
    qual_vent = ventilador



def guardar_recorrencia(btn_recorrencia):
    """
    [Resumo]
            Como diz o nome da funcao, ela é responsável por guardar se a
            configuração do timer deve ser ou evento isolado ou ser repetido 
            sempre. Ademais, ela também altera o texto do botão em que o 
            usuário configura a recorrência toda vez que este é clicado.
    """
    global recorrencia
    if  recorrencia == 0:
        recorrencia = 1
        btn_recorrencia.setText('Retirar Recorrência')
    else:
        recorrencia = 0
        btn_recorrencia.setText('Recorrência')


def confere_horarios(inicio, fim,timer):
    """
    [Resumo]
            Aqui é checado se o horário inicial não é maior que o final e se a
            temporização foi confirmada pelo usuário.
    """
    global timer_confirmado
    
    if inicio.time().hour() >= fim.time().hour():
        timer.label_2.setStyleSheet(
            'QLabel {background-color: #f5050d}')
        timer.label_3.setStyleSheet(
            'QLabel {background-color: #f5050d}')
        timer.btn_confirmar.setText('Tente novamente')
    elif inicio.time().hour() == fim.time().hour() and inicio.time().minute() >= fim.time().minute():
        timer.label_2.setStyleSheet(
            'QLabel {background-color: #f5050d}')
        timer.label_3.setStyleSheet(
            'QLabel {background-color: #f5050d}')
        timer.btn_confirmar.setText('Tente novamente')
    else:
        timer_confirmado = True
        timer.label_2.setStyleSheet(
            'QLabel {background-color: #ffff}')
        timer.label_3.setStyleSheet(
            'QLabel {background-color: #ffff}')
        timer.btn_confirmar.setText('Confirmar')
        print('\n***** confirmado *****\n')


def liga_desliga(btn_on_off,painel):
    global qual_vent
    global estado
    if qual_vent == 1: 
        btn_ventilador = painel.btn_v1
    elif qual_vent == 2:
        btn_ventilador = painel.btn_v2
    
    if estado == False:
        estado = True
        btn_on_off.setText('Desligar')
        btn_ventilador.setStyleSheet(
            'QPushButton {background-color: #4fc97a}')
    else:
        estado = False
        btn_on_off.setText('Ligar')
        btn_ventilador.setStyleSheet(
            'QPushButton {background-color: rgb(156, 156, 156)}')
