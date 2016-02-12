#!/usr/bin/env python
# -*- coding: utf-8 -*-

class FCFS:
    """Algoritmo de escalonamento First Come, First Serve (FCFS)"""

    def execute(self, processos):
        """
        Executa o algoritmo. Recebe como parametros a lista de processos a
        serem executados.
        """
        tempo_retorno_total = 0  # Inicializa o tempo de retorno total
        tempo_resposta_total = 0 # Inicializa o tempo de resposta total
        tempo_espera_total = 0   # Inicializa o tempo de espera total

        # Armazena o instante de chegada do primeiro processo
        tempo_inicio = processos[0][0]

        # Armazena a soma das durações do processos
        soma_duracao = 0

        for n, processo in enumerate(processos):
            # O primeiro processo possui tempo de resposta e tempo de espera zero
            if n != 0:
                # O tempo de resposta e o tempo de espera coincidem
                # E a duracao do processo anterior menos a diferenca entre o tempo
                # de chegada do processo atual e o tempo de inicio da execucao
                # do primeiro processo
                tempo_resposta_total += soma_duracao - (processo[0] - tempo_inicio)
                tempo_espera_total += soma_duracao - (processo[0] - tempo_inicio)

            # Acumula a duracao de cada processo
            soma_duracao += processo[1]

            # Tempo total ate o fim do processo menos a diferenca entre o tempo de
            # chegado do processo atual e o tempo inicial
            tempo_retorno_total += soma_duracao - (processo[0] - tempo_inicio)

        # Calcula o tempo de retorno medio
        tempo_retorno_medio = float(tempo_retorno_total) / len(processos)

        # Calcula o tempo de resposta medio
        tempo_resposta_medio = float(tempo_resposta_total) / len(processos)

        # Calcula o tempo de espera medio
        tempo_espera_medio = float(tempo_espera_total) / len(processos)

        # converte para string, substitui ponto por virgula, com uma casa decimal
        tempo_retorno_medio = ("%.1f" % tempo_retorno_medio).replace('.', ',')
        tempo_resposta_medio = ("%.1f" % tempo_resposta_medio).replace('.', ',')
        tempo_espera_medio = ("%.1f" % tempo_espera_medio).replace('.', ',')

        # Retorna uma tupla contendo o tempo de retorno medio, o tempo de
        # resposta medio e o tempo de espera medio, respectivamente
        return (tempo_retorno_medio, tempo_resposta_medio, tempo_espera_medio)
