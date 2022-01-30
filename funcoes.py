from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, uic


class Painel:
        """
        [Resumo]

                Essa classe serve para conectar o painel de controle com as telas de
                configuracao de cada ventilador

        [Obs]
                self.qual_vent = guarda qual ventilador esta sendo configurado

                self.janela_controle = tela do timer para user comum e de status dos
                ventiladores para adm
        """

        def __init__(self, painel, controle):
                self.qual_vent = 0
                self.janela_controle = controle

                self.vent_1 = painel.btn_v1
                self.vent_2 = painel.btn_v2

                self.vent_1.clicked.connect(lambda: self.abrir_controle(1))
                self.vent_2.clicked.connect(lambda: self.abrir_controle(2))

        def abrir_controle(self, ventilador: int):
            """
            [Resumo]
                            Função responsável por abrir a janela de configurações de
                            cada ventilador.

            Args:
                    ventilador (int): [nº do ventilador sendo configurado]
            """
            self.janela_controle.show()
            self.qual_vent = ventilador

            if self.qual_vent == 1:
                self.timer = Timer(self.vent_1, self.janela_controle)
            elif self.qual_vent == 2:
                self.timer = Timer(self.vent_2, self.janela_controle)


class Timer:
    """
    [Resumo] 
            Essa classe contem funções e variáveis responsáveis pelo controle
            do estado do ventilador sendo configurado.

    [Obs]
            self.estado = False -> Ventilador Desligado
            self.estado = True -> Ventilador Ligado
    """

    def __init__(self, painel_btn, timer):
        self.inicio = timer.time_inicio
        self.fim = timer.time_fim

        self.recorrencia = 0
        self.timer_confirmado = False
        self.estado = False

        self.btn_on_off = timer.btn_on_off
        self.btn_recorrencia = timer.btn_recorrencia
        self.btn_confirmar = timer.btn_confirmar
        self.btn_ventilador = painel_btn

        self.btn_on_off.clicked.connect(self.liga_desliga)
        self.btn_recorrencia.clicked.connect(self.guardar_recorrencia)
        self.btn_confirmar.clicked.connect(self.confere_horarios)

    def guardar_recorrencia(self):
        """
        [Resumo]
                Como diz o nome da funcao, ela é responsável por guardar se a
                configuração do timer deve ser ou evento isolado ou ser repetido 
                sempre. Ademais, ela também altera o texto do botão em que o 
                usuário configura a recorrência toda vez que este é clicado.
        """
        if self.recorrencia == 0:
            self.recorrencia = 1
            self.btn_recorrencia.setText('Retirar Recorrência')
        else:
            self.recorrencia = 0
            self.btn_recorrencia.setText('Recorrência')

    def confere_horarios(self):
        """
        [Resumo]
                Aqui é checado se o horário inicial não é maior que o final e se a
                temporização foi confirmada pelo usuário.
        """
        if self.inicio.time().hour() >= self.fim.time().hour():
            erro = uic.loadUi('tela_erro_horario.ui')
            erro.show()
        elif self.inicio.time().hour() == self.fim.time().hour() and self.inicio.time().minute() >= self.fim.time().minute():
            erro = uic.loadUi('tela_erro_horario.ui')
            erro.show()
        else:
            self.timer_confirmado = True
            print('\n***** confirmado *****\n')

    def liga_desliga(self):
        if self.estado == False:
            self.estado = True
            self.btn_on_off.setText('Desligar')
            self.btn_ventilador.setStyleSheet(
                'QPushButton {background-color: #4fc97a}')
        else:
            self.estado = False
            self.btn_on_off.setText('Ligar')
            self.btn_ventilador.setStyleSheet(
                'QPushButton {background-color: rgb(156, 156, 156)}')
