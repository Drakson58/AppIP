# AppIP
Trabalho da disciplicada de Sistema Operacionais de Redes 1. Objetivo do trabalho é fazer um programa que busque informações sobre um ip.

Front-end:

0 - Através do módulo Tkinter foi criada uma janela para organizar os widgets da interface da atividade.
0.1 - A interface foi elaborada para gerar a interação do componente de entrada de dados do usuário com a caixa de texto.
 	0.2 - Dependendo do que o usuário inserir na aplicação,ele receberá uma resposta que estará visível na caixa de texto, ou se inserir “sair”,a aplicação vai ser encerrar juntamente com sua conexão com o servidor.

1-A função click() determina a funcionalidade do botão “enviar” presente na interface,que quando apertado manda os dados da interface para um arquivo ,logo poderá ser acessado pelo um socket do cliente.

1.1 - Cria-se um objeto “cl” da classe cliente,onde sua classe possui um método que inicializa o socket do cliente para estabelecer conexão com o socket do servidor.

1.2 -Quando esse método é chamado na função “click()” uma variável chamada ‘tipo’ recebe o valor retornado por esse método,que poderá ser uma mensagem que irá informar erro ou dizer o tipo do Ip.

1.3 Se a variável tipo == ‘sair’ a interface encerrará sua execução.


back-end:

	O valor é recebido pelo cliente e descodificado para poder prosseguir com as manipulações.
	
	0 - Verifica a mensagem recebida pelo o cliente.
		0.1 - Caso seja igual a ‘sair’ a conexão é fechada.
		0.2 - Se for diferente de ‘sair’ passa pelo if e são feitas as manipulações.

	1 - É verificado usando orientação ao objeto se o dado recebido é um ip (módulo validaMsg.py).
		1.1 - É criada uma lista que vai receber os valores de cada octeto (_msgSeparada ).
		1.2 - Na função validaPontos( )  foi usada expressão “.count(‘.’)” para verificar se a msg tem 3 pontos.
		1.3.1 - Na função validaCampos( ) foi usado o “.split(‘.’)” para retornar uma lista somente com os valores de cada octeto; Ex: 10.0.0.1 => campos = [‘10’, ‘0’, ’0’, ’1’]. 
		1.3.2 - Foi usado um for e a função .isdigit( ) para verifica se o valor de cada octeto é número e caso seja, será adicionado na lista => _msgSeparada.
1.3.3 - Logo depois é usada a função len(str()) e um for para verificar se o tamanho de cada octeto não ultrapassa o valor 3.
1.3.4 - Foi usada uma operação matemática para verificar se a divisão de cada octeto não ultrapassa o valor de 127.5, pois um octeto inválido com o valor de 256 dividido por 2 é igual a 128. 

2 - É verificado a classe que o IP pertence (módulo classeIp.py).
	1.1 - Na função classeTipo( ) foram feitas as devidas comparações e retornado os devidos valores de cada classe.

	3 - Depois de toda a manipulação  a lista que recebeu o IP é limpada (linha +- 53) para poder receber os novos valores.
		3.1 - É mandado para o cliente o resultado codificado da manipulação.

Complicações:
	O fato de o servidor necessitar de ser executado ao mesmo tempo que a interface para executar a integração do front-end com o back-end impedia a continuação do código, pois eles são executados em loop,então a compilação de um impedia a do outro,portanto foi necessário a execução paralela do servidor através de uma thread.

