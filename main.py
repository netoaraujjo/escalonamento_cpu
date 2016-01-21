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

def converte_entrada(entrada):
    entrada = entrada.replace("\n", "")
    entrada = entrada.split(" ")
    entrada = map(int, entrada)
    entrada = tuple(entrada)
    return entrada

def main():
    entrada = sys.stdin.readlines()
    processos = map(converte_entrada, entrada)

    fcfs = FCFS()
    fcfs_result = fcfs.execute(processos)

    sjf = SJF()
    sjf_result = sjf.execute(processos)

    rr = RR()
    rr_result = rr.execute(processos, 2)

    saida = "FCFS {0} {1} {2}\nSJF {3} {4} {5}"

    print(processos)

    print(rr_result)

    print(saida.format(
            fcfs_result[0], fcfs_result[1], fcfs_result[2],
            sjf_result[0], sjf_result[1], sjf_result[2]))

if __name__ == '__main__':
    main()
