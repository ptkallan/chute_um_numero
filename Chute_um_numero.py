# Criar um algoritmo que gera um valor aleatório que requer inúmeras tentativas até acerto o valor gerado
import random
import PySimpleGUI as sg

class ChuteUmNumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Seu chute',size=(20,0))],
            [sg.Input(size=(18,0),key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(30,10))]
        ]
        # Janela
        self.janela = sg.Window('Chute um número!',layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                # receber valores
                self.LerValoresDaTela()
                # Fazer alguma coisa com estes valores
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print("Chute um valor mais baixo!")
                            self.LerValoresDaTela()
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print("Chute um valor mais alto!")
                            self.LerValoresDaTela()
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print("Acerto miseravi!!")
                            break

        except:
            print('Favor digitar apenas números!')
            self.Iniciar()

    def LerValoresDaTela(self):
        self.evento, self.valores = self.janela.Read()

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)

chute = ChuteUmNumero()
chute.Iniciar()