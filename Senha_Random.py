import random
import string

def gerar_senha(tamanho = 8, incluir_maiusculas = True, incluir_numeros = True, incluir_simbolos = True):
    """Gera uma senha aleatória com base nas preferências do usuário."""
    
    #Conjunto de caracteres base para a senha (Letra Maiuscula)
    caracteres = string.ascii_lowercase
    
    #Adiciona outros caracteres de acordo com as preferencias do usuario
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
        
    #gera a senha aleatória usando uma amostra dos caracteres disponíveis
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def exibir_menu():
    """Exibe o menu para configurar e gerar uma senha."""
    print("Gerador de senhas aleatórias")
    
    #configurações da senha
    try:
        tamanho = int(input("Digite o tamanho necessario para a sua senha(mínimo 4): "))
        if tamanho < 4:
            print("Tamanho mínimo de de 4 caracteres. Definindo para 4")
            tamanho = 4
    except ValueError:
        print("Entrada inválida! Usando tamanho padrão de 8 caracteres.")
        tamanho = 8
        
    incluir_maiusculas = input("Incluir letras maiusculas? (s/n):").strip().lower() == "s"
    incluir_numeros = input("Incluir numeros a sua senha? (s/n)").strip().lower() == "s"
    incluir_simbolos = input("Incluir simbolos a sua senha? (s/n)").strip().lower() == "s"
    
    #Gera e exibe a senha com verificação
    senha = gerar_senha(
        tamanho = tamanho,
        incluir_maiusculas = incluir_maiusculas,
        incluir_numeros = incluir_numeros,
        incluir_simbolos = incluir_simbolos
    )
    if senha: #exibe a senha se foi gerada com sucesso
        print(f"Sua senha gerada: {senha}")
    else:
        print("Não foi possível gerar a senha devido à configuração.")
    
#exibe o gerador
exibir_menu()
