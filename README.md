Algoritmos de escalonamento de CPU
==

Algoritmos implementados:

* First Come, First Serve (FCFS)
* Smallest Job First (SJF)
* Round Robin (RR)


Métricas avaliadas:

* Tempo de retorno médio: Refere-se ao tempo transcorrido entre o momento da entrada do processo no sistema e o seu término.
* Tempo de resposta médio: Intervalo de tempo entre a chegada do processo e o início de sua execução.
* Tempo de espera médio: Soma dos períodos em que um processo estava no seu estado pronto.

Formato do arquivo de entrada:

<pre>
  <code>
  0 20
  0 10
  4 6
  4 8
  </code>
</pre>

A entrada é composta por uma série de pares de números inteiros separados por um espaço em branco indicando o instante de chegada do processo e a duração de cada processo.


Formato do arquivo de saída:

<pre>
  <code>
  FCFS 30,5 19,5 19,5
  SJF 21,5 10,5 10,5
  RR 32 3,0 21
  </code>
</pre>


A saída é composta por linhas contendo a sigla de cada um dos três algoritmos e os valores das três métricas solicitadas. Cada linha apresenta a sigla do algoritmo e os valores médios (com uma casa decimal) para tempo de retorno, tempo de resposta e tempo de espera, exatamente nesta ordem, separados por um espaço em branco.
