import numpy as np
from scipy.stats import norm

def runs_test(sequence):
    median = np.median(sequence)
    signs = ['+' if val > median else '-' for val in sequence]

    
    runs = 1
    for i in range(1, len(signs)):
        if signs[i] != signs[i-1]:
            runs += 1

    n1 = signs.count('+')
    n2 = signs.count('-')
    n = n1 + n2

    if n1 == 0 or n2 == 0:
        print("All values fall on one side of median — not suitable for test.")
        return

    expected = (2 * n1 * n2) / n + 1
    variance = (2 * n1 * n2 * (2 * n1 * n2 - n)) / (n**2 * (n - 1))

    z = (runs - expected) / np.sqrt(variance)
    p_value = 2 * (1 - norm.cdf(abs(z)))

    print(f"Runs: {runs}")
    print(f"Expected Runs: {expected:.2f}")
    print(f"Z-score: {z:.2f}")
    print(f"P-value: {p_value:.4f}")

    if p_value < 0.05:
        print("Reject H₀ — sequence may not be random.")
    else:
        print("Fail to reject H₀ — sequence appears random.")


runs_test(fl)
