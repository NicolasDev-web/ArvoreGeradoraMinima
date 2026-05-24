# Árvore Geradora Mínima - Heavy Cycle Edges

## 📋 Nome do Problema

**Heavy Cycle Edges** - UVA Online Judge Problem #10397

## 🔗 Link do Problema

[UVA 10397 - Heavy Cycle Edges](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2847)

## 👥 Integrantes do Grupo

Este projeto foi desenvolvido como parte de um trabalho acadêmico sobre Árvores Geradoras Mínimas (Minimum Spanning Trees - MST).

## 💻 Linguagem Utilizada

- **Java** (100%)

## 🚀 Como Executar a Solução

### Pré-requisitos
- Java JDK 8 ou superior instalado
- Compilador Java (`javac`)

### Compilação
```bash
cd src
javac *.java
```

### Execução
```bash
java Main
```

Ou para testar com um arquivo de entrada:
```bash
java Main < ../dados/entradas_do_problema.txt
```

### Formato de Entrada
```
n m
u1 v1 w1
u2 v2 w2
...
um vm wm
0 0
```

Onde:
- `n`: número de vértices
- `m`: número de arestas
- `u`, `v`: vértices da aresta
- `w`: peso da aresta
- Entrada termina quando `n = 0` e `m = 0`

### Exemplo de Entrada
```
3 3
0 1 1
1 2 2
2 0 3
4 5
0 1 1
1 2 2
2 3 3
3 1 4
0 2 0
0 0
```

### Saída Esperada
```
3
1 4
forest
```

## 📊 Explicação da Modelagem do Problema como Grafo Ponderado

O problema envolve um **grafo não-direcionado ponderado** com as seguintes características:

- **Vértices**: Representam pontos ou nós no grafo
- **Arestas**: Conexões entre vértices com pesos (custos)
- **Pesos**: Números inteiros positivos associados a cada aresta

A tarefa é identificar todas as arestas que **não pertencem a nenhuma Árvore Geradora Mínima (MST)** do grafo.

### Conceito Fundamental: Arestas Pesadas em Ciclos

Uma **aresta pesada de ciclo** (heavy cycle edge) é uma aresta que:
- Não faz parte de nenhuma MST do grafo
- Está envolvida em pelo menos um ciclo
- Tem peso maior que a aresta máxima do caminho na MST entre seus dois vértices

**Exemplo Visual:**
```
Ciclo: 0 -- 1 -- 2 -- 0
       w=1    w=2    w=3

MST inclui arestas com pesos 1 e 2
A aresta de peso 3 é uma "heavy cycle edge"
```

## 🎯 Algoritmo Utilizado

**Algoritmo de Kruskal com Modificação para Detecção de Arestas Pesadas**

### Passos do Algoritmo

1. **Ordenar arestas por peso** (crescente)
2. **Construir MST** usando Union-Find (Disjoint Set Union)
3. **Para cada aresta não incluída na MST:**
   - Encontrar o peso máximo no caminho entre seus vértices na MST
   - Se o peso da aresta é maior que esse máximo, ela é uma "heavy cycle edge"
4. **Imprimir** os pesos das arestas pesadas em ordem crescente

### Pseudocódigo
```
function kruskalModificado(n, edges):
    sort edges by weight
    uf = new UnionFind(n)
    mst_edges = []
    
    for each edge in edges:
        if not uf.connected(edge.u, edge.v):
            uf.union(edge.u, edge.v)
            mst_edges.add(edge)
        else:
            // Edge would create a cycle
            if edge.weight > max_weight_in_path(edge.u, edge.v, mst):
                heavy_edges.add(edge.weight)
    
    return sort(heavy_edges)
```

## 🔗 Papel do Union-Find/DSU (Disjoint Set Union)

O **Union-Find** é crucial neste projeto com múltiplos propósitos:

### 1. **Detecção de Ciclos**
- Determina se dois vértices já estão conectados na MST
- Se conectados, adicionar uma nova aresta criaria um ciclo

### 2. **Construção da MST**
- Mantém componentes conectadas disjuntas
- Garante que apenas arestas seguras sejam adicionadas

### 3. **Otimizações Implementadas**

#### Path Compression
```java
public int find(int p) {
    while (p != parent[p]) {
        parent[p] = parent[parent[p]];  // Compressão de caminho por redução
        p = parent[p];
    }
    return p;
}
```

#### Union by Rank
```java
public void union(int p, int q) {
    int rootP = find(p);
    int rootQ = find(q);
    
    if (rank[rootP] < rank[rootQ]) 
        parent[rootP] = rootQ;
    else if (rank[rootP] > rank[rootQ]) 
        parent[rootQ] = rootP;
    else {
        parent[rootQ] = rootP;
        rank[rootP]++;
    }
}
```

### Complexidade Amortizada
Com ambas as otimizações, as operações `find` e `union` têm complexidade praticamente **O(α(n))**, onde α é a função de Ackermann inversa (praticamente constante para valores práticos).

## 📈 Variação de MST Usada

Este projeto implementa uma **variação específica** do problema de MST:

### "Reverse MST" ou "MST Complement"
- Em vez de encontrar as arestas **que fazem parte** da MST
- Encontramos as arestas **que não fazem parte** de nenhuma MST
- Estas são exatamente as arestas que criariam ciclos com pesos maiores

