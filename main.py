#print("hello world")
#print(3+4)
#print("hello" + " " + "world")
#print(input("Enter your name:"))
#print("Hello, " + input("Enter your name: ")+"!")

#Exercício 01
##Crie um programa que o usuário digita o seu nome e retorna o número de caracteres:

#print(len(input("Digite seu nome: ")))

#Exercício 02
##Criar um programa onde o usuário digita dois valores e apareça a soma:

#print(int(input("Digite um valor: ")) + int(input("Digite o segundo valor: ")))

#Exercírio 03
##Refatore o exercício 02 atribuindo variáveis

#print(int(input("Digite um valor: ")) + int(input("Digite o segundo valor: ")))

nome = str(input("Digite seu nome: "))
quantidade_de_caracteres = len(nome)
print(quantidade_de_caracteres)