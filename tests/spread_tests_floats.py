import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy as scipy_entropy
from statsmodels.sandbox.stats.runs import runstest_1samp


with open("keystroke_floats.txt") as f:
    floats = [float(line.strip()) for line in f if line.strip()]

arr = np.array(floats)


plt.hist(arr, bins=50, color='coral', edgecolor='black')
plt.title("Float Distribution Histogram")
plt.xlabel("Float Value")
plt.ylabel("Frequency")
plt.show()

binned, _ = np.histogram(arr, bins=100, range=(0,1), density=True)
binned = binned[binned > 0]
shannon_entropy = scipy_entropy(binned, base=2)
print(f"Shannon Entropy (approx): {shannon_entropy:.4f} bits (out of max ~6.6 for 100 buckets)")


median = np.median(arr)
runs_test_data = np.array([1 if x > median else 0 for x in arr])
z_stat, p_val = runstest_1samp(runs_test_data)
print(f"Runs Test: z = {z_stat:.4f}, p = {p_val:.4f}")
if p_val > 0.05:
    print("Runs test passed (no significant pattern)")
else:
    print("Runs test failed (non-randomness suspected)")


def autocorr(x, lag=1):
    return np.corrcoef(x[:-lag], x[lag:])[0,1]

ac = autocorr(arr, lag=1)
print(f"Lag-1 autocorrelation: {ac:.4f}")
if abs(ac) < 0.1:
    print("No significant autocorrelation")
else:
    print("Significant autocorrelation")

### Optional: Convert to Bitstream 
def floats_to_bits(floats, bits=10):
    max_val = 2 ** bits - 1
    int_vals = (np.array(floats) * max_val).astype(int)
    return ''.join(format(v, f'0{bits}b') for v in int_vals)

bitstream = floats_to_bits(arr, bits=10)
print(f"Generated bitstream length: {len(bitstream)} bits")

# Optionally: write to file
# with open("float_bitstream.bin", "w") as f:
#     f.write(bitstream)
