def exercicio_nome():
      nome = 'Rondi'
      idade = 35

      print(f'meu nome e {nome} e tenho {idade} anos')
      
      
def exercio_quebra_de_linha():
      #modo 1
      print("""
            A
            L
            U
            R
            A
            """ )

      #modo 2
      letras = ["A", "L", "U", "R", "A"]
      print(*letras, sep="\n")

      #modo 3
      for letra in "ALURA":
            print(letra)


def exercicio_mostrar_pi():
      pi = 3.14159
      arredondado = round(pi, 2)
      print(f'O valor arredondado de pi é: {arredondado}')
      print(f'O valor arredondado de pi é: {pi:.2f}')


def exercicio_verificar_par_impar():
# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

      verificar_numero = int(input('Insira um numero: '))

      if (verificar_numero % 2 == 0):
            print('esse numero e par')
      else:
            print('esse numero e impar')


def exercicio_verificar_idade():
# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias 
# de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

      verificar_idade = int(input('Informe sua idade: '))
      
      if(verificar_idade >=0 and verificar_idade <=12):
            print('Criança')
      elif(verificar_idade >=13 and verificar_idade <=18):
            print('Adolescente')
      elif(verificar_idade > 18): 
            print('Adulto')
      else:
            print('Valor Invalido')
            
            
def exercico_validacao_dados():
# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a 
# senha fornecidos correspondem aos valores esperados determinados por você.

      usuario_correto = 'Rondi'
      senha_correta = 35
      
      usuario = str(input('Qual seu usuario?'))
      senha = int(input('Qual sua senha?'))
      
      if(usuario == usuario_correto and senha == senha_correta):
            print('Usuario e senha corretos')
      elif(usuario == usuario_correto and senha != senha_correta):
            print('Usuario correto e senha incorreta')
      elif(usuario != usuario_correto and senha == senha_correta):
            print('Usuario incorreto e senha correta')
      else:
            print('Usuario e senha incorretos')
                     

def exercicio_plano_cartesiano():
# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else 
# para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

      x = int(input('Digite o valor de x: '))
      y = int(input('Digite o valor de y: '))
      
      if(x >0 and y>0):
            print('Primeiro Quadrante')
      elif(x<0 and y>0):
            print('Segundo Quadrante')
      elif(x<0 and y<0):
            print('Terceiro Quadrante')
      elif(x>0 and y <0):
            print('Quarto Quadrante')
      else:
            print('O ponto está localizado no eixo ou origem')      
            
            
def exemplos_GPT_for():
      # Somar números de uma lista
      numeros = [1, 2, 3, 4, 5]
      soma = 0
      for numero in numeros:
            soma += numero
      print(f"Soma: {soma}")

      # Contar caracteres específicos
      texto = "Python é incrível"
      contador = 0
      for caractere in texto:
            if caractere.lower() == 'i':
                  contador += 1
      print(f"Letra 'i' aparece {contador} vezes")

      # Criar uma nova lista com condições
      numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      pares = []
      for numero in numeros:
            if numero % 2 == 0:
                  pares.append(numero)
      print(f"Números pares: {pares}")


def listas_simples():
# 1 - Crie uma lista para cada informação a seguir:
# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

      numeros = [1,2,3,4,5,6,7,8,9,10]
      for numero in numeros:
            print(numero)
            
      lista_de_nomes = ['Rondi','Maura', 'Samara', 'Heitor']
      for nomes in lista_de_nomes:
            if nomes == 'Rondi':
                  print(nomes)
                  
      lista_datas = [1990,2025]
      idade = lista_datas[1] - lista_datas[0]
      print(f'{lista_datas[1]} - {lista_datas[0]} = {idade}')
                  
                  
def loop_simples():
# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
      mercado = ['macarrao','arroz','oleo']
      for produtos in mercado:
            print(produtos)


def soma_impares_loop():
# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
      numeros = [1,2,3,4,5,6,7,8,9,10]
      soma = 0
      for numero in numeros:
            if(numero % 2 != 0):
                  soma += numero
      print(f'Resultado final: {soma}') # fora do loop
      
      soma_impares = 0
      for impares in range(1,11,2):
            soma_impares += impares
            print(soma_impares) # dentro do loop
                  

def contador_1_a_10():
# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
      contador = 10
      while(contador > 0):
            print(contador)
            contador -= 1
            
      for contador in range(10,0,-1):
            print(contador)


def tabuada():
# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
      numerador = int(input('Inorme o numerador: '))
      quantidade_de_multiplicacoes = int(input('Quantas vezes deseja que esse numero seja multiplicado: '))
      
      for i in range(1,quantidade_de_multiplicacoes +1):
            resultado = numerador * i
            print(f'{numerador} x {i} = {resultado}')


def try_except():
# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
      numeros_e_outros = [1,2,3,4,True,6,7,'abc',9,10]
      soma = 0
      try: 
            for numeros in numeros_e_outros:
                  if isinstance(numeros,int) and not isinstance(numeros,bool):
                        soma += numeros
                  print(soma)      
      except Exception as e:
            print(f'Erro: {e}')
     
      
def media_lista():
    # 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
    numeros_e_outros = [1,2,3,4,True,6,7,'abc',9,25]
    soma = 0
    quantidade = 0

    try:
        for numeros in numeros_e_outros:
            if isinstance(numeros, (int, float)) and not isinstance(numeros, bool):
                soma += numeros
                quantidade += 1
        tamanho_da_lista = len(numeros_e_outros)
        print(f'Tamanho da lista: {tamanho_da_lista}')
        print(f'Soma dos números válidos: {soma}')
        print(f'Quantidade de números válidos: {quantidade}')
        print(f'Média dos números válidos: {soma/quantidade}')
    except ZeroDivisionError:
        print("A lista está vazia, não é possível calcular a média.")
    except Exception as e:
        print(f'Ocorreu um erro ao calcular a média: {e}')