### Características Especiais
- **Múltiplas MSTs possíveis**: Quando arestas têm pesos iguais, pode haver várias MSTs
- **Arestas que nunca entram**: Algumas arestas nunca farão parte de nenhuma MST
- **Propriedade do Ciclo**: Se uma aresta não pertence a nenhuma MST, ela é a aresta mais pesada em algum ciclo

## 🔧 Análise de Complexidade

### Complexidade Temporal

| Operação | Complexidade |
|----------|-------------|
| Ordenação de arestas | **O(m log m)** |
| Construção da MST (Union-Find) | **O(m · α(n))** ≈ **O(m)** |
| **Total** | **O(m log m)** |

Onde:
- `m` = número de arestas
- `n` = número de vértices
- `α(n)` = função de Ackermann inversa (praticamente constante)

### Complexidade Espacial

| Estrutura | Espaço |
|-----------|--------|
| Array de arestas | **O(m)** |
| Union-Find | **O(n)** |
| Fila de saída | **O(m)** no pior caso |
| **Total** | **O(m + n)** |

### Análise Detalhada

1. **Sorting**: O(m log m) domina a complexidade total
2. **MST Construction**: Praticamente linear com otimizações
3. **Output**: O(k) onde k é o número de arestas pesadas (k ≤ m)

## 🎲 Casos Especiais Relevantes

### 1. **Grafo sem ciclos (Floresta)**
```
Entrada: 3 2
         0 1 1
         1 2 2
Output: forest
```
- Não existem arestas pesadas
- Todas as arestas fazem parte de uma MST

### 2. **Aresta isolada (não conecta componentes)**
```
Entrada: 4 5
         0 1 1
         1 2 2
         2 0 3
         3 2 4
         3 0 5
Output: 4 5 (ou similar)
```

### 3. **Ciclo simples**
```
Entrada: 3 3
         0 1 1
         1 2 2
         2 0 3
Output: 3
```
- Apenas a aresta mais pesada é pesada

### 4. **Múltiplas arestas com mesmo peso**
```
Entrada: 4 6
         0 1 10
         1 2 10
         2 3 10
         3 0 10
         0 2 10
         1 3 10
```
- Possível ter múltiplas MSTs válidas

### 5. **Grafo desconexo (Floresta com múltiplas componentes)**
```
Entrada: 4 2
         0 1 5
         2 3 7
Output: forest
```
- Sem ciclos, nenhuma aresta pesada

### 6. **Grande número de arestas pesadas**
```
Entrada: 5 10
         (múltiplas arestas redundantes)
Output: (muitos pesos)
```

## 📸 Evidência de Aceitação

![Accepted Screenshot](https://github.com/NicolasDev-web/ArvoreGeradoraMinima/blob/main/evidencias/accepted.png)

**Status**: ✅ **ACCEPTED**

Link da submissão: [UVA Online Judge](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2847)

## 📁 Estrutura do Projeto

```
ArvoreGeradoraMinima/
├── src/
│   ├── Main.java                 # Classe principal
│   ├── Edge.java                 # Classe para representar arestas
│   ├── HeavyCycleEdges.java      # Algoritmo de Kruskal modificado
│   ├── UF.java                   # Union-Find com otimizações
│   └── Queue.java                # Implementação de fila
├── dados/
│   └── entradas_do_problema.txt  # Casos de teste
├── evidencias/
│   └── accepted.png              # Evidência de aceitação
└── README.md                      # Este arquivo
```

## 🔍 Descrição das Classes

### Edge.java
- Representa uma aresta do grafo
- Implementa `Comparable` para ordenação por peso
- Métodos: `weight()`, `either()`, `other(int)`

### UF.java
- Implementação de Union-Find com otimizações
- **Path Compression**: Reduz altura da árvore
- **Union by Rank**: Sempre conecta árvore menor à maior
- Métodos: `find(int)`, `union(int, int)`, `connected(int, int)`

### HeavyCycleEdges.java
- Implementa o algoritmo de Kruskal
- Detecta arestas que criariam ciclos
- Armazena pesos das arestas pesadas em uma fila

### Queue.java
- Implementação de fila com lista ligada
- Genérica e iterável
- Métodos: `enqueue()`, `dequeue()`, `isEmpty()`, `peek()`

### Main.java
- Lê múltiplos casos de teste
- Processa cada grafo com `HeavyCycleEdges`
- Imprime resultado no formato esperado

## 💡 Conceitos-Chave Abordados

1. ✅ **Algoritmo de Kruskal** para MST
2. ✅ **Estrutura Union-Find** com otimizações
3. ✅ **Detecção de ciclos** em grafos
4. ✅ **Ordenação de arestas** por peso
5. ✅ **Análise de complexidade** amortizada
6. ✅ **Implementação de estruturas de dados** personalizadas

## 📚 Referências

- [Kruskal's Algorithm - CP Algorithms](https://cp-algorithms.com/graph/mst_kruskal.html)
- [Union-Find Data Structure](https://cp-algorithms.com/dsa/dsu.html)
- [UVA Online Judge - Problem 10397](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2847)
- Introduction to Algorithms (CLRS)

## 📝 Notas

- O projeto utiliza índices de vértices começando do 0
- O programa processa múltiplos casos de teste até receber "0 0"
- Arestas pesadas são impressas em ordem crescente de peso
- Se não houver arestas pesadas, imprime "forest"

---

**Desenvolvido como projeto acadêmico sobre Estruturas de Dados e Algoritmos**
