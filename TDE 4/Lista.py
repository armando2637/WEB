'''1. Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo
teclado(entre 0 e 20) e mostrá-la por extenso.'''

numeros=("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","catorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte")
n=int(input("Digite um número entre 0 e 20: "))
if 0<=n<=20: print(f"Você digitou {numeros[n]}")
else: print(f"Número fora do intervalo!")


'''2. Faça um programa que preencha por leitura uma lista de 10 posições, e conta
quantos valores diferentes existem na lista.'''

lista=[]
for i in range(10): lista.append(int(input(f"Digite o {i+1}º valor: ")))
print(f"Existem {len(set(lista))} valores diferentes na lista.")


'''3.Crie um programa que leia quatro valores pelo teclado e guarde-os em uma lista.
No final mostre:
a)Quantas vezes apareceu o valor 9.
b)Em que posição foi digitado o primeiro valor 3.
c)Quais foram os números pares.'''

valores=[int(input(f"Digite o {i+1}º valor: ")) for i in range(4)]
print(f"O valor 9 apareceu {valores.count(9)} vezes.")
print(f"O primeiro 3 foi digitado na posição {valores.index(3)}" if 3 in valores else f"O valor 3 não foi digitado.")
print(f"Números pares: {[v for v in valores if v%2==0]}")


'''4. Um dado é lançado 50 vezes, e o valor correspondente é armazenado em uma
lista. Faça um programa que determine o percentual de ocorrências de face 6 do
dado dentre esses 50 lançamentos.'''

import random
lancamentos=[random.randint(1,6) for _ in range(50)]
print(f"O número 6 apareceu {(lancamentos.count(6)/50*100):.2f}% das vezes.")


'''5. Tradutor Simples:
Desenvolva um programa que atue como um tradutor simples entre duas línguas. O
programa deve usar um dicionário onde as chaves são palavras em uma língua e os
valores são suas traduções em outra língua. O usuário deve poder fornecer uma
palavra como entrada e obter sua tradução como saída.'''

dicionario={"casa":"house","gato":"cat","cachorro":"dog","livro":"book"}
palavra=input("Digite uma palavra em português: ").lower()
print(f"Tradução: {dicionario.get(palavra,'Não encontrada no dicionário')}")


'''6. Estoque de Produtos
Implemente um sistema simples de controle de estoque de produtos. O programa
deve permitir ao usuário adicionar novos produtos ao estoque, atualizar a
quantidade de produtos existentes e exibir o estoque atualizado. Use um dicionário
onde as chaves são os nomes dos produtos e os valores são as quantidades
disponíveis.'''

estoque={}
while True:
    print(f"\n1 - Adicionar produto\n2 - Atualizar quantidade\n3 - Exibir estoque\n4 - Sair")
    opcao=input("Escolha: ")
    if opcao=="1": produto=input("Nome do produto: "); qtd=int(input("Quantidade: ")); estoque[produto]=estoque.get(produto,0)+qtd
    elif opcao=="2": produto=input("Produto para atualizar: "); print(f"Produto não encontrado!") if produto not in estoque else estoque.update({produto:int(input('Nova quantidade: '))})
    elif opcao=="3": print(f"Estoque: {estoque}")
    elif opcao=="4": break


'''7. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a
ordem lida.'''

idades=[int(input("Digite a idade: ")) for _ in range(5)]
alturas=[float(input("Digite a altura: ")) for _ in range(5)]
print(f"\nIdade e altura na ordem inversa:")
for i in range(4,-1,-1): print(f"Idade: {idades[i]}, Altura: {alturas[i]}")


'''8. Frequência de Letras:
Crie um programa que receba uma string como entrada e conte o número de
ocorrências de cada letra do alfabeto (ignorando maiúsculas/minúsculas). O
programa deve imprimir um dicionário onde as chaves são as letras do alfabeto e os
valores são o número de vezes que cada letra ocorre na string.'''

texto=input("Digite uma string: ").lower()
freq={}
for letra in texto:
    if letra.isalpha(): freq[letra]=freq.get(letra,0)+1
print(f"{freq}")


'''9. Média de Notas: Escreva uma função em Python que receba um dicionário contendo nomes de
alunos e suas respectivas notas em uma disciplina. A função deve calcular a média
das notas de todos os alunos e retornar um dicionário onde a chave é "média" e o
valor é a média calculada.'''

def media_notas(d): return {"média":sum(d.values())/len(d)}
alunos={"Ana":8.5,"Pedro":7.0,"Maria":9.0}
print(f"{media_notas(alunos)}")


'''10. Contagem de Palavras:
Escreva um programa em Python que receba uma string como entrada e conte o
número de ocorrências de cada palavra na string. O programa deve imprimir um
dicionário onde as chaves são as palavras e os valores são o número de vezes que
cada palavra ocorre na string.'''

texto=input("Digite uma frase: ").lower().split()
contagem={}
for p in texto: contagem[p]=contagem.get(p,0)+1
print(f"{contagem}")


'''11. Escreva uma função que recebe um número n como parâmetro e imprime se n é
positivo ou negativo.'''

def verifica_numero(n): print(f"Número positivo") if n>=0 else print(f"Número negativo")
verifica_numero(int(input("Digite um número: ")))


'''12. Escreva uma função para imprimir o valor absoluto de um número.'''

def valor_absoluto(n): return abs(n)
print(f"{valor_absoluto(-10)}")


'''13. Escreva uma função que recebe dois números (a e b) como parâmetro e retorne
True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.'''

def verifica_soma(a,b,limite): return (a+b)>limite
print(f"{verifica_soma(5,7,10)}")


'''14. Faça um programa com uma função chamada somaImposto. A função possui
dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas
expressa em porcentagem e custo, que é o custo de um item antes do imposto. A
função “altera” o valor de custo para incluir o imposto sobre vendas.'''

def somaImposto(taxa,custo): return custo+(custo*taxa/100)
print(f"{somaImposto(10,100)}")


'''15. Faça uma função que informe a quantidade de dígitos de um determinado
número inteiro informado.'''

def qtd_digitos(n): return len(str(abs(n)))
print(f"{qtd_digitos(12345)}")
