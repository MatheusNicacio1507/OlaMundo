'''
Elabore um programa que pergunta ao aluno suas 3 notas escolares.
O programa deverá calcular a média das 3 notas inseridas e
exibir esta média.
'''

'''
#Meu programa abaixo, sem correções

print("Informe suas 3 notas escolares:")

nota1 = int(input("Informe sua nota:"))
nota2 = int(input("Informe sua nota:"))
nota3 = int(input("Informe sua nota:"))

media = nota1 + nota2 + nota3
media = media/3

print("Sua média é:", media)

print("Parabéns!")
'''

#Programa do Professor:

#Etapa 1: entrada de dados
nota1 = float(input("Informe sua nota 1:"))
nota2 = float(input("Informe sua nota 2:"))
nota3 = float(input("Informe sua nota 3:"))

#Etapa 2: processamento de dados
media = (nota1 + nota2 + nota3) / 3

#Etapa 3: saída de dados (resposta na tela do usuário)
print("Sua média é", media)