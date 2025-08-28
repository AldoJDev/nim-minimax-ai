# Jogo Nim com Inteligência Artificial (Poda Alpha-Beta)

Este repositório contém a implementação do clássico jogo de estratégia Nim. O projeto coloca um jogador humano contra uma Inteligência Artificial (IA) que utiliza o algoritmo Minimax otimizado com a Poda Alpha-Beta para determinar a jogada ideal.

## 📜 Visão Geral

O objetivo deste projeto foi aplicar um algoritmo de busca competitiva, a Poda Alpha-Beta, para desenvolver uma IA capaz de jogar o jogo Nim de forma eficiente. O jogo é configurado na sua variante *misère*, onde o objetivo é forçar o oponente a pegar o último objeto.

A IA assume que o oponente sempre fará a melhor jogada possível. A otimização com Poda Alpha-Beta permite que a árvore de decisões seja analisada de forma muito mais rápida, descartando ramos que não influenciarão no resultado final.

## ✨ Recursos

*   **Implementação Clássica do Nim**: Jogo configurado com as pilhas iniciais de 1, 3, 5 e 7 contadores.
*   **Variante *Misère***: O jogador que remove o último contador perde o jogo.
*   **Inteligência Artificial Robusta**: A IA utiliza o algoritmo Minimax com Poda Alpha-Beta para garantir jogadas ótimas.
*   **Modo de Jogo**: Jogador vs. IA.
*   **Interface de Linha de Comando**: Interação simples e direta através do terminal.

## Regras do Jogo (Variante Misère)

1.  O jogo é organizado em quatro pilhas com 1, 3, 5 e 7 contadores.
2.  Dois jogadores (Humano e IA) realizam jogadas alternadamente.
3.  Em cada jogada, o jogador deve remover um ou mais contadores de **uma única pilha**. É permitido remover todos os contadores de uma pilha, se desejado.
4.  O jogador que for forçado a remover o último contador de todas as pilhas **perde** o jogo.

## 💻 Tecnologias e Algoritmos

*   **Linguagem de Programação**: Python
*   **Algoritmo de IA**: O núcleo da lógica da IA é o **Minimax**, um algoritmo recursivo ideal para jogos de dois jogadores com soma zero.
*   **Otimização**: Foi implementada a **Poda Alpha-Beta** para otimizar o Minimax, reduzindo drasticamente o número de nós na árvore de busca que precisam ser avaliados para tomar uma decisão.

## 📊 Análise de Desempenho

Testes foram realizados para comparar a eficiência do algoritmo Minimax puro com a versão otimizada com Poda Alpha-Beta. Os resultados demonstram uma redução significativa no tempo de processamento por jogada.

| Algoritmo Implementado      | Oponente      | Tempo Médio por Jogada (s) |
| :-------------------------- | :------------ | :------------------------- |
| Minimax (puro)              | IA vs. IA     | 0.660s                     |
| Minimax + Poda Alpha-Beta   | IA vs. IA     | **0.048s**                 |
| Minimax + Poda Alpha-Beta   | IA vs. Humano | **0.055s**                 |

A utilização da Poda Alpha-Beta resultou em uma execução aproximadamente **13 vezes mais rápida**, tornando a IA mais ágil e eficiente sem comprometer a qualidade de suas decisões.

## 📚 Referências

*   **Vídeo Explicativo**: [Algorithms Explained – minimax and alpha-beta pruning](https://www.youtube.com/watch?v=l-hh51ncgDI)
*   **Artigo sobre Nim e Minimax**: [Minimax in Python: Learn How to Lose the Game of Nim](https://realpython.com/python-minimax-nim/)
*   **Documentação**: [W3Schools - Python sorted()](https://www.w3schools.com/python/ref_func_sorted.asp), [W3Schools - Python Lambda](https://www.w3schools.com/python/python_lambda.asp)
*   **Conceito Teórico**: [Wikipedia - Alpha–beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)
