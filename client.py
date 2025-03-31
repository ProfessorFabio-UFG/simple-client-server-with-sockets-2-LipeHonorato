from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)

#Imprime na tela para o client indicar o cálculo desejado
valor1 = input("Digite o valor 1: ")
valor2 = input("Digite o valor 2: ")
op =  input("Digite a operação (sum, sub ou div): ")

#tranforma o calculo em uma string
calculo = valor1 + " " + valor2 + " " + op
print(calculo)

s.send(str.encode(calculo))  # send some data
data = s.recv(1024)     # receive the response

print (bytes.decode(data))            # print the result

s.close()               # close the connection
