import random
import string
def criar_senhaboa(length, uppercase,lowercase, number, special):
    #Criar também uma senha com opções de tamanho de caracteres, complexidades e tipos de caracteres
    
    #Definir os caracteres
    uppercase_chars= string.ascii_uppercase if uppercase else ''
    lowercase_char = string.ascii_lowercase if lowercase else ''
    number_char = string.digits if number else ''
    special_char = string.punctuation if special else ''

    #Combinando os caracteres em uma única string de caracteres possíveis

    possible_chars= uppercase_chars + lowercase_char + number_char + special_char

    #Ter certeza que a senha tenha pelo menos 8 caracteres
    length= max(length, 8)

    #Criando a senha 
    senha = ''.join(list(random.choice(possible_chars) for i in range(length)))

    #Salvando a senha para um arquivo de texto 
    with open ("senhas.txt", 'a') as f:
        f.write(senha + "\n")
        return senha
    
 # Exemplo de uso   
senha = criar_senhaboa(length=11, uppercase=True, lowercase=True, number=True, special=True)
print(senha)  