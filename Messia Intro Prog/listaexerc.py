#Questa1 1Descrição: Um mapa do tesouro tem duas partes, A e B. A primeira parte está escondida no X número de passos para o norte, e a segunda no Y número de passos para o leste. 
# Crie um programa que receba os valores de X e Y e calcule a distância total que o pirata precisa percorrer para chegar ao tesouro (soma de X e Y). 
nortex = int(input("digite o numero de passo x"))
lestey = int(input("digite o numero de passo y"))
total_de_passos = nortex+lestey
print("O total de passos é de:{total_de_passos}")


#Questao 2Um guerreiro precisa de uma armadura especial para a batalha. 
#Para forjar a armadura, ele precisa de uma liga metálica que combina ferro e ouro. 
#O ferreiro diz que a liga precisa ter no mínimo 70% de ferro.
# Crie um programa que receba a quantidade de ferro e ouro em kg e verifique se a porcentagem de ferro na liga é suficiente. 
qnt_ferro =int(input("quantidade de ferro"))
qnt_ouro =int(input("quantidade de ouro"))
liga_da_armadura = qnt_ferro+qnt_ouro
porcentagem_ferro = (qnt_ferro/liga_da_armadura)*100
if porcentagem_ferro >= 70:
    print("A porcentagem de ferro na liga é suficiente para forjar")
else:
    print("A porcentagem de ferro na liga não é suficiente para forjar")


    #Questao3 Imagine que você é um mago que pode adivinhar o animal favorito das pessoas.
    # Crie um programa que pergunte à pessoa se seu animal favorito é mamífero ou réptil.
    # Se for mamífero, o programa deve sugerir que é um cachorro; se for réptil, o programa deve sugerir que é uma tartaruga.
    def funcao_processamento():
      print('Digite seu animal favorito:')
      print('\n1- Mamífero  \n2 - Réptil')
    escolha = int(input("qual sua opção?"))
    if escolha == 1:
        print("certeza que é um doggola")
    else:
        print('Dever ser uma tortuga')


#Um colecionador de moedas tem 3 tipos de moedas: de 1 real, de 50 centavos e de 25 centavos.
#Escreva um programa que receba a quantidade de cada tipo de moeda e calcule o valor total que o colecionador tem. 
qnt_umreal = int(input("quantidade de moedas de um real"))
qnt_50cent = float(input("quantidade de moedas de 50 centavos"))
qnt_25cent = float(input("quantidade de moedas de 25 centavos"))
valor_total = (qnt_umreal*1)+(qnt_50cent*0.5)+(qnt_25cent*0.25)
print("O valor total é de: {valor_total}")


#Um explorador está cruzando um deserto. Ele precisa saber se a quantidade de água que tem é suficiente para chegar ao próximo oásis.
# Ele calcula que precisa de 2 litros de água para cada quilômetro.
# Crie um programa que receba a quantidade de água disponível e a distância até o oásis, e informe se a água é suficiente. 
def agua_suficiente(agua_disponivel, distancia_oasis):
  # Calcule a água necessária para alcançar o oásis
  agua_necessaria = distancia_oasis * 2  # 2 litros por quilômetro

  # Verifique se a água disponível é suficiente
  if agua_disponivel >= agua_necessaria:
    return True
  else:
    return False
agua_disponivel = float(input("Digite a quantidade de água disponível (em litros): "))
distancia_oasis = float(input("Digite a distância até o oásis (em quilômetros): "))
if agua_suficiente(agua_disponivel, distancia_oasis):
  print("Você tem água suficiente para alcançar o oásis!")
else:
  print("Você não tem água suficiente para alcançar o oásis.")


#Em um campeonato de corrida de dragões, cada dragão corre uma determinada distância em um certo tempo.
#Crie um programa que receba a distância e o tempo de dois dragões diferentes e determine qual dragão é mais rápido, ou se ambos têm a mesma velocidade. 

#Dragao1
distancia_dragao_1= float (input("Distancia percorrida pelo dragão 1"))
tempo_dragao_1= float (input("DTempo do  dragão 1"))
velocidade_dragao_1 = (distancia_dragao_1/tempo_dragao_1)


#Dragao2
distancia_dragao_2= float(input("Distancia percorrida pelo dragão 2"))
tempo_dragao_2= float(input("DTempo do  dragão 2"))
velocidade_dragao_2 = (distancia_dragao_2/tempo_dragao_2)

if velocidade_dragao_1 > velocidade_dragao_2:
   print('O Dragão 1 é mais rápido')
elif velocidade_dragao_1 < velocidade_dragao_2:
    print('o Dragão 2 é mais rápido')
else:
     print('Os dois tem a mesma velocidade')



