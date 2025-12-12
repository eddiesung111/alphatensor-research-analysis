import numpy as np
import time

def standard_multiply(A, B):
    return np.dot(A, B)

# Benchmarking
N = 1000
A = np.random.rand(N, N)
B = np.random.rand(N, N)

start = time.time()
C = standard_multiply(A, B)
print(f"Time taken for {N}x{N}: {time.time() - start:.4f} seconds")
