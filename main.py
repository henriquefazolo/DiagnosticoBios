'''

Elabore os códigos em Python dos problemas a seguir:
Um computador costuma apitar quando é ligado.
Tais apitos são apitos de diagnóstico, indicando se há algum problema ou não.
Se houver um problema, o apito é diferente. Para cada fabricante de BIOS,
há uma codificação diferente. Veja a tabela a seguir de um modelo:

AMI BIOS Tone POST Codes
Apito
Condição de Erro
1 curto
Atualização de DRAM
2 curtos
Circuito de Paridade
3 curtos
Memória Base 64K RAM
4 curtos
Timer do Sistema
5 curtos
Processador

(fonte: https://www.boadica.com.br/dica/165/entenda-os-bips-da-sua-bios)

Utilizando essa tabela, crie um programa que indique qual é o erro gerado para ajudar usuários. A entrada do programa é o número de apitos. De acordo com o número de apitos fornecido pelo usuário, mostre qual é o erro deste suposto computador.

'''

from random import randint


class Diagnostico:
    def __init__(self):
        self.apito = randint(1, 5)

    def ligar(self):
        """
        1 curto     Atualização de DRAM
        2 curtos    Circuito de Paridade
        3 curtos    Memória Base 64K RAM
        4 curtos    Timer do Sistema
        5 curtos    Processador

        :return: Retorna erro conforme a quantidade de curtos detectados ao ligar o dispositivo.
        """
        apito = self.apito
        if apito == 1:
            return 'Atualização de DRAM'
        elif apito == 2:
            return 'Circuito de Paridade'
        elif apito == 3:
            return 'Memória Base 64K RAM'
        elif apito == 4:
            return 'Timer do Sistema'
        elif apito == 5:
            return 'Processador'
        else:
            return 'Computador ligado com sucesso!'


pc = Diagnostico()
print(pc.ligar())

