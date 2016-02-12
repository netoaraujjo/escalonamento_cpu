#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy

class SJF:
    """Algoritmo de escalonamento Smallest Job First (SJF)"""

    def execute(self, processos):
        """
        Executa o algoritmo. Recebe como parametros a lista de processos a
        serem executados.
        """

        # Cria uma copia da lista de processos
        procs = copy.deepcopy(processos)

        tempo_retorno_total = 0 # Inicializa o tempo de retorno total
        tempo_resposta_total = 0 # Inicializa o tempo de resposta total
        tempo_espera_total = 0 # Inicializa o tempo de espera total

        # Armazena o instante de chegada do primeiro processo
        tempo_inicio = processos[0][0]

        # Inicializa o tempo atual com o instante de chegada do primeiro processo
        tempo_atual = tempo_inicio

        # Armazena a soma das durações do processos
        soma_duracao = 0

        while procs:
            # busca o proximo processo a ser executado
            proximo = self.__next_process(procs, tempo_atual)

            if proximo == -1: # ocorrencia de vacuo. nao ha processo com tempo de chegada <= ao tempo atual
                tempo_atual = procs[0] # atualiza o tempo atual para o tempo de chegada do proximo processo na lista
            else:
                # O tempo de resposta e o tempo de espera coincidem
                # E a duracao do processo anterior menos a diferenca entre o tempo
                # de chegada do processo atual e o tempo de inicio da execucao
                # do primeiro processo
                tempo_resposta_total += soma_duracao - (procs[proximo][0] - tempo_inicio)
                tempo_espera_total += soma_duracao - (procs[proximo][0] - tempo_inicio)

                # Acumula a duracao de cada processo
                soma_duracao += procs[proximo][1]

                # Tempo total ate o fim do processo menos a diferenca entre o tempo de
                # chegado do processo atual e o tempo inicial
                tempo_retorno_total += soma_duracao - (procs[proximo][0] - tempo_inicio)


                # adiciona a duracao do processo escolhido, atualizando o tempo atual
                tempo_atual = tempo_atual + procs[proximo][1]
                procs.pop(proximo)

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


    # Metodo que busca o proximo processo a ser executado
    def __next_process(self, procs, ta):
        """
        Busca o proximo indice a ser executado. Recebe como parametros a lista de processos
        e o tempo atual
        """

        menor_duracao = None
        index_melhor = -1

        for index, p in enumerate(procs):
            if p[0] <= ta:   # se no instante atual o processo ja entrou no sistema
                if menor_duracao is None: # se for o primeiro processo com tempo <= tempo_atual
                    menor_duracao = p[1]
                    index_melhor = index
                else:
                    # se o tempo de duracao for menor que o tempo do melhor ate o momento, o melhor e atualizado
                    if p[1] < menor_duracao:
                        menor_duracao = p[1]
                        index_melhor = index
                    # caso de empate
                    # se o tempo de duracao e igual ao melhor ate o momento, verifica o instante de chegada
                    # o que chegou primeiro e escolhido
                    elif p[1] == menor_duracao:
                        if p[0] < procs[index_melhor][0]:
                            index_melhor = index
                            menor_duracao = p[1] # talvez desnecessario

        # Retorna o indice do proximo processo a ser executado
        return index_melhor
