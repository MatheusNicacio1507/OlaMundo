#input é uma função que permite perguntar algo ao usuário
#nome = input("Qual é o seu nome?")
'''
Bloco 
De
Comentário
Permite que você escreva várias linhas
'''
#print("Olá,", nome, ". Tudo bem com você")

#print(type(nome))

a = 10
b = 5.8
c = "Rio de Janeiro"
d = True

print("a:",a)
print("b:",b)
print("c:",c)
print("d:",d)

print("Tipo da var a:",type(a)) #Tipo inteiro (números inteiros)
print("Tipo da var b:",type(b)) #Tipo float (números reais)
print("Tipo da var c:",type(c)) #Tipo string  (alfanumérico)
print("Tipo da var d:",type(d)) #Tipo boolean (True ou False com iniciais maiúsculas)

a = 20
print("a:",a)

b = "São Paulo"
print("b:",b)

print("Tipo da var a:",type(a))
print("Tipo da var b:",type(b))

a = input("Informe um número")
b = input("Informe outro número")
print("a:",a,"- b:",b)
print("Tipo da var a:",type(a))
print("Tipo da var a:",type(b))

c = a + b #Concatenou as strings de a com b (juntou repetindo)
print("c:", c)
print("Tipo da var de c", type(c))

d = int(a)
print("d:",d)
print("Tipo da var d:",type(d))

a = int(input("Informe um número:"))
b = int(input("Informe outro número:"))
print("a:",a,"- b:",b)
print("Tipo da var a:",type(a))
print("Tipo da var a:",type(b))

c = a + b
print("c:", c)
print("Tipo da var de c", type(c))

a = float(input("Informe um número:"))
b = float(input("Informe outro número:"))
print("a:",a,"- b:",b)
print("Tipo da var a:",type(a))
print("Tipo da var a:",type(b))

c = a + b
print("c:", c)
print("Tipo da var de c", type(c))