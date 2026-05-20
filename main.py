#ESTUDANDO AINDA POR ISSO OS COMENTÁRIOS SÃO BEM EXPLICATIVOS, PARA ME AJUDAR A ENTENDER MELHOR O CÓDIGO
class DSU:
    def __init__(self, n):
        # Inicialmente, cada vértice é seu próprio "pai" (ou seja, cada um forma um conjunto isolado)
        self.parent = list(range(n))
        # O 'rank' é usado para otimizar a união das árvores, mantendo-as rasas.
        # Todos começam com rank 0 (árvores de altura 1).
        self.rank = [0] * n

    def find(self, i):
        # O método 'find' descobre a qual conjunto o vértice 'i' pertence, 
        # buscando quem é o "representante" (ou raiz) desse conjunto.
        
        if self.parent[i] != i:
            # OTIMIZAÇÃO: Path Compression (Compressão de Caminho)
            # Durante a busca recursiva, já atualizamos o pai do vértice atual 
            # diretamente para a raiz do conjunto. Isso achata a árvore e 
            # faz com que as próximas buscas sejam quase instantâneas.
            self.parent[i] = self.find(self.parent[i])
            
        return self.parent[i]

    def union(self, i, j):
        # O método 'union' tenta juntar os conjuntos dos vértices 'i' e 'j'.
        # Primeiro, encontramos os representantes (raízes) de ambos.
        root_i = self.find(i)
        root_j = self.find(j)

        # Se as raízes são iguais, eles JÁ ESTÃO no mesmo conjunto.
        # Adicionar uma aresta entre eles formaria um CICLO!
        if root_i == root_j:
            return False # Retorna False para avisar que a união não foi feita (ciclo detectado)

        # OTIMIZAÇÃO: Union by Rank (União por Classificação/Tamanho)
        # Se eles estão em conjuntos diferentes, anexamos a árvore menor à raiz da árvore maior.
        if self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        elif self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        else:
            # Se tiverem o mesmo tamanho, escolhemos um para ser a nova raiz
            # e aumentamos o seu rank em 1.
            self.parent[root_j] = root_i
            self.rank[root_i] += 1
            
        return True # Retorna True indicando que a união foi um sucesso (sem ciclos)