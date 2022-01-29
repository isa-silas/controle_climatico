# from main import painel_controle as painel
# from main import timer as controle


class Painel:
    def __init__(self,painel,controle):
        self.janela_controle = controle
        self.vent_escritorio = painel.btn_v1
        self.vent_oficina = painel.btn_v2
        self.vent_escritorio.clicked.connect(self.abrir_controle)
        self.vent_oficina.clicked.connect(self.abrir_controle)
        

    def abrir_controle(self):
        self.janela_controle.show()


