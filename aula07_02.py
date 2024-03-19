# -*- coding: utf-8 -*-
"""Aula07/02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Znv3XO-mbi9myYHhOzQx9Oqu9tNeUstd

# **Aula 2 - Operadores**

## Atividade 1
"""

x = 4
x1 = 5
x2 = 9

x_result1 = ((( 2 + 5 ) * 3 ) + x + 5) < x1
x_result2 = ((( 2 + 5 ) * 3 ) + (x + 5 + x1)) == (x == 6 + x2 * 2)
x_result3 = ((( 3 * 6 ) + x - 3 ) < x2)
x_result4 = ((( 7 * 8 ) > (x + 4 - x1) < (x * 2 + x2 * 9)))

print(f'Resultado 1: {x_result1}')
print(f'Resultado 2: {x_result2}')
print(f'Resultado 3: {x_result3}')
print(f'Resultado 4: {x_result4}')

"""## Atividade 2"""

n = int(input('Digite um número: '))

condicao1 = 20 < n < 30
condicao2 = not condicao1

print(f'O número está entre 20 e 30? {condicao1}')
print(f'O número está fora de 20 e 30? {condicao2}')

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))

condicao1 = (a > 10) and (b <= 5)
condicao2 = not ((a >= 10) or (b < 5))

print(f'A primeira expressão é: {condicao1}')
print(f'A segunda expressão é: {condicao2}')



"""# **Aula 2 - Estruturas condicionais**

## Atividade 1

### Pseudocódigo

```
var

nota1, nota2, media: real

inicio

escreva('Digite a primeira nota:')
leia(nota1)

escreva('Digite a primeira nota:')
leia(nota2)

media <- (nota1 + nota2) / 2

se(media >= 7) entao:
  escreva('O aluno está aprovado.')
senao:
  escreva('O aluno está reprovado.')
fim_se

fim
  
```
"""

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
  print(f'O aluno está aprovado com média {media} .')
else:
  print(f'O aluno está reprovado com média {media} .')