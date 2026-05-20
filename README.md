# Heavy Cycle Edges - Minimum Spanning Tree (MST)

## 📌 Descrição do Problema

Este projeto resolve um problema clássico de Teoria dos Grafos voltado para a identificação de arestas críticas em ciclos. Dado um grafo não direcionado com pesos nas arestas, o objetivo é encontrar e imprimir os pesos de todas as arestas que configuram a aresta mais pesada de algum ciclo presente no grafo. Caso não exista nenhum ciclo, o programa identifica a estrutura como uma **floresta**.

## 🏗️ Modelagem do Grafo

- **Vértices:** identificados por inteiros de `0` a `n-1`.
- **Arestas:** conexões bidirecionais ponderadas.
- É garantido que não existem pesos duplicados ou arestas paralelas.

## 🚀 Estratégia de Solução

A solução utiliza o **Algoritmo de Kruskal** amparado pela estrutura de dados **Disjoint Set Union (DSU / Union-Find)**.

Pela propriedade dos ciclos na Árvore Geradora Mínima (MST), a aresta de maior peso em qualquer ciclo é exatamente a aresta que *não* pertence à MST.

### Passos do algoritmo

1. Ordenar todas as arestas em ordem crescente de peso.
2. Iterar sobre as arestas ordenadas utilizando DSU para tentar unir os vértices.
3. Se os vértices de uma aresta já pertencem ao mesmo conjunto no DSU, adicioná-la criaria um ciclo. Como a análise é feita em ordem crescente, essa aresta é garantidamente a mais pesada deste ciclo.
4. Registrar o peso dessa aresta.
5. Ao final, se nenhuma aresta foi rejeitada, o grafo não possui ciclos e o programa retorna `forest`. Caso contrário, os pesos são impressos em ordem crescente.

## 💻 Estrutura de Dados (DSU)

O `Union-Find` é implementado com as heurísticas de **Path Compression** (compressão de caminho) e **Union by Rank** (união por classificação), garantindo que as operações de busca e união operem em tempo praticamente constante, `O(α(V))`. Isso permite que o algoritmo tenha complexidade dominada pela ordenação das arestas, `O(E log E)`.

## 🧠 Observação

A abordagem evita busca exaustiva por ciclos, tornando o algoritmo eficiente mesmo para grafos grandes.
