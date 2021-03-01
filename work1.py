############# PROBLEMA 1 #############

''' 
Pretende-se desenvolver um programa que obtenha um texto a partir da linha de comandos e
converta esse texto da seguinte forma:

• O texto deve ser ordenado de forma inversa, i.e., se a entrada for “ola” o sistema converte
para “alo”
• As vogais devem ser convertidas para maiúsculas (se forem minúsculas) ou para minúsculas
(se forem maiúsculas)

Exemplos de testes:
➢ Introduza um texto: Um bom dia a todos!
A aplicação deve escrever na consola:
➢ !sOdOt A AId mOb mu 
'''

# NOTA: não é permitido usar funções e extensões de Python, como replace(). Devem limitar-se à utilização dos comandos aprendidos em aula.

# Apresentação do trabalho e seu objetivo
print("\nOlá, estamos a fazer um trabalho de grupo e esta é a 1ª parte. O objetivo é desenvolver um programa para a inversão e substituição de letras de um texto à escolha de acordo com as seguintes regras:")
print("- O texto deve ser ordenado de forma inversa, i.e., se a entrada for “ola” o sistema converte para “alo”")
print("- As vogais devem ser convertidas para maiúsculas (se forem minúsculas) ou para minúsculas (se forem maiúsculas)")
input("\nVamos então começar? Prima enter...n\")
      
# Input do user
string = input('Escreva um texto: ')
# Inversão do texto do input
string_reverse = string[::-1]

string_final = ''
for s in string_reverse:
    # Adiciona apenas as consoantes ao string final
    if s in string_reverse and s not in 'aeiouAEIOU':
        string_final += s
    # Se tiver vogais minusculas coloca em maiusculas na string final
    elif s == 'a':
        string_final += 'A'
    elif s == 'e':
        string_final += 'E'
    elif s == 'i':
        string_final += 'I'
    elif s == 'o':
        string_final += 'O'
    elif s == 'u':
        string_final += 'U'
    # Se tiver vogais maiusculas coloca em minusculas na string final
    elif s == 'A':
        string_final += 'a'
    elif s == 'E':
        string_final += 'e'
    elif s == 'I':
        string_final += 'i'
    elif s == 'O':
        string_final += 'o'
    elif s == 'U':
        string_final += 'u'

# Imprime o string final no terminal
print(string_final)

      
############## PROBLEMA 2 ################

'''
Pretende-se desenvolver um programa de radiciação, i.e, para o cálculo de raízes , considerando
que a solução é o valor V, se Vn = a

O programa deve receber como parâmetros os valores de n e de a, imprimindo o valor de V como
resultado. Adicionalmente, deve ter um parâmetro para escolher o algoritmo de implementação,
sendo possível optar por G (algoritmo de Guess and Check), A (algoritmo de soluções aproximadas) e
B (algoritmos de bissecção).

Devem seguir o exemplo das aulas (que ilustra a implementação dos três algoritmos para a raiz cúbica)
e adaptá-lo para que funcione com quaisquer valores e imprima também o número de iterações
necessárias para chegar ao resultado.
'''
      
 # Apresentação do programa de radiação e a opção de escolha de dois parâmetros para o user introduzir
print('\nOlá, esta é a 2ª parte do nosso trabalho de grupo.\n')
input('Prima enter para continuar...\n')
print('Pretende-se desenvolver um programa de radiação para o Cálculo de Raízes. Basta inserir um número qualquer à escolha, o índice da raíz desse número e será dado o resultado juntamente com o número de tentativas que foram necessárias para o programa concluir o cálculo.\n')
input('Prima enter para continuar...\n')
print('Para chegar à resolução da raíz existem três algorítmos que pode escolher: G, A ou B\n')
input('Prima enter para continuar...\n')
print('G é o algoritmo de Guess and Check, A é o algoritmo de Soluções Aproximadas e B é o algoritmo de Bissecção\n')

# user input na escolha de algorítmo, número e índice de radiação
algo = input('Escolha o algorítmo G, A ou B: ')
num = float(input('\nEscolha um número para calcular a sua raíz: '))
raiz = int(input('\nEscolha o índice da raíz: '))

# Colocou-se algumas restrições tendo em conta as propriedades do cálculo de raízes.
if raiz < 0:
  print('\nO índice da raíz tem de ser inteiro e maior que 0.')
elif raiz == 0:
  print('\nA raíz de índice 0 é sempre 1.')
elif raiz%2 == 0 and num < 0:
  print('\nNão é possível calcular a raíz de índice par e de um valor negativo.')
elif raiz == 1:
  print('\nA raíz de índice 1 de um radicando é sempre igual ao valor do radicando, neste caso', num)
# Se passar as restrições vai ser executado o código correspondente à escolha do algoritmo.
else:
  count = 0
  num_abs = abs(num)
  guess = 0.0
  epsilon = 0.01
  increment = 0.0001

  # Algoritmo G

  if algo == 'g' or algo == 'G':
    '''utilizei um while loop porque o input pode ser decimal e embora sendo possivel usar um for loop o código fica mais clean - range() não admite floats'''
    while guess**raiz < num_abs:
      guess += 0.01
    if guess**raiz != num_abs:
      print(num, 'não é uma raiz de índice', raiz, 'perfeita.')
    else:
      if num < 0:
        guess = -guess
      print('\nA raiz de índice', raiz, 'do número', num, 'é', guess,'.')

  # Algoritmo A

  elif algo == 'a' or algo == 'A':
    # se o input for maior que um ou negativo
    if num >= 1 or num <= 0:
      while abs(guess**raiz - num_abs) >= epsilon and guess <= num_abs:
        guess += increment
        count +=1
      print('\nO número de tentativas é de', count)
      if abs(guess**raiz - num_abs) >= epsilon:
        print('\nFalhou o cálculo da raiz de índice', raiz, 'de', num)
      else:
        # se o input for um número negativo
        if num < 0:
          guess = -guess
        print(guess, 'é suficientemente próximo da raiz de índice', raiz, 'de', num)
    else:
      ''' se o input for entre 1 e 0 entao o guess é um, desincrementa-se o epsilon até achar o valor aproximado e verifica-se o guess para quando deixar de ser maior ou igual ao módulo do número do user terminar o loop - para não dar um loop infinito'''
      guess = 1.0
      while abs(guess**raiz - num_abs) >= epsilon and guess >= num_abs:
        guess -= increment
      print('\nO número de tentativas corresponde a', count)
      if abs(guess**raiz - num_abs) >= epsilon:
        print('\nFalhou o cálculo da raiz de indice', raiz, 'de', num)
      else:
        # se o input for um número negativo
        if num < 0:
          guess = -guess
        print(guess, 'é suficientemente próximo da raiz de indice', raiz, 'de', num)

  # Algoritmo B

  elif algo == 'b' or algo == 'B':
    low = 0
    high = num_abs
    guess = (high + low) / 2.0
    # se o input for maior que um ou negativo
    if num >= 1 or num <= -1:
      while abs(guess**raiz - num_abs) >= epsilon:
        if guess**raiz < num_abs:
          low = guess
        else:
          high = guess
        guess = (high + low) / 2.0
        count +=1
      # se o input for um número negativo
      if num < 0:
        guess = -guess
      print('\nO número de tentativas corresponde a', count)
      print(guess, 'é suficientemente próximo da raiz de índice', raiz, 'de', num)
    else:
      # se o input for entre 1 e 0 entao o maior valor terá de ser 1
      high = 1
      while abs(guess**raiz - num_abs) >= epsilon:
        if guess**raiz < num_abs:
          low = guess
        else:
          high = guess
        guess = (high + low) / 2.0
        count += 1
      # se o input for um número negativo
      if num < 0:
        guess = -guess
      print('\nO número de tentativas corresponde a', count)
      print(guess, 'é suficientemente próximo da raiz de índice', raiz, 'de', num)
