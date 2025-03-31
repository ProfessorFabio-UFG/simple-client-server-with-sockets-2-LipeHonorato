from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-
(conn, addr) = s.accept()  # returns new socket and addr. client 

while True:                # forever
  data = conn.recv(1024)   # receive data from client
  if not data: break       # stop if client stopped

  #decodifica os dados
  calculo = bytes.decode(data)

  #separa os valores que tem um espaço entre si em um vetor
  valores = calculo.split(" ")

  #pegar os valores da conta
  valor1 = int(valores[0])
  valor2 = int(valores[1])
  op = valores[2] # operacao sum, sub, div

  # checando a operacao correta
  if (op == 'sum'):
    res = valor1 + valor2
  elif (op == 'sub'):
    res = valor1 - valor2
  elif (op == 'div'):
    if (valor2 == 0):
      res = 'error division by zero'
    else:
      res = valor1/valor2
  else:
    res = 'error'

  
  conn.send(str.encode(str(res))) # return sent data


conn.close()               # close the connection
