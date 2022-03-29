import math
import random
import banana
########################################################
print('olá mundo')
#######################################################
c = str(input('qual é seu nome amigo?; '))
print(f'seja bem víndo caro amigo {c}')

#############################################################

D = (input('digite qualquer coisa amigo  '))
print('esse elemento e ',type(D))
###############################################################

v1 = float(input('Digite um número por favor : '))
v2 = float(input('Digite um número outro numero : '))


resultado = banana.soma(v1, v2)
print(f'o resultado da soma desses dois numeros foi {resultado}')
###############################################################
C = float(input('digite um numero e eu direi seu sucessor e seu antecesor: '))
o = C - 1
a = C + 1
print(f'o antecessor de {C} é {o} e seu sucessor é {a}')
##########################################################
E = int(input('digite um numero camarada : '))

s = math.sqrt(E)
p = E * 2
i = E * 3

print(f'a raiz quadrada do numero que voce colocou é {s}, seu dobro é {p} , e seu triplo é {i}')
###############################################################
n1 = int(input('Digite um número inteiro por favor que eu direi a sua media de aritimetica : '))
n2 = int(input('Digite mais um numero por favor : '))
n3 = int(input('mais um  : '))
n4 = int(input('só mais esse : '))

resultado = banana.media(n1, n2, n3, n4)
print(f'a madia de aritimetica desses numeros foi {resultado}')
###############################################################
c = int(input('irei coververter o numero que você me der em centimetro e milimetro : '))

r = c * 10 ** -2
i = c * 10 ** -3



print(f'analisando os dados que você me deu, ao convertelo em centimetro deu {r}cm e transformando esse mesmo numero em milimietro deu {i}mm ')

####################################################################

v = float(input('me dê um numero por favor : '))


banana.tabuada(v)

#######################################################
J = float(input('quanto dinheiro você tem na sua carteira? :'))
dolar = J/1.00
print(f'com o dinheiro que você tem da pra compra {dolar} US$')
#########################################################
n1 = float(input('quantos metros de altra tem a sua parede?: '))
n2 = float(input('quatos metros de largura tem a sua parede?: '))

resultado = banana.pintar(n1,n2)
print(f'você vai precisar de {resultado} baldes de tita')
############################################################
D = float(input('ola camarada sou um bom vendedor , por isso irei te dar um desconto. me diga o valor e eu irei dar 5% de desconto: '))

desconto = D - (D * 5 /100)

print(f'o valor do produto com desconto é {desconto}R$')
###############################################################


banana.salario()
print(f'seu salar io agora é {resultado}')
###################################################################
banana.temperatura()

##############################################################
banana.aluguel()
############################################################
g1 = float(input('digite qualquer numero aqui: '))
n = math.trunc(g1)
print(f'a parte inteira do seu numero é {n}')
##############################################################
vo = float(input('comprimento do cateto oposto: '))
va = float(input('comprimrnto do cateto adjacente: '))
vh = math.hypot(vo,va)
print(f'a hipotenuza vai medir {vh}')
###############################################################
a = float(input('digite o ângulo desejado: '))
s = math.sin(math.radians(a))

print(f'o ângulo de {a} tem o SENO de {s}' )

c = math.cos(math.radians(a))
print(f'o ângulo de {a} tem o COSENO de {c}' )

t = math.tan(math.radians(a))
print(f'o ângulo de {a} tem a TANGENTE de {t}' )
####################################################################
n1 = str(input('nome do primeiro aluno: ' ))
n2 = str(input('nome do segundo aluno: '))
n3 = str(input('nome do terceiro aluno: ' ))
n4 = str(input('nome do quarto aluno: ' ))
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print(f'o aluno que se ferrou pra limpar o quadro só vai ser o {escolhido}')
#################################################################
n1 = str(input('nome do primeiro aluno: ' ))
n2 = str(input('nome do segundo aluno: '))
n3 = str(input('nome do terceiro aluno: ' ))
n4 = str(input('nome do quarto aluno: ' ))
lista = [n1,n2,n3,n4]
escolhido = random.shuffle(lista)
print(f'a ordem de alunos que para apresentar o trabalho será')
print(lista)
################################################################
#não consseguir fazer o exercicio de mp3
##############################################################

