import math

def prob(n, p):
    return p * pow(1 - p, n - 1)
def infoMeasure(n, p):
    return -math.log2(prob(n, p))
def sumProb(N, p):
    """
        Dùng phương pháp thực nghiệm tính toán cho thấy
        hàm sumProb trả về giá trị 1 
    """
    xs = 0.0
    for s in range(1, N + 1):
        xs += prob(s, p)
    return xs
def approxEntropy(N, p):
    entropy = 0.0
    for e in range(1, N + 1):
        entropy += prob(e, p) * infoMeasure(e, p)
    return entropy

print(sumProb(500, 0.5))