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
    def __init__(self,painel,controle):
        self.qual_vent = 0
        self.janela_controle = controle
        
        self.vent_1 = painel.btn_v1
        self.vent_2 = painel.btn_v2
        
        self.vent_1.clicked.connect(lambda: self.abrir_controle(1))
        self.vent_2.clicked.connect(lambda: self.abrir_controle(2))
        

    def abrir_controle(self, ventilador: int):
        self.janela_controle.show()
        self.qual_vent = ventilador


