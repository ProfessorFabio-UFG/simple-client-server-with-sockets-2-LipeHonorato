# Descrição do Sistema
Esse programa possui uma aplicação cliente e uma servidor que podem comunicar entre si, para isso, execute a aplicação do servidor e a aplicação do cliente 
em sequência.

## Aplicação Servidor (server.py)
Para compilar e excecutar o programa use o seguinte comando no terminal: `python3 server.py`.

Depois de executar o servidor, o cliente não interage diretamente com ele pelo terminal, mas sim pela aplicação cliente. Depois de receber o cálculo da 
aplicação cliente, o servidor separa os valores e a operação em um vetor, verifica qual é a operação escolhida e calcula o resultado. Em seguida o resultado 
é enviado para a aplicação cliente e a conexão é encerrada.

## Aplicação Cliente (client.py)
Para compilar e excecutar o programa use o seguinte comando no terminal: `python3 client.py`.

Após isso, será imprimido na tela instruções para usar o programa. O cliente então deverá inserir os 2 valores e a operação desejada para o cálculo, depois
de inserir, será imprimido na tela o cálculo desejado no formato `'valor1' 'operação' 'valor2'`. O cálculo será enviado para o servidor, após o servidor 
calcular o resultado, ele é imprimido na tela e o programa será encerrado.
