import math

def prob(n, p, r):
    return math.comb(n - 1,  r - 1) * pow(p, r) * pow(1 - p, n - r)
def infoMeasure(n, p, r):
    return -math.log2(prob(n, p, r))
def sumProb(N, p, r):
    xs = 0.0
    for s in range(1, N + 1):
        xs += prob(s, p, r)
    return xs
def approxEntropy(N, p, r):
    entropy = 0.0
    for e in range(r, N + 1):
        entropy += prob(e, p, r) * infoMeasure(e, p, r)
    return entropy

print(sumProb(1000000, 1/2))