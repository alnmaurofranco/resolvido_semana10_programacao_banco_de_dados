import random
import math

def vector_sum (vetores):
    result = vetores[0]
    for vetor in vetores[1:]:
        result = [result[i] + vetor[i] for i in range(len(vetor))]
    return result

def scalar_multiply (escalar, vetor):
    return [escalar * i for i in vetor]

def vector_mean(vetores):
    return scalar_multiply(1/len(vetores), vector_sum(vetores))

def vector_subtract (v, w):
    return [v_i - w_i for v_i, w_i in zip (v, w)]

def dot (v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares (v):
    return dot (v, v)

def squared_distance (v, w):
    return sum_of_squares (vector_subtract(v, w))

def distance (v, w):
    return math.sqrt(squared_distance(v, w))

class KMeans:
    def __init__ (self, k, means):
        self.k = k
        self.means = means

    def classify (self, ponto):
        return min(range(self.k), key = lambda i: squared_distance(ponto, self.means[i]))

    def train (self, pontos):
        assignments = None
        while True:
            new_assignments = list(map(self.classify, pontos))

            if new_assignments != assignments:
                assignments = new_assignments
                for i in range (self.k):
                    points = [p for p, a in zip (pontos, assignments) if a == i]
                    if points:
                        self.means[i] = vector_mean (points)

def the_best_k (base, i, limiar):
    k = 2
    m = 0.0
    banco_dados = base[0]
    selecionado_dados = base[1]
    
    while k <= i:
        kmeans = KMeans(k, selecionado_dados)
        kmeans.train(banco_dados)
        km = kmeans.means
        m = vector_mean(km)
        if (m[0] < limiar):
            indice_menor_k = k
        k =+ 1
    return indice_menor_k

def test_k_means ():
    dados = [[1], [3], [6], [7], [10], [11], [17], [20], [28]]
    selecionado_dados = [[3], [7], [17], [20]]
    base = [dados, selecionado_dados]

    i = 4
    limiar = 16
    menor_k = the_best_k(base, i, limiar)
    print(f'Limiar: {limiar}')
    print(f'Menor K: {menor_k}')

def main():
    test_k_means()

main()