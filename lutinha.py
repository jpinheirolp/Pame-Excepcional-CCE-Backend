import random

class Lutador:
    def __init__(self, nome, peso, forca , ginga, arteMarcial="MMA"): # ginga,também chamada de agilidade ou destreza pelos leigos. 
        if (not( isinstance(nome, str))):
            print("Atributo nome tem que ser do tipo string.")
            return None
        if (not( isinstance(peso, int ) or isinstance(peso, float ))):
            print("Atributo peso tem que ser do tipo int ou float.")
            return None
        if (not( isinstance(forca, int))):
            print("Atributo forca tem que ser do tipo int.")
            return None
        if (not( isinstance(ginga, int))):
            print("Atributo ginga tem que ser do tipo int.")
            return None
        if (not( isinstance(arteMarcial, str))):
            print("Atributo arteMarcial tem que ser do tipo string.")
            return None
        
        self.nome = nome
        self.peso = peso
        self.forca = forca
        self.arteMarcial = arteMarcial
        self.ginga = ginga
        self.historicoDeLutas = []
    
    def __repr__(self):
        return f'Pesando incríveis {self.peso} kilos, com uma inacreditável força de {self.forca}, uma ginga invejável de {self.ginga} , mestre em {self.arteMarcial}. O inigualável Luuutador {self.nome}!!! '

    def atualizaHistorico(self,resultadoLuta):
        self.historicoDeLutas += [resultadoLuta]

class Luta:
    def __init__(self, lutador1, lutador2):   
        if(not( isinstance(lutador1,Lutador) and isinstance(lutador2,Lutador))):
            print("Atributos da classe Luta devem pertencer a classe Lutador")
            return None
        
        diferncaPeso = abs(lutador1.peso - lutador2.peso)
        if( diferncaPeso > 6 ):
            print("Lutadores não podem ter pesos muito diferentes")
            return None
        self.lutador1 = lutador1
        self.lutador2 = lutador2
    
    def __repr__(self):
        return f'O grande comfronto de {self.lutador1.nome} contra {self.lutador2.nome}!'
    
    def informacoes(self):
        print(f'No canto direito {self.lutador1.nome} pesando {self.lutador1.peso}, com força de {self.lutador1.forca}, ginga de {self.lutador1.ginga} especializado em {self.lutador1.arteMarcial}, no canto esquerdo o adversário {self.lutador2.nome} pesando {self.lutador2.peso}, com força de {self.lutador2.forca}, ginga de {self.lutador2.ginga} especializado em {self.lutador2.arteMarcial}')
    
    def registraCombate(self):
        
        pontosL1 = self.lutador1.forca + self.lutador1.ginga
        pontosTotais = pontosL1 + self.lutador2.forca + self.lutador2.ginga
        chanceDeVitoriaL1 = pontosL1 / pontosTotais
        acaso = random.random()
        resultadoL1 = chanceDeVitoriaL1 >= acaso
        
        self.lutador1.atualizaHistorico(['vitoria']) if resultadoL1 else self.lutador1.atualizaHistorico(['derrota'])
        self.lutador2.atualizaHistorico(['vitoria']) if not(resultadoL1) else self.lutador2.atualizaHistorico(['derrota'])
        
        vencedor = self.lutador1.nome if resultadoL1 else self.lutador2.nome
        print(f'{vencedor} venceu o confronto de hoje! Palmas para ele!! (barulho de palmas)')

luchador1 = Lutador('Kleber',120,5000,3000,"capoeira")
print(luchador1)

luchador2 = Lutador('Waldisney',125,5050,2400,"muay thai")
print(luchador2)

lucha = Luta(luchador1,luchador2)
print(lucha)

lucha.registraCombate()
lucha.registraCombate()
lucha.registraCombate()
lucha.informacoes()
print(luchador1.historicoDeLutas,luchador2.historicoDeLutas)

luchador3 = Lutador('Jamon',145,2000,5090)
luchador4 = Lutador('Guilhermo',85,2100,4050)
combateInvalido = Luta(luchador3,luchador4)

luchador5 = Lutador("so","para","testar","mes","mo")

lucha2 = Luta(luchador5,22)
