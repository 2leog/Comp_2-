import imp
from Integral import Inte
from Limites import Lim
from Calculos_Ele import CEle
from Derivada import Der

class Dis:

    def __init__(self, comando, contas):
        self.comando = comando
        self.resposta = ""
        self.obj = []
        self.contato = ''
        self.contas = contas

    def verifica(self): # Metodo que chama a classe necessaria
        
        match self.comando:

            case "$":
                self.obj = Inte(self.contas) # Classe que recebe uma variavel contas como parametro

            case "@":
                self.obj = Der(self.contas) # Classe que recebe uma variavel contas como parametro
            
            case "&":
                self.obj = Lim(self.contas)  # Classe que recebe uma variavel contas como parametro

            case "*":    
                self.obj = CEle(self.contas) # Classe que recebe uma variavel contas como parametro

        self.obj.loop() # Entra em um loop que espera o comando passado pelo usuário
        

        
    def getSolucao(self):
        self.resposta = self.obj.resposta() # Atributo que recebe o retorno de uma função do objeto criado (Metodo necessário para todas as areas)
        return self.resposta



    def __str__(self):
       print(self.resposta)

        