from Calculos_Ele import CEle 

class Der: # Os atributos e os dois primeiros metodos, são essenciais para todas as classes

    def __init__(self, contas):
        self.contas = contas
        self.obj_Cele = CEle()
        self.verifica = True

    def prioridade(self): # l

        for i in range(len(self.contas)):

            if self.contas[i] == ')' and self.verifica == True:
                prioritario = [self.contas[i-j] for j in range(0, len(self.contas[0:i:-1]))]
                





    def loop(self): 
        contador = 0

        while True:

            match self.contas[contador]:

                case 'm': # m simboliza multiplicacao

                    self.obj_Cele.multiplica(int(self.contas[contador - 1]), int(self.contas[contador + 1]))
                
                case 'd': # d simboliza divisao

                    self.obj_Cele.divisor(int(self.contas[contador - 1]), int(self.contas[contador + 1]))

                case 's':

                    self.obj_Cele.soma(int(self.contas[contador - 1]), int(self.contas[contador + 1]))

                case ''