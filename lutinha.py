import random
class Lutador:
    def __init__(self, nome, peso, forca):
        self.nome = nome
        self.peso = peso
        self.forca = forca
        self.historicoDeLutas = []
    def __repr__(self):
        return f'Pesando incríveis {self.peso} kilos, com uma inacreditável força de {self.forca} newtons, O inigualável Luuutador {self.nome}!!! '

class Luta:
    def __init__(self, lutador1, lutador2):
        diferncaPeso = abs(lutador1.peso - lutador2.peso)
        if( diferncaPeso > 6 ):
            print("Lutadores não podem ter pesos muito diferentes")
            return None
            
        self.lutador1 = lutador1
        self.lutador2 = lutador2
    def __repr__(self):
        return f'O grande comfronto de {self.lutador1.nome} contra {self.lutador2.nome}!'
    def informacoes(self):
        print(f'No canto direito {self.lutador1.nome} pesando {self.lutador1.peso} com força de {self.lutador1.forca}, no canto esquerdo o adversário {self.lutador2.nome} pesando {self.lutador2.peso} com força de {self.lutador2.forca}')
    def registraCombate(self):
        chanceDeVitoriaL1 = self.lutador1.forca / (self.lutador1.forca + self.lutador2.forca)
        acaso = random.random()
        resultadoL1 = chanceDeVitoriaL1 >= acaso
        self.lutador1.historicoDeLutas += ['vitoria'] if resultadoL1 else ['derrota']
        self.lutador2.historicoDeLutas += ['vitoria'] if not(resultadoL1) else ['derrota']
        vencedor = self.lutador1.nome if resultadoL1 else self.lutador2.nome
        print(f'{vencedor} venceu o confronto de hoje! Palmas para ele!! (barulho de palmas)')

luchador1 = Lutador('Kleber',120,5000)
print(luchador1)
luchador2 = Lutador('Waldisney',125,5050)
print(luchador2)
lucha = Luta(luchador1,luchador2)
print(lucha)
lucha.registraCombate()
lucha.registraCombate()
lucha.registraCombate()
lucha.informacoes()
print(luchador1.historicoDeLutas,luchador2.historicoDeLutas)
luchador3 = Lutador('Jamon',145,5090)
luchador4 = Lutador('Guilhermo',85,4050)
combateInvalido = Luta(luchador3,luchador4)


