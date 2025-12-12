import numpy as np
import matplotlib.pyplot as plt

def theoretical_operations(N, algo='standard'):
    if algo == 'standard':
        return N ** 3
    elif algo == 'strassen':
        return N ** 2.807
    elif algo == 'alphatensor':
        # AlphaTensor improved on specific sizes, but generally follows Strassen-like scaling
        return N ** 2.77  # A hypothetical improvement for visualization

# Generate N sizes
N_values = np.linspace(10, 1000, 100)

# Calculate ops
ops_std = theoretical_operations(N_values, 'standard')
ops_str = theoretical_operations(N_values, 'strassen')
ops_alpha = theoretical_operations(N_values, 'alphatensor')

# Plot
plt.figure(figsize=(10, 6))
plt.plot(N_values, ops_std, label='Standard O(N^3)', linestyle='--')
plt.plot(N_values, ops_str, label='Strassen O(N^2.81)')
plt.plot(N_values, ops_alpha, label='AlphaTensor (Discovery)', linewidth=2)

plt.xlabel('Matrix Size (N)')
plt.ylabel('Operations (Theoretical)')
plt.title('Why AlphaTensor Matters: Algorithmic Complexity Scaling')
plt.legend()
plt.grid(True)
plt.savefig('complexity_comparison.png')
plt.show()
