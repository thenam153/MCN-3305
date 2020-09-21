import math

def prob(n, p, N):
    return math.comb(N, n) * pow(p, n) * pow(1 - p, N - n)
def infoMeasure(n, p, N):
    return -math.log2(prob(n, p, N))
def sumProb(N, p):
    xs = 0.0
    for s in range(0, N + 1):
        xs += prob(s, p, N)
    return xs
def approxEntropy(N, p):
    entropy = 0.0
    for e in range(0, N + 1):
        entropy += prob(e, p, N) * infoMeasure(e, p, N)
    return entropy

print(sumProb(5, 1/3))