j1 = str(input('digite seu nome aqui po favor nome por favor'))
print('colocando esse nome para maiusculo fica {}'.format(j1.upper()))
print('e menucula fica{}'.format(j1.lower()))
################################################
n = int(input('Digite um número entre 0 e 9999: '))
n2 = str(int(10000 + n))
print('O número {} possui, {} milhares.'.format(n, n2[1]))
print('O número {} possui, {} centenas. '.format(n, n2[2]))
print('O número {} possui, {} dezenas. '.format(n, n2[3]))
print('O número {} possui, {} unidades.'.format(n, n2[4]))

###########################################################

nome=str(input("Introduza o nome da cidade: ")).strip()
print("santo" in nome.lower())

###########################################################

nome=str(input("diga seu nome completo: ")).strip()
print("silva" in nome.lower())
print('valeu!')

###########################################################

frase = str(input('digite uma frase: ')).strip().lower()
print('a letra a (sem acento) aparece',frase.count('a'),'vezes na frase.')
print('a posição que o a está é',frase.find('a')+1)
print('a letra a apareceu por ultimo na posição',frase.rfind('a')+1)

###################################################################
nome = str(input('digite seu nome: ')).strip().lower()
print('seu nome (sem acento) aparece',nome.count('nome'),'vezes na frase.')
print('a posição que o nome está é',nome.find('a')+1)
print('seu nome apareceu por ultimo na posição',nome.rfind('nome')+1)


###############################################################
from random import randint
from time import sleep
comp = randint (0, 5)
print('vou pensar em um numero de 0 a 5 adivinhe!')
jogador =int(input('em que numero eu pensei ? '))
print('calma processando...')
sleep(3)
if jogador == comp:
 print('parabens você ganhou !')
else:
 print('vc perdeu hehehe!')

#############################################################

velo = int(input('Velocidade(Km/h): '))
print(f'MULTADO! Você excedeu o limite de 80Km/h e agora deve pagar uma multa de R${(velo - 80)*7:.2f}!' if velo > 80 else 'Dentro dos limites de velocidade!')
print('Dirija com cuidado!')

##############################################################

número = int(input('me diga um número qualquer: '))
if número % 2 == 0:
    print(número,'é par.')
else:
    print(número,'é impar.')

################################################################

km = float(input('Qual a distância em (Km) você deseja percorrer? '))
if km <= 200:
    print('Sua passagem vai custar {} reais. '.format(km * 0.5))
else:
    print('Sua passagem vai custar {} reais. '.format(km * 0.45))

###########################################################

import calendar
ano = int(input('Digite o ano: '))
ano6 = calendar.isleap(ano)
if ano6 is True:
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')

###################################################################

primeiro = int(input('Digite o primeiro número: 3'))
segundo = int(input('Digite o segundo número:'))
terceiro = int(input('Digite o terceiro número:'))
numeros = [primeiro, segundo, terceiro]

print('O maior valor digitado foi {}'.format(max(numeros)))
print('O menor valor digitado foi {}'.format(min(numeros)))


##################################################################

salario = float(input('Informe o salário do funcionário: '))
if salario <=1250:
    print('Seu salário terá um aumento de 15%!!')
    print(f'O valor do seu salario era {salario} e agora será de R${(salario*0.15)+salario:.2f}')
else:
    print('Seu salário terá um aumento de 10%!!')
    print(f'O valor do seu salario era {salario} e agora será de R$ {(salario*0.10)+salario:.2f}')


##########################################################

a = float(input('Coloque o valor de um lado: '))
b = float(input('Coloque o valor de outro lado: '))
c = float(input('Coloque o valor de outro lado: '))

if abs( b - c) < a <  b + c and abs( a - c ) < b < a + c and abs( a - b ) < c < a + b:
    print('Os lados {}, {} e {} podem formar triângulo.'.format(a,b,c))
else:
    print('Os lados {}, {} e {} não podem formar triângulo.'.format(a,b,c))
