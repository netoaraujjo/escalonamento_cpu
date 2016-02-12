#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from fcfs import *
from sjf import *
from rr import *

# Tempo de retorno médio – Refere-se ao tempo transcorrido entre o momento da
# entrada do processo no sistema e o seu término.
#
# Tempo de resposta médio – Intervalo de tempo entre a chegada do processo e o
# início de sua execução.
#
# Tempo de espera médio – Soma dos períodos em que um processo estava no seu
# estado pronto.

# converte a entrada para uma lista de tuplas
def converte_entrada(entrada):
    entrada = entrada.replace("\n", "")
    entrada = entrada.split(" ")
    entrada = map(int, entrada)
    entrada = tuple(entrada)
    return entrada

def main():
    # le o arquivo de entrada
    entrada = sys.stdin.readlines()
    processos = map(converte_entrada, entrada)

    # executa os algoritmos
    fcfs = FCFS()
    fcfs_result = fcfs.execute(processos)

    sjf = SJF()
    sjf_result = sjf.execute(processos)

    rr = RR()
    rr_result = rr.execute(processos, 2)

    # formata as saidas
    saida_fcfs = "FCFS {0} {1} {2}"
    saida_fcfs = saida_fcfs.format(fcfs_result[0], fcfs_result[1], fcfs_result[2])

    saida_sjf = "SJF {0} {1} {2}"
    saida_sjf = saida_sjf.format(sjf_result[0], sjf_result[1], sjf_result[2])

    saida_rr = "RR {0} {1} {2}"
    saida_rr = saida_rr.format(rr_result[0], rr_result[1], rr_result[2])

    saida = "{0}\n{1}\n{2}"

    # imprime a saida
    print(saida.format(saida_fcfs, saida_sjf, saida_rr))

if __name__ == '__main__':
    main()
