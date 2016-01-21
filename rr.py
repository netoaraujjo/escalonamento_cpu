#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy

class RR:
    """Algoritmo de escalonamento Round Robin (RR)"""

    def execute(self, processos, quantum):
        """
        Executa o algoritmo. Recebe como parametros a lista de processos a
        serem executados e a duracao do quantum.
        """

        # Cria uma copia da lista de processos
        procs = map(list, copy.deepcopy(processos))

        tempo_retorno_total = 0  # Inicializa o tempo de retorno total
        tempo_resposta_total = 0 # Inicializa o tempo de resposta total
        tempo_espera_total = 0   # Inicializa o tempo de espera total

        # Armazena o instante de chegada do primeiro processo
        tempo_inicio = processos[0][0]

        # Inicializa o tempo atual com o instante de chegada do primeiro processo
        tempo_atual = tempo_inicio

        # Armazena a soma das durações do processos
        soma_duracao = 0

        # numero total de processos
        num_processos = len(processos)

        while procs:

            # seleciona o proximo processo a ser executado
            while True:
                # busca o processo que chegou ao sistema no tempo atual
                if procs[0][0] < tempo_atual or procs[0][0] == tempo_inicio:
                    break
                else:
                    # envia o processo para o fim da fila
                    p = procs[0]
                    procs.pop(0)
                    procs.append(p)

            # Verifica se e a primeira execucao
            if -1 not in procs[0]:
                procs[0].append(-1) # indica que o processo ja foi executado uma vez
                tempo_resposta_total += tempo_atual - procs[0][0] # acumula valor para calculo do tempo de resposta medio

            # verifica se e a ultima execucao do processo
            if procs[0][1] <= quantum:
                tempo_atual += procs[0][1] # soma o tempo da ultima execucao do processo para ao tempo atual
                tempo_retorno_total += tempo_atual - procs[0][0] # acumula o tempo de retorno no total

                # atualiza o tempo de espera total para todos os processos, exceto o ultimo a executar
                for index, proc in enumerate(procs):
                    if index != 0 and proc[0] < tempo_atual:
                        if tempo_atual - proc[0] >= quantum:
                            tempo_espera_total += quantum
                        else:
                            tempo_espera_total += tempo_atual - proc[0]

                procs.pop(0) # remove o processo da lista

            else:
                procs[0][1] -= quantum # reduz um quantum da duracao do processo

                tempo_atual += quantum # atualiza o tempo atual

                # atualiza o tempo de espera total para todos os processos, exceto o ultimo a executar
                for index, proc in enumerate(procs):
                    if index != 0 and proc[0] < tempo_atual:
                        if tempo_atual - proc[0] >= quantum:
                            tempo_espera_total += quantum
                        else:
                            tempo_espera_total += tempo_atual - proc[0]

                # envia o processo para o fim da lista
                p = procs[0]
                procs.pop(0)
                procs.append(p)


        # Calcula o tempo de retorno medio
        tempo_retorno_medio = float(tempo_retorno_total) / num_processos

        # Calcula o tempo de resposta medio
        tempo_resposta_medio = float(tempo_resposta_total) / num_processos

        # Calcula o tempo de espera medio
        tempo_espera_medio = float(tempo_espera_total) / num_processos

        # Retorna uma tupla contendo o tempo de retorno medio, o tempo de
        # resposta medio e o tempo de espera medio, respectivamente
        return (tempo_retorno_medio, tempo_resposta_medio, tempo_espera_medio)